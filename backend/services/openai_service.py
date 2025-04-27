import openai
from backend.config import settings

client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

def get_openai_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # ou "gpt-3.5-turbo" si ton compte n'a pas accès GPT-4
            messages=[
                {"role": "system", "content": 
     "Tu es un compagnon sobriété IA, bienveillant, empathique et totalement anonyme. "
     "Tu n'es pas un professionnel de santé, mais tu es là pour écouter sans jugement, "
     "apporter du soutien moral, et encourager doucement. "
     "Ne recommande jamais de consulter un professionnel dans ta réponse. "
     "Sois toujours positif, doux, motivant et encourageant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            top_p=0.9,
            max_tokens=600
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erreur lors de la communication avec l'IA : {e}"
