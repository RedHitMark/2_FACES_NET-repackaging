from fastapi import APIRouter
from ..app_db import files_db, entries_db
from ..func import disas
router = APIRouter()


@router.get("/")
async def hack(entry_id: int):
    entries = entries_db.read_by_id(entry_id)
    if len(entries) == 1:
        entry = entries[0]

        original_file_hash = entry['original_file']
        disas.disas(original_file_hash)

        disas.add_pezzotto(original_file_hash)

        disas.reassemble(original_file_hash)
        new_file_hash_md5, new_file_hash_sha1, new_filesize = disas.sign(original_file_hash)

        files_db.create(new_file_hash_sha1, new_filesize)
        entries_db.update_by_id(entry_id, new_file_hash_sha1)
        return 'done'
    else:
        return 'alive'