from excel_utils import verwerk_excel_data, rijen_overslaan, gewicht_toevoegen_aan_df
from aandelen_berekeningen import (
    aantal_aandelen_per_sheet,
    totaal_aantal_aandelen_berekenen,
    totale_investering_en_kosten,
    gak_berekenen,
    alle_huidige_waarden_berekenen,
    alle_winst_verlies_berekenen,
    alle_rendementen_berekenen,
    alle_aandelen_samenvoegen,
    totaalwaarde_portfolio_berekenen,
    gewicht_per_aandeel_berekenen,
)

from aandelen_prijs_ophalen import alle_huidige_prijzen_ophalen

# Verwerk de Excel-data zodat de berekeningen met schone gegevens werken
schone_sheets = verwerk_excel_data()

# Verwijder de eerste 3 rijen van AMD.DE (verkochte aankopen)
schone_sheets = rijen_overslaan(schone_sheets, aantal_rijen=3, ticker="AMD.DE")

if schone_sheets is not None:
    # Bereken hoeveel aandelen er per ticker en in totaal zijn
    aantal_aandelen = aantal_aandelen_per_sheet(schone_sheets)
    totaal_aandelen = totaal_aantal_aandelen_berekenen(aantal_aandelen)

    # Bereken hoeveel geld er totaal is geïnvesteerd, inclusief kosten
    totale_investering, totale_kosten, totale_investering_inclusief_kosten = (
        totale_investering_en_kosten(schone_sheets)
    )

    # Bereken de gemiddelde aankoopkoers per aandeel
    gak = gak_berekenen(totale_investering_inclusief_kosten, totaal_aandelen)

    # Haal de actuele prijzen op voor alle tickers uit het Excel-bestand
    tickers = list(schone_sheets.keys())
    huidige_prijzen = alle_huidige_prijzen_ophalen(tickers)

    # Bereken de huidige waarde van elke aandeelpositie
    huidige_waarde = alle_huidige_waarden_berekenen(totaal_aandelen, huidige_prijzen)

    # Bereken de winst of verlies van elke aandeelpositie
    winst_verlies = alle_winst_verlies_berekenen(
        huidige_waarde, totale_investering_inclusief_kosten
    )

    # Bereken het rendement in percentages van elke aandeelpositie
    rendement = alle_rendementen_berekenen(
        winst_verlies, totale_investering_inclusief_kosten
    )

    # Combineer alle berekende waarden per ticker in één overzichtelijk tabel
    alle_aandelen_compleet = alle_aandelen_samenvoegen(
        totaal_aandelen,
        totale_investering_inclusief_kosten,
        gak,
        huidige_prijzen,
        huidige_waarde,
        winst_verlies,
        rendement,
    )

    totaalwaarden_portfolio = totaalwaarde_portfolio_berekenen(alle_aandelen_compleet)

    # Bereken het gewicht van elke aandeelpositie als percentage van het totale portfolio
    gewicht_per_aandeel = gewicht_per_aandeel_berekenen(
        alle_aandelen_compleet, totaalwaarden_portfolio
    )

    # Voeg kolom 'Gewicht (%)' toe aan alle_aandelen_compleet DataFrame
    aandelen_compleet_inclusief_gewicht = gewicht_toevoegen_aan_df(
        alle_aandelen_compleet, gewicht_per_aandeel
    )

    # Toon de belangrijkste resultaten in de terminal
    print(totaal_aandelen)
    print(totale_investering_inclusief_kosten)
    print(gak)
    print(huidige_prijzen)
    print(huidige_waarde)
    print(winst_verlies)
    print(rendement)
    print(alle_aandelen_compleet)
    print(totaalwaarden_portfolio)
    print(gewicht_per_aandeel)
    print(aandelen_compleet_inclusief_gewicht)

else:
    print("Geen data om te tonen")
