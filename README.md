# Portfolio Tracker

Python script dat automatisch een portfolio overzicht genereert op basis van een Excel-bestand met maandelijkse aankoopdata. Elke week wordt er een e-mail verstuurd met het portfolio overzicht als Excel-bijlage en een korte samenvatting gegenereerd via de Claude API.

## Wat doet het?

- Berekent per aandeel: aantal stuks, totale investering, GAK, huidige waarde, winst/verlies en rendement
- Haalt actuele aandeelprijzen op via yfinance
- Exporteert het overzicht naar Excel
- Slaat een wekelijkse JSON-snapshot op voor vergelijking
- Genereert een samenvatting via de Claude API (Haiku)
- Verstuurt een e-mail met Excel-bijlage en samenvatting

## Installatie

1. Zorg dat [uv](https://github.com/astral-sh/uv) is geïnstalleerd
2. Clone de repository
3. Installeer de dependencies:

```bash
uv sync
```

4. Maak een `.env` bestand aan op basis van `.env.example` en vul je API key en wachtwoord in:

```
ANTHROPIC_API_KEY=sk-ant-...
EMAIL_WACHTWOORD=je-app-wachtwoord
```

## Gebruik

Portfolio tracker draaien en Excel exporteren:

```bash
uv run main.py
```

Wekelijks e-mailrapport genereren en versturen:

```bash
uv run run_email_rapport.py
```

## Bestandsstructuur

```
portfolio_tracker/
├── main.py                          # Scriptflow portfolio tracker
├── run_email_rapport.py             # Scriptflow e-mail rapport
├── excel_utils.py                   # Excel inlezen en output schrijven
├── aandelen_berekeningen.py         # Portfolio berekeningen
├── aandelen_prijs_ophalen.py        # Actuele prijzen ophalen via yfinance
├── claude_api.py                    # Samenvatting genereren via Claude API
├── email_automatisering.py          # Snapshot opslaan en mail versturen
├── snapshots/                       # Wekelijkse JSON-snapshots
├── EDCA - Aandelen.xlsx             # Input Excel met aankoopdata
└── Aandelen Portfolio Rendement.xlsx # Output Excel met portfolio overzicht
```

## Tickers

NVD.DE, AMD.DE, 1YD.DE, AMZ.DE, 6B0.MU, TOITF, MSF.DE
