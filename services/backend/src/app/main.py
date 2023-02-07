from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from .models import ScanRequest, ScanResponse
from .yara_scanner import YaraScanner, default_scanner


logger = logging.getLogger(__name__)

app = FastAPI()



# Add CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routes
@app.get("/")
def home():
    return "OpenAssistant Yara malware scanner"

@app.get("/ping")
async def ping():
    return {"ping": "pong!"}

@app.post("/scan")
async def scan(scan_request: ScanRequest):
    yara_scanner = default_scanner
    result = yara_scanner.scan_string(scan_request.data)
    print(result)
    return ScanResponse(
        result=result,
        scan_type=scan_request.scan_type,
        data=scan_request.data,
    )

