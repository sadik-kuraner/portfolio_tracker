import pandas as pd


def input_excel_lezen(
    bestandspad="EDCA - Aandelen.xlsx",
    gekozen_sheets=None,
):
    """
    Leest een Excel-bestand in en haalt de gekozen sheets op.

    Parameters:
    bestandspad (str): het pad naar het Excel-bestand.
    gekozen_sheets (list | None): de namen van de sheets die ingelezen moeten worden.
        Als dit None is, worden de standaard sheets gebruikt.

    Returns:
    dict | None: De geselecteerde sheets als pandas DataFrames.
        Geeft None terug als het bestand niet gelezen kan worden (error).
    """
    if gekozen_sheets is None:
        gekozen_sheets = [
            "NVD.DE",
            "AMD.DE",
            "1YD.DE",
            "AMZ.DE",
            "6B0.MU",
            "TOITF",
            "MSF.DE",
        ]

    try:
        aandelen_sheets = pd.read_excel(bestandspad, sheet_name=gekozen_sheets)
        return aandelen_sheets
    except FileNotFoundError:
        print("Dit bestand bestaat niet. Voer de juiste bestandsnaam in")
        return None
    except ValueError:
        print("Eén of meer sheetnamen bestaan niet in dit Excel-bestand")
        return None
    except ImportError:
        print("Python mist een package om Excel te lezen. Installeer bijv. openpyxl.")
        return None


def clean_data(df):
    """
    Maakt één dataframe schoon voor de analyse.

    Parameters:
    df (DataFrame): dataframe die schoongemaakt moet worden.

    Returns:
    DataFrame: dataframe met alleen de gewenste kolommen die nodig zijn
    voor de berekeningen, zonder lege rijen en zonder de rij "Totaal".
    """

    # Pak alleen de eerste rijen en kolommen waar de tabel staat
    df = df.iloc[:37, :8]

    # Verwijder de volledig lege rijen
    df = df.dropna(how="all")

    # Gebruik de eerste kolom om de rij "Totaal" te verwijderen
    eerste_kolom = df.iloc[:, 0].astype(str)
    df = df[~eerste_kolom.str.contains("Totaal", case=False, na=False)]

    # Bewaar daarna alleen de kolommen die je echt nodig hebt
    df = df[["Maand", "Geïnvesteerd", "Aankoopprijs", "Aantal Aandelen", "Kosten"]]

    return df


def verwerk_excel_data():
    """
    Leest Excel-data in en maakt elke sheet schoon.

    Returns:
    (dict | None): dictionary met sheetnamen als keys en schoongemaakte
    DataFrames als values. Geeft None terug als het Excel-bestand niet gelezen kan worden.
    """

    excel_data = input_excel_lezen()

    if excel_data is None:
        return None

    schone_sheets = {}

    for sheet_naam, df in excel_data.items():
        schone_sheets[sheet_naam] = clean_data(df)

    return schone_sheets


def verkochte_aandelen_lezen(bestandspad="EDCA - Aandelen.xlsx"):
    """
    Leest de data vanuit de "Verkocht" sheet en verwijdert lege rijen en kolommen.
    Verwijdert daarnaast de 'Totaal' rij en filtert op twee kolommen.

    Parameters:
    bestandspad (str): het pad naar het Excel-bestand.

    Returns:
    DataFrame: de kolommen 'Aandeel' en 'Aantal Verkocht' vanuit de geselecteerde sheet als DataFrame.
    """

    verkocht_sheet_inlezen = pd.read_excel(bestandspad, sheet_name="Verkocht")

    df = verkocht_sheet_inlezen

    df = df.dropna(how="all")

    eerste_kolom = df.iloc[:, 0].astype(str)
    df = df[~eerste_kolom.str.contains("Totaal", case=False, na=False)]

    df = df[["Aandeel", "Aantal Verkocht"]]

    return df


def rijen_overslaan(schone_sheets, aantal_rijen, ticker="AMD.DE"):
    """
    Verwijdert de eerste (aantal_rijen) rijen van de opgegeven ticker uit schone_sheets.

    Parameters:
    schone_sheets (dict): dictionary met Tickers als key en schoongemaakt DataFrames
    als value.
    aantal_rijen (int): het aantal rijen dat verwijderd moet worden.
    ticker (str): de naam van de Ticker.

    Returns:
    dict: Ticker als key en de DataFrame zonder de eerste aantal rijen als value.
    """

    if ticker in schone_sheets:
        df = schone_sheets[ticker]
        schone_sheets[ticker] = df.iloc[aantal_rijen:]

    return schone_sheets


def gewicht_toevoegen_aan_df(alle_aandelen_samen, gewicht_per_aandeel):
    """
    Voegt de kolom 'Gewicht (%)' toe aan de alle_aandelen DataFrame.

    Parameters:
    alle_aandelen_samen (DataFrame): DataFrame met een totaaloverzicht van
    alle aandelen inclusief de kolommen.
    gewicht_per_aandeel (dict): dictionary waarbij de Ticker de key is
    en het gewicht de value.

    Returns:
    alle_aandelen_samen DataFrame: DataFrame met per ticker de berekende waarden
    als kolommen.
    """

    df = alle_aandelen_samen

    df["Gewicht (%)"] = df["Naam aandeel"].map(gewicht_per_aandeel)

    return df
