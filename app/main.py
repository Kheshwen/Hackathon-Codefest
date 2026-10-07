from fastapi import FastAPI
from app.models import CheckRequest, CheckResponse

app = FastAPI(title="SemakDulu")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/check", response_model=CheckResponse)
def check(req: CheckRequest):
    return CheckResponse(
        verdict="unsure",
        reason="Placeholder",
        action="Placeholder",
    )