from pydantic import BaseModel

class Finding(BaseModel):
    check: str          # "mule_db", "keywords", "urls"
    level: str          # "safe" | "caution" | "danger"
    reason: str

class CheckRequest(BaseModel):
    text: str

class CheckResponse(BaseModel):
    verdict: str        # safe | caution | danger | unsure
    reason: str
    action: str
    findings: list[Finding] = []