import json
from datetime import datetime
import os


def snapshot_opslaan(aandelen_compleet_inclusief_gewicht, totaalwaarden_portfolio):
    """
    Slaat een JSON-snapshot op van de actuele portfolio data, inclusief datum in bestandsnaam.

    Parameters:
    aandelen_compleet_inclusief_gewicht (DataFrame): DataFrame met per ticker de berekende waarden
    als kolommen.
    totaalwaarden_portfolio (dict): dictionary met portfolio totalen als keys en berekende waarden
    als values.
    """

    aandelen_compleet = aandelen_compleet_inclusief_gewicht.to_dict(orient="records")

    compleet_overzicht = {
        "aandelen_overzicht": aandelen_compleet,
        "totaalwaarden": totaalwaarden_portfolio,
    }

    datum = datetime.now().strftime("%Y-%m-%d")

    with open(f"snapshots/snapshot_{datum}.json", "w") as f:
        json.dump(compleet_overzicht, f, indent=4, ensure_ascii=False)


def vorige_snapshot_inlezen():
    """
    Leest de portfolio data in van de laatste JSON-snapshot.

    Returns:
    dict: dictionary van de meest recente portfolio data.
    """

    snapshot_lijst = os.listdir("snapshots/")

    laatste_snapshot = sorted(snapshot_lijst)[-1]

    with open(f"snapshots/{laatste_snapshot}", "r") as f:
        data = json.load(f)

    return data
