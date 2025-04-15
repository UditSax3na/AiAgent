from openai import OpenAI
from config.env import API_KEY
from config.constants import OPENROUTER_MODEL, OPENROUTER_URL

def Ask_AI(text):
    client = OpenAI(
        base_url=OPENROUTER_URL,
        api_key=API_KEY
    )
    if text != "":
        Ntext = text+" and create plan, code, and how to run in respective sequence sections don't number the heading only write plan, code and how to run cannot be in bold and in numbers"
        completion = client.chat.completions.create(
            extra_body={},
            model=OPENROUTER_MODEL,
            messages=[
                {
                "role": "user",
                "content": [
                        {
                        "type": "text",
                        "text": Ntext
                        }
                    ]
                }
            ]
        )
        return True, completion.choices[0].message.content
    else:
        return False, "Give me some task to work on!"


