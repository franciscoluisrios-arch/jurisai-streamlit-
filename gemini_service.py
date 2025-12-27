import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiService:

    def generate_analysis(self, context: dict) -> str:
        model = genai.GenerativeModel("gemini-1.5-pro")
        prompt = f"""
        Analise juridicamente o caso abaixo:

        {context}
        """
        response = model.generate_content(prompt)
        return response.text

    def generate_draft(self, context: dict, diagnosis: str) -> str:
        model = genai.GenerativeModel("gemini-1.5-pro")
        prompt = f"""
        Com base no contexto e diagnóstico abaixo, elabore a minuta:

        CONTEXTO:
        {context}

        DIAGNÓSTICO:
        {diagnosis}
        """
        response = model.generate_content(prompt)
        return response.text
