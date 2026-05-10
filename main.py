from excel_utils import verwerk_excel_data
from aandelen_berekeningen import aantal_aandelen_per_sheet

# Controleer de schone sheets en bereken het aantal aandelen
schone_sheets = verwerk_excel_data()

if schone_sheets is not None:
    print(schone_sheets.keys())

    aantal_aandelen = aantal_aandelen_per_sheet(schone_sheets)
    print(aantal_aandelen.keys())
else:
    print("Geen data om te tonen")
