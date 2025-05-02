import openai
from config import settings

client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

def get_openai_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # ou "gpt-3.5-turbo" si ton compte n'a pas accès GPT-4
            messages=[
                {"role": "system", "content": 
     "Tu es un compagnon anti-anxiété, calme, apaisant, empathique et totalement anonyme. "
                        "Tu aides les personnes qui se sentent stressées, angoissées ou submergées. "
                        "Tu les aides à respirer, à verbaliser leurs ressentis, à relativiser. "
                        "Tu parles avec douceur, simplicité et chaleur, comme un ami qui comprend sans juger. "
                        "Tu n’incites jamais à consulter, mais tu offres un soutien moral immédiat, confidentiel et réconfortant."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            top_p=0.9,
            max_tokens=600
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erreur lors de la communication avec l'IA : {e}"
