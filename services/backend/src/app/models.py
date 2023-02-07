from pydantic import BaseModel
from typing import List, Optional



class ScanRequest(BaseModel):
    data: str
    scan_type: Optional[str] = "string"


class ScanResponse(BaseModel):
    result: List[str]
    scan_type: Optional[str] = "string"
    data: Optional[str] = None