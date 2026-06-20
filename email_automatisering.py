import json
from datetime import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def snapshot_opslaan(aandelen_compleet_inclusief_gewicht, totaalwaarden_portfolio):
    """
    Slaat een JSON-snapshot op van de actuele portfolio data, inclusief datum in bestandsnaam.

    Parameters:
    aandelen_compleet_inclusief_gewicht (DataFrame): DataFrame met per ticker de berekende waarden
    als kolommen.
    totaalwaarden_portfolio (dict): dictionary met portfolio totalen als keys en berekende waarden
    als values.

    Returns:
    dict: dictionary met keys 'aandelen_overzicht' (list) en 'totaalwaarden' (dict).
    """

    aandelen_compleet = aandelen_compleet_inclusief_gewicht.to_dict(orient="records")

    compleet_overzicht = {
        "aandelen_overzicht": aandelen_compleet,
        "totaalwaarden": totaalwaarden_portfolio,
    }

    datum = datetime.now().strftime("%Y-%m-%d")

    with open(f"snapshots/snapshot_{datum}.json", "w") as f:
        json.dump(compleet_overzicht, f, indent=4, ensure_ascii=False)

    return compleet_overzicht


def vorige_snapshot_inlezen():
    """
    Leest de portfolio data in van de laatste JSON-snapshot.

    Returns:
    dict | None: dictionary van de meest recente portfolio data.
    None als er nog geen snapshots zijn.
    """

    snapshot_lijst = os.listdir("snapshots/")

    if not snapshot_lijst:
        return None

    laatste_snapshot = sorted(snapshot_lijst)[-1]

    with open(f"snapshots/{laatste_snapshot}", "r") as f:
        data = json.load(f)

    return data


def mail_versturen(samenvatting, excel_bestand="Aandelen Portfolio Rendement.xlsx"):
    """
    Maakt de mail op inclusief bijlagen en verstuurt de mail.

    Parameters:
    samenvatting (str): beknopte samenvatting van de portfolio data die wordt vergeleken
    met data van vorige week.
    excel_bestand (str): Bestandsnaam van het Excel-rapport dat als bijlage wordt meegestuurd.
    Default: "Aandelen Portfolio Rendement.xlsx".
    """

    # Stel de mail header in (afzender, ontvanger, onderwerp)
    afzender = "kuranersadik@gmail.com"
    ontvanger = "kuranersadik@gmail.com"
    onderwerp = "Wekelijks portfolio rapport"

    msg = MIMEMultipart()

    msg["From"] = afzender
    msg["To"] = ontvanger
    msg["Subject"] = onderwerp

    # Voeg de samenvatting toe als platte tekst
    tekst = MIMEText(samenvatting, "plain")
    msg.attach(tekst)

    # Open het Excel bestand als bytes en maak er een bijlage van
    with open(excel_bestand, "rb") as f:
        bijlage = MIMEBase("application", "octet-stream")
        bijlage.set_payload(f.read())

    # Codeer de bijlage naar base64 voor veilig transport via mail
    encoders.encode_base64(bijlage)

    # Voeg bestandsnaam toe aan de bijlage header
    bijlage.add_header("Content-Disposition", "attachment", filename=excel_bestand)

    # Voeg de bijlage toe aan de mail
    msg.attach(bijlage)

    # Maak een beveiligde verbinding met de mailserver en verstuur de mail
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(afzender, os.environ.get("EMAIL_WACHTWOORD"))
        server.sendmail(afzender, ontvanger, msg.as_string())
