import os
import socket
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="SWE40006 Distinction Web App")

# Read environment variables with fallback safety defaults
APP_ENV = os.getenv("APP_ENVIRONMENT", "Production")
DEVELOPER_NAME = os.getenv("DEVELOPER_NAME", "Josh Bakanursky")
STUDENT_ID = os.getenv("STUDENT_ID", "102551610")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    hostname = socket.gethostname()
    try:
        container_ip = socket.gethostbyname(hostname)
    except Exception:
        container_ip = "Unknown"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Distinction Task Deployment</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #f4f6f9; color: #333; }}
            .card {{ background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }}
            h1 {{ color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }}
            .metric {{ margin: 15px 0; font-size: 1.1em; }}
            .label {{ font-weight: bold; color: #4b5563; }}
            .badge {{ background-color: #10b981; color: white; padding: 4px 8px; border-radius: 6px; font-size: 0.9em; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Task 4.3 Distinction Deployment</h1>
            <div class="metric"><span class="label">Developer:</span> {DEVELOPER_NAME}</div>
            <div class="metric"><span class="label">Student ID:</span> {STUDENT_ID}</div>
            <div class="metric"><span class="label">Environment:</span> <span class="badge">{APP_ENV}</span></div>
            <div class="metric"><span class="label">Container Hostname:</span> <code>{hostname}</code></div>
            <div class="metric"><span class="label">Internal Container IP:</span> <code>{container_ip}</code></div>
        </div>
    </body>
    </html>
    """
    return html_content
