import yfinance as yf


def huidige_prijs_ophalen(ticker):
    """
    Haalt de huidige prijs op van één aandeel

    Parameters:
    ticker (str): de ticker van het aandeel.

    Returns:
    (float): de huidige prijs van het aandeel.
    """

    aandeel = yf.Ticker(ticker)
    informatie = aandeel.info
    huidige_prijs = informatie.get("currentPrice")

    return huidige_prijs


def alle_huidige_prijzen_ophalen(tickers):
    """
    Haalt de huidige prijzen van alle tickers op.

    Parameters:
    tickers (list): een lijst met tickers van de aandelen.

    Returns:
    dict: de ticker als key en de huidige prijs als value.
    """

    prijs_per_ticker = {}

    for ticker in tickers:
        prijs_per_ticker[ticker] = huidige_prijs_ophalen(ticker)

    return prijs_per_ticker
