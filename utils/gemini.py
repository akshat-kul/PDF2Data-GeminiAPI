import google.generativeai as genai
from papers.schemas import SamplePaper
from utils.gemini_prompt import gemini_prompt
from config.settings import settings

gemini_api_key = settings.gemini_api_key
gemini_client = genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Example function to extract data from a PDF using Gemini API 1.5
async def extract_from_pdf(file_path: str) -> SamplePaper:
    model = genai.GenerativeModel("gemini-1.5-flash")
    sample_pdf = genai.upload_file(file_path)
    response = model.generate_content([gemini_prompt, sample_pdf])
    return response.text

def extract_from_text(text: str) -> SamplePaper:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([gemini_prompt, text])
    return response.text