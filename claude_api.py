import os
import anthropic
from dotenv import load_dotenv


load_dotenv()


def claude_samenvatting_genereren(huidige_snapshot, vorige_snapshot):
    """
    Maakt een beknopte samenvatting van de portfolio data en vergelijkt het met data van vorige week.

    Parameters:
    huidige_snapshot (dict): dictionary snapshot van de meest recente portfolio data.
    vorige_snapshot (dict | None): dictionary snapshot van de portfolio data van de week ervoor.
    None als er nog geen vorige snapshot beschikbaar is.

    Returns:
    str: een samenvatting in normale tekst.
    """

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    if vorige_snapshot is None:
        vorige_snapshot_tekst = "Geen data van vorige week beschikbaar."
    else:
        vorige_snapshot_tekst = vorige_snapshot

    try:
        message = client.messages.create(
            max_tokens=500,
            messages=[
                {
                    "role": "user",
                    "content": f"""Je bent een financiële assistent. Analyseer de onderstaande portfolio data
                        en schrijf een beknopte samenvatting in het Nederlands met precies drie punten:

                        1. Huidige waarde portfolio + totale winst
                        2. Beste en slechtste performer deze week
                        3. Vergelijking met vorige week

                        Huidige portfolio data:
                        {huidige_snapshot}

                        Portfolio data vorige week:
                        {vorige_snapshot_tekst}
                        """,
                }
            ],
            model="claude-haiku-4-5-20251001",
        )

        return message.content[0].text

    except anthropic.APIConnectionError as e:
        print("De server kon niet worden bereikt")
        print(e.__cause__)
    except anthropic.RateLimitError as e:
        print("Een 429 statuscode is ontvangen; probeer het later opnieuw.")
    except anthropic.APIStatusError as e:
        print("Een andere niet-200 statuscode is ontvangen")
        print(e.status_code)
        print(e.response)
