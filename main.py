import os
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import google.generativeai as genai

app = FastAPI()

templates = Jinja2Templates(directory="templates")

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# تم التحديث إلى النموذج المدعوم الحالي
model = genai.GenerativeModel("gemini-2.5-flash")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request, "result": ""})

@app.post("/process", response_class=HTMLResponse)
async def process_text(request: Request, text: str = Form(...), action: str = Form(...)):
    prompts = {
        "fix": "قم بتصحيح الأخطاء الإملائية والنحوية وتنسيق النص التالي بدقة:",
        "summarize": "قم بتلخيص النص التالي بوضوح واختصار:",
        "rewrite": "قم بإعادة صياغة النص التالي بأسلوب احترافي وبليغ:"
    }
    
    selected_prompt = prompts.get(action, "قم بتحسين النص وإعادة صياغته:")
    final_prompt = f"{selected_prompt}\n\n{text}"

    try:
        response = model.generate_content(final_prompt)
        result = response.text
    except Exception as e:
        result = f"حدث خطأ أثناء المعالجة: {str(e)}"

    return templates.TemplateResponse(request, "index.html", {"request": request, "result": result, "original_text": text})
