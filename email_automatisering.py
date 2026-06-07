import json
from datetime import datetime


def snapshot_opslaan(aandelen_compleet_inclusief_gewicht, totaalwaarden_portfolio):
    """
    Slaat een JSON-snapshot op van de actuele portfolio data, inclusief datum in bestandsnaam.

    Parameters:
    aandelen_compleet_inclusief_gewicht (DataFrame): DataFrame met per ticker de berekende waarden
    als kolommen.
    totaalwaarden_portfolio (dict): dictionary met portfolio totalen als keys en berekende waarden
    als values.
    """

    aandelen_compleet = aandelen_compleet_inclusief_gewicht.to_dict()

    compleet_overzicht = {
        "aandelen_overzicht": aandelen_compleet,
        "totaalwaarden": totaalwaarden_portfolio,
    }

    datum = datetime.now().strftime("%d-%m-%Y")

    with open(f"snapshot_{datum}.json", "w") as f:
        json.dump(compleet_overzicht, f)
