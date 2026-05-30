import pandas as pd


def aandelen_per_aankoop_berekenen(df):
    """
    Haalt per aankoop het aantal aandelen op uit de Excel-data.

    Parameters:
    df (DataFrame): dataframe met de kolom Aantal Aandelen.

    Returns:
    Series: aantal aandelen per aankoop.
    """
    aantal_aandelen = df["Aantal Aandelen"]

    return aantal_aandelen


def aantal_aandelen_per_sheet(schone_sheets):
    """
    Berekent per aandelensheet hoeveel aandelen er zijn gekocht per maand.

    Parameters:
    schone_sheets (dict): dict met tickers als keys en schone DataFrames als values.

    Returns:
    dict: dict met tickers als keys en Series met het aantal gekochte aandelen
    per maand als values.
    """
    aandelen_per_sheet = {}

    for sheet_naam, df in schone_sheets.items():
        aandelen_per_sheet[sheet_naam] = aandelen_per_aankoop_berekenen(df)

    return aandelen_per_sheet


def totaal_aantal_aandelen_berekenen(aandelen_per_sheet):
    """
    Berekent per aandelensheet het totaal aantal gekochte aandelen.

    Parameters:
    aandelen_per_sheet (dict): dict met tickers als keys en Series met
    gekochte aandelen per aankoop als values.

    Returns:
    dict: dict met tickers als keys en totaal aantal gekochte aandelen als values.
    """

    totaal_aantal_aandelen = {}

    for sheet_naam, aandelen in aandelen_per_sheet.items():
        totaal_aantal_aandelen[sheet_naam] = aandelen.sum()

    return totaal_aantal_aandelen


def verkochte_aandelen_aftrekken(totaal_aantal_aandelen, df):
    """
    Trekt per ticker de verkochte aandelen af van het totaal aantal aandelen

    Parameters:
    totaal_aantal_aandelen (dict): dictionary waarbij de Ticker de key is en aantal
    aandelen de value.
    df (DataFrame): dataframe met de kolommen 'Aandeel' en 'Aantal Verkocht'.

    Returns:
    dict: dictionary met Ticker als key en bijgewerkt aantal aandelen na aftrek van
    verkopen als value.
    """

    for index, rij in df.iterrows():
        if rij["Aandeel"] in totaal_aantal_aandelen:
            totaal_aantal_aandelen[rij["Aandeel"]] -= rij["Aantal Verkocht"]

    return totaal_aantal_aandelen


def totale_investering_en_kosten(schone_sheets):
    """
    Geef per sheet: totale investering, totale kosten en totale investering inclusief kosten.

    Parameters:
    schone_sheets (dict): dictionary met sheetnamen als keys en schoongemaakte
    DataFrames als values.

    Returns:
    tuple: Drie dictionaries:
    totale_investering bevat per sheet de som van de kolom "Geïnvesteerd".
    totale_kosten bevat per sheet de som van de kolom "Kosten".
    totale_investering_inclusief_kosten bevat per sheet investering plus kosten.
    """

    totale_investering = {}
    totale_kosten = {}
    totale_investering_inclusief_kosten = {}

    for sheet_naam, sheet_data in schone_sheets.items():
        totale_investering[sheet_naam] = sheet_data["Geïnvesteerd"].sum()
        totale_kosten[sheet_naam] = sheet_data["Kosten"].sum()

        totale_investering_inclusief_kosten[sheet_naam] = (
            totale_investering[sheet_naam] + totale_kosten[sheet_naam]
        )

    return totale_investering, totale_kosten, totale_investering_inclusief_kosten


def gak_berekenen(totale_investering_inclusief_kosten, totaal_aantal_aandelen):
    """
    Berekent de GAK (Gemiddelde Aankoopprijs) per sheet.

    Parameters:
    totale_investering_inclusief_kosten (dict): dictionary met sheetnaam als key
    en totale investering inclusief kosten als value.
    totaal_aantal_aandelen (dict): dictionary met sheetnaam als key en totaal aantal
    aandelen als value.

    Returns:
    gak_per_aandeel (dict): dictionary met sheetnaam als key en GAK als value.
    """

    gak_per_sheet = {}

    for sheet_naam, investering in totale_investering_inclusief_kosten.items():
        if totaal_aantal_aandelen[sheet_naam] == 0:
            gak_per_sheet[sheet_naam] = 0
        else:
            gak_per_sheet[sheet_naam] = (
                totale_investering_inclusief_kosten[sheet_naam]
                / totaal_aantal_aandelen[sheet_naam]
            )

    return gak_per_sheet


def huidige_waarde_berekenen(aantal_aandelen, huidige_prijs):
    """
    Berekent de huidige waarde van één aandeelpositie.

    Parameters:
    aantal_aandelen (float): het aantal aandelen dat je bezit.
    huidige_prijs (float): de huidige prijs van één aandeel.

    Returns:
    float: de huidige waarde van deze aandeelpositie.
    """

    huidige_waarde = aantal_aandelen * huidige_prijs

    return huidige_waarde


def alle_huidige_waarden_berekenen(totaal_aandelen, huidige_prijzen):
    """
    Berekent de huidige waarde per ticker.

    Parameters:
    totaal_aandelen (dict): per ticker het totaal aantal aandelen dat je bezit.
    huidige_prijzen (dict): per ticker de huidige prijs van één aandeel.

    Returns:
    dict: per ticker de huidige waarde van de aandeelpositie.
    """

    alle_huidige_waarden = {}

    for ticker, aantal_aandelen in totaal_aandelen.items():
        huidige_prijs = huidige_prijzen[ticker]
        huidige_waarde = huidige_waarde_berekenen(aantal_aandelen, huidige_prijs)
        alle_huidige_waarden[ticker] = huidige_waarde

    return alle_huidige_waarden


def winst_verlies_berekenen(huidige_waarde, totale_investering_inclusief_kosten):
    """
    Berekent de winst of verlies van een ticker.

    Parameters:
    huidige_waarde (float): de huidige waarde van het aandeel.
    totale_investering_inclusief_kosten (float): de totale investering inclusief
    kosten van dit aandeel.

    Returns:
    float: de winst of verlies van een ticker.
    """
    winst_verlies_uitkomst = huidige_waarde - totale_investering_inclusief_kosten

    return winst_verlies_uitkomst


def alle_winst_verlies_berekenen(
    alle_huidige_waarden, totale_investering_inclusief_kosten
):

    alle_winst_verlies = {}

    for ticker, huidige_waarde in alle_huidige_waarden.items():
        winst_verlies = winst_verlies_berekenen(
            huidige_waarde, totale_investering_inclusief_kosten[ticker]
        )
        alle_winst_verlies[ticker] = winst_verlies

    return alle_winst_verlies


def rendement_berekenen(winst_verlies_uitkomst, totale_investering_inclusief_kosten):
    """
    Berekent het rendement in procenten voor een Ticker.

    Parameters:
    winst_verlies_uitkomst (float): de winst of verlies voor een Ticker.
    totale_investering_inclusief_kosten (float): de totale investering inclusief kosten
    voor een Ticker.

    Returns:
    float: het rendement voor een Ticker.
    """
    rendement_som = (winst_verlies_uitkomst / totale_investering_inclusief_kosten) * 100

    return rendement_som


def alle_rendementen_berekenen(alle_winst_verlies, totale_investering_inclusief_kosten):
    """
    Berekent het rendement in procenten voor iedere Ticker.

    Parameters:
    alle_winst_verlies (dict): dictionary waarbij de Ticker de key is en het winst/verlies de value.
    totale_investering_inclusief_kosten (dict): dictionary waarbij de Ticker de key is en de totale
    investering inclusief kosten de value.

    Returns:
    dict: dictionary waarbij de key de Ticker is en het rendement percentage de value.
    """

    alle_rendement = {}

    for ticker, winst_verlies_uitkomst in alle_winst_verlies.items():
        rendement = rendement_berekenen(
            winst_verlies_uitkomst, totale_investering_inclusief_kosten[ticker]
        )
        alle_rendement[ticker] = rendement

    return alle_rendement


def alle_aandelen_samenvoegen(
    totaal_aandelen,
    totale_investering_inclusief_kosten,
    gak,
    huidige_prijzen,
    huidige_waarde,
    winst_verlies,
    rendement,
):
    """
    Combineert alle berekende waarden per ticker in één overzichtelijk DataFrame.

    Parameters:
    totaal_aandelen (dict): {ticker: totaal aantal aandelen}
    totale_investering_inclusief_kosten (dict): {ticker: totale investering inclusief kosten in €}
    gak (dict): {ticker: gemiddelde aankoopkoers in €}
    huidige_prijzen (dict): {ticker: actuele prijs in €}
    huidige_waarde (dict): {ticker: huidige waarde van de positie in €}
    winst_verlies (dict): {ticker: winst of verlies in €}
    rendement (dict): {ticker: rendement in %}

    Returns:
    pd.DataFrame: per rij één ticker met alle berekende waarden als kolommen.
    """
    alle_aandelen_samen = []

    for ticker, aantal in totaal_aandelen.items():
        rij = {
            "Naam aandeel": ticker,
            "Aantal stuks": aantal,
            "Totale investering (€)": totale_investering_inclusief_kosten[ticker],
            "Huidige prijs (€)": huidige_prijzen[ticker],
            "Huidige waarde (€)": huidige_waarde[ticker],
            "GAK (€)": gak[ticker],
            "Winst/Verlies (€)": winst_verlies[ticker],
            "Rendement (%)": rendement[ticker],
        }

        alle_aandelen_samen.append(rij)

    return pd.DataFrame(alle_aandelen_samen)
