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
