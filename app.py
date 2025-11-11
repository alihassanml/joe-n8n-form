from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit")
async def submit_form(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    campaign: str = Form(...),
    mainUrl: str = Form(...),
    briefInfo: str = Form(...),
    channel: str = Form(""),
    size: str = Form(""),
    type: str = Form(""),
    campaignPeriod: str = Form(""),
    estimatedVolume: str = Form("")
):
    # Collect data
    data = {
        "name": name,
        "email": email,
        "campaign": campaign,
        "mainUrl": mainUrl,
        "briefInfo": briefInfo,
        "channel": channel,
        "size": size,
        "type": type,
        "campaignPeriod": campaignPeriod,
        "estimatedVolume": estimatedVolume,
    }

    # Here you can:
    # 1. Save to database
    # 2. Forward to n8n / webhook
    # 3. Send email

    print("Form submitted:", data)

    return JSONResponse({"message": "🎉 Form submitted successfully!", "data": data})
