from excel_utils import verwerk_excel_data
from aandelen_berekeningen import (
    aantal_aandelen_per_sheet,
    totaal_aantal_aandelen_berekenen,
    totale_investering_en_kosten,
    gak_berekenen,
)

# Lees de schone sheets in en bereken: totaal aantal aandelen, investering en kosten
schone_sheets = verwerk_excel_data()

if schone_sheets is not None:
    # Bereken de belangrijkste portfolio overzichten
    aantal_aandelen = aantal_aandelen_per_sheet(schone_sheets)
    totaal_aandelen = totaal_aantal_aandelen_berekenen(aantal_aandelen)
    totale_investering, totale_kosten, totale_investering_inclusief_kosten = (
        totale_investering_en_kosten(schone_sheets)
    )
    gak_uitrekenen = gak_berekenen(totale_investering_inclusief_kosten, totaal_aandelen)

    print(totaal_aandelen)
    print(totale_investering_inclusief_kosten)
    print(gak_uitrekenen)

else:
    print("Geen data om te tonen")
