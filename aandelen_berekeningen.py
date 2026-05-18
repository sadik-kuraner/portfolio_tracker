def aandelen_per_aankoop_berekenen(df):
    """
    Berekent hoeveel aandelen je hebt gekocht obv je geïnvesteerd bedrag en aankoopprijs.

    Parameters:
    df (DataFrame): dataframe met de kolommen Geïnvesteerd en Aankoopprijs.

    Returns:
    Series: aantal aandelen per aankoop.

    """
    aantal_aandelen = df["Geïnvesteerd"] / df["Aankoopprijs"]

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
