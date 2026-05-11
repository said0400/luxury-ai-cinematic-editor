import google.generativeai as genai
import os
import logging

def generate_script():
    # 1. التحقق من مفتاح API
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logging.error("GEMINI_API_KEY is missing from environment variables.")
        return None

    genai.configure(api_key=api_key)

    # 2. إعداد الموديل مع System Instruction لضمان النبرة المطلوبة (Luxury/Psychological)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={
            "temperature": 0.75, # توازن بين الإبداع والمنطق
            "top_p": 0.9,
            "max_output_tokens": 200,
        }
    )

    try:
        # 3. قراءة البرومبت بأمان
        prompt_path = "prompts/luxury_prompt.txt"
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"Prompt file not found at {prompt_path}")

        with open(prompt_path, "r", encoding="utf-8") as f:
            base_prompt = f.read()

        # 4. توليد المحتوى
        response = model.generate_content(base_prompt)
        
        if not response.text:
            raise ValueError("Gemini returned an empty response.")

        script = response.text.strip()

        # 5. حفظ النتيجة (إنشاء مجلد temp إذا لم يكن موجوداً)
        os.makedirs("temp", exist_ok=True)
        with open("temp/script.txt", "w", encoding="utf-8") as f:
            f.write(script)

        return script

    except Exception as e:
        logging.error(f"Error in generate_script: {str(e)}")
        return None
