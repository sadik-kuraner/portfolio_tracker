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
