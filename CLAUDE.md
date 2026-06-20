# Portfolio Tracker — CLAUDE.md

## Projectomschrijving

Python script dat automatisch een portfolio-overzicht genereert op basis van een Excel-bestand (EDCA) met maandelijkse aankoopdata. Het script berekent per aandeel het aantal stuks, totale investering, GAK, huidige waarde, winst/verlies en rendement, en exporteert het resultaat naar Excel. Elke vrijdag om 22:00 wordt via GitHub Actions automatisch een e-mail verstuurd met het portfolio-overzicht als bijlage en een samenvatting gegenereerd via de Claude API.

## Bestandsstructuur

- `main.py` — scriptflow portfolio tracker, roept alle functies aan in de juiste volgorde
- `run_email_rapport.py` — scriptflow e-mail rapport
- `excel_utils.py` — Excel inlezen, data opschonen, output naar Excel schrijven
- `aandelen_berekeningen.py` — alle portfolio berekeningen (GAK, waarde, rendement, gewicht etc.)
- `aandelen_prijs_ophalen.py` — actuele aandeelprijzen ophalen via yfinance
- `claude_api.py` — samenvatting genereren via Claude API
- `email_automatisering.py` — snapshot opslaan, inlezen en mail versturen
- `EDCA - Aandelen.xlsx` — input Excel met aankoopdata per ticker als sheet
- `Aandelen Portfolio Rendement.xlsx` — output Excel met portfolio-overzicht

## Tickers

NVD.DE, AMD.DE, 1YD.DE, AMZ.DE, 6B0.MU, TOITF, MSF.DE

## Status

- Portfolio tracker core: afgerond
- E-mail automatisering via Claude API: afgerond
- GitHub Actions voor wekelijkse automatisering: afgerond

## Begeleiding

- Sadik heeft ~6 maanden Python-ervaring en is een gevorderde beginner
- Geef altijd hints eerst, schrijf geen code tenzij expliciet gevraagd
- Leg uit waarom iets werkt, niet alleen wat het doet
- Korte antwoorden, geen onnodige uitleg
