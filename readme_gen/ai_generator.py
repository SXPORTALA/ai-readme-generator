from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def gerar_readme_ia(arquivos):

    estrutura = "\n".join(arquivos)

    prompt = f"""
    Gere SOMENTE um README.md em markdown.

    Estrutura do projeto:
    {estrutura}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text