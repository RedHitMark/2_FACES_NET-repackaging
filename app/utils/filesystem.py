import os
import shutil
import hashlib


BUF_SIZE = 65536


def clean_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path, ignore_errors=True)

    os.makedirs(folder_path)


def rename(filepath):
    return


async def upload(file, path_to):
    with open(path_to, 'wb') as f:
        await file.seek(0)
        while True:
            data = await file.read(BUF_SIZE)
            if not data:
                break
            f.write(data)

        f.close()

async def eval_file_hash(file):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    size = 0

    await file.seek(0)
    while True:
        data = await file.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)
        size += len(data)

    return md5.hexdigest(), sha1.hexdigest(), size


# async def eval_file_size(file):
#     size = 0
#     await file.seek(os.SEEK_END)
#     size = f.tell()
#
#     return size
