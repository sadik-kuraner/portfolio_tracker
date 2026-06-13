from main import run_portfolio_tracker
from email_automatisering import snapshot_opslaan, vorige_snapshot_inlezen

# Runt de portfolio tracker en slaat resultaat op in Excel-bestand
aandelen_compleet_inclusief_gewicht, totaalwaarden_portfolio = run_portfolio_tracker()

# Slaat een JSON-snapshot op van de actuele portfolio data
snapshot_opslaan(aandelen_compleet_inclusief_gewicht, totaalwaarden_portfolio)

# Leest de meest recente JSON-snapshot in
snapshot_inlezen = vorige_snapshot_inlezen()
