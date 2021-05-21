from fastapi import APIRouter, File, UploadFile, Response, status, Body
from pydantic import BaseModel

from ..app_db import files_db, entries_db
from ..utils import filesystem


class CustomResponse(BaseModel):
    file_name: str
    file_size: int
    md5: str
    sha1: str


router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def upload(
        uploaded_file: UploadFile = File(default="apk"),
        response: Response = Response()):
    if uploaded_file.filename.endswith(".apk"):
        md5, sha1, size = await filesystem.eval_file_hash(uploaded_file)

        if len(files_db.read(sha1=sha1)) == 0:
            await filesystem.upload(uploaded_file, f"upload_dir/{sha1}.apk")

            files_db.create(sha1, size)

            response.status_code = status.HTTP_200_OK
            return CustomResponse(
                file_name=uploaded_file.filename,
                file_size=size,
                md5=md5,
                sha1=sha1
            )
        else:
            response.status_code = status.HTTP_406_NOT_ACCEPTABLE
            return {"reason": "apk already Present"}
    else:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"reason": "Only apk file allowed"}
