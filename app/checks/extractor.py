import re

PHONE_RE = re.compile(r'(?<!\d)(?:\+?60|0)1\d[\s-]?\d{3,4}[\s-]?\d{4}(?!\d)')
URL_RE = re.compile(
    r'(?:https?://|www\.)[^\s]+|\b(?:bit\.ly|tinyurl\.com|s\.id|t\.ly)/[^\s]+',
    re.I,
)
ACCOUNT_RE = re.compile(r'(?<!\d)\d(?:[\s-]?\d){8,15}(?!\d)')

def normalize_phone(raw: str) -> str:
    digits = re.sub(r'\D', '', raw)
    if digits.startswith('60'):
        digits = digits[2:]
    elif digits.startswith('0'):
        digits = digits[1:]
    return '+60' + digits

def _dedupe(items):
    return list(dict.fromkeys(items))

def extract(text: str) -> dict:
    urls = [u.rstrip('.,;)') for u in URL_RE.findall(text)]
    rest = URL_RE.sub(' ', text)

    phones = [normalize_phone(p) for p in PHONE_RE.findall(rest)]
    rest = PHONE_RE.sub(' ', rest)   # remove phones so they aren't read as accounts

    accounts = [re.sub(r'\D', '', a) for a in ACCOUNT_RE.findall(rest)]
    accounts = [a for a in accounts if 9 <= len(a) <= 16]

    return {
        "urls": _dedupe(urls),
        "phones": _dedupe(phones),
        "accounts": _dedupe(accounts),
    }