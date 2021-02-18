import os
import hashlib

from fastapi import APIRouter, File, UploadFile

from ..func import disas

router = APIRouter()


BUF_SIZE = 65536  # lets read stuff in 64kb chunks!


DESTINATION = "upload_dir"
CHUNK_SIZE = 2 ** 20  # 1MB

@router.get("/")
async def run():
    disas.disas('')
    disas.reassemble('')
    disas.sign('')
    return 'job done'


@router.post("/")
async def upload(file: UploadFile = File(default='png')):
    print(file.file)
    try:
        os.mkdir("upload_dir")
        print(os.path)
    except Exception as e:
        print(e)
    file_name = os.getcwd() + "/upload_dir/" + file.filename.replace(" ", "-")
    with open(file_name, 'wb+') as f:
        f.write(file.file.read())
        f.close()

    # TODO eval md5 and sha1
    return {
        "file_name": file.filename,
        "file_size": file.__sizeof__(),
        # "md5": md5(file.file),
        # "sha1":  h.hexdigest()
    }
