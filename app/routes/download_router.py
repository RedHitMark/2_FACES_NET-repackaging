import os

from fastapi import APIRouter, Path
from fastapi.responses import FileResponse


router = APIRouter()


@router.get("/{sha1_hash}")
async def download(
        sha1_hash: str = Path(title="Sha1 of the file you want to download", default="")
    ):
    file_name = f"{sha1_hash}.apk"

    file_path = os.getcwd() + "/upload_dir/" + file_name
    return FileResponse(path=file_path, media_type='application/octet-stream', filename=file_name)
