import google.generativeai as genai
import os


def generate_script():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel("gemini-1.5-flash")

    with open("prompts/luxury_prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()

    response = model.generate_content(prompt)

    script = response.text.strip()

    with open("temp/script.txt", "w", encoding="utf-8") as f:
        f.write(script)

    return script
