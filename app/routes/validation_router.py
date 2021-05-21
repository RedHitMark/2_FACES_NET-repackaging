from fastapi import APIRouter, Path

from ..func import validate

router = APIRouter()


@router.post("/send-virustotal/{sha1_hash}")
async def send_to_virus_total(sha1_hash: str = Path(default="", title="SHA-1 of the file")):
    return validate.submit_to_virustotal(sha1_hash=sha1_hash)


@router.post("/force-virustotal/{sha1_hash}")
async def force_scan(sha1_hash: str = Path(default="", title="SHA-1 of the file")):
    return validate.froce_virustotal(sha1_hash=sha1_hash)


@router.get("/report/{sha1_hash}")
async def get_virus_total_report(sha1_hash: str = Path(default="", title="SHA-1 of the file")):
    return validate.get_virustotal_report(sha1_hash)
