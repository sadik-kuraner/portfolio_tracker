from main import run_portfolio_tracker
from email_automatisering import (
    snapshot_opslaan,
    vorige_snapshot_inlezen,
    mail_versturen,
)
from claude_api import claude_samenvatting_genereren

# Runt de portfolio tracker en slaat resultaat op in Excel-bestand
aandelen_compleet_inclusief_gewicht, totaalwaarden_portfolio = run_portfolio_tracker()

# Leest de meest recente JSON-snapshot in
vorige_snapshot = vorige_snapshot_inlezen()

# Slaat een JSON-snapshot op van de actuele portfolio data
huidige_snapshot = snapshot_opslaan(
    aandelen_compleet_inclusief_gewicht, totaalwaarden_portfolio
)

# Maakt een korte samenvatting van de portfolio data en vergelijkt het met data van vorige week.
samenvatting = claude_samenvatting_genereren(huidige_snapshot, vorige_snapshot)

# Maakt de mail op inclusief bijlagen en verstuurt de mail.
mail_versturen(samenvatting)
