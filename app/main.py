from fastapi import FastAPI
from app.models import CheckRequest, CheckResponse
from app.checks.extractor import extract
from app.checks import mule_db

app = FastAPI(title="HomelessPeople") //change the title later

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/check", response_model=CheckResponse)
def check(req: CheckRequest):
    extracted = extract(req.text)
    findings = mule_db.lookup(extracted)
    if findings:
        return CheckResponse(
            verdict="danger",
            reason=findings[0].reason,
            action="Do not send money. Call NSRC 997 if you already paid.",
            findings=findings,
        )
    return CheckResponse(verdict="unsure", reason="Nothing found yet.",
                         action="Be careful and ask someone you trust.")