from fastapi import FastAPI
from scrape import SIS

app = FastAPI()

@app.get("/sis")
def api(usn: str, dd: str, mm: str, yyyy: str):
    sis = SIS()
    password = f"{dd.zfill(2)}-{mm.zfill(2)}-{yyyy}"
    return sis.scrape(usn, password)
