# Portfolio Tracker — CLAUDE.md

## Projectomschrijving

Python script dat automatisch een portfolio-overzicht genereert op basis van een Excel-bestand (EDCA) met maandelijkse aankoopdata. Het script berekent per aandeel het aantal stuks, totale investering, GAK, huidige waarde, winst/verlies en rendement, en exporteert het resultaat naar Excel.

Geplande uitbreiding: wekelijkse e-mail via Claude API met portfolio-overzicht en vergelijking met vorige week.

## Bestandsstructuur

- `main.py` — scriptflow, roept alle functies aan in de juiste volgorde
- `excel_utils.py` — Excel inlezen, data opschonen, output naar Excel schrijven
- `aandelen_berekeningen.py` — alle portfolio berekeningen (GAK, waarde, rendement, gewicht etc.)
- `aandelen_prijs_ophalen.py` — actuele aandeelprijzen ophalen via yfinance
- `EDCA - Aandelen.xlsx` — input Excel met aankoopdata per ticker als sheet
- `Aandelen Portfolio Rendement.xlsx` — output Excel met portfolio-overzicht

## Tickers

NVD.DE, AMD.DE, 1YD.DE, AMZ.DE, 6B0.MU, TOITF, MSF.DE

## Status

- Portfolio tracker core: afgerond
- E-mail automatisering via Claude API: in ontwikkeling

## Begeleiding

- Sadik heeft ~6 maanden Python-ervaring en is een gevorderde beginner
- Geef altijd hints eerst, schrijf geen code tenzij expliciet gevraagd
- Leg uit waarom iets werkt, niet alleen wat het doet
- Korte antwoorden, geen onnodige uitleg
