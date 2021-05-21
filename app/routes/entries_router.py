from fastapi import APIRouter, status
from typing import List, Optional
from pydantic import BaseModel
from ..app_db import entries_db
router = APIRouter()


class Entry(BaseModel):
    id: int
    title: str
    description: str
    original_file: str
    hacked_file: Optional[str] = None


class CreationEntry(BaseModel):
    title: str
    description: str
    sha1: str


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Entry], response_model_exclude_unset=True)
async def get_all_entries():
    entries_a = entries_db.read_all()
    print(entries_a)
    return entries_a


@router.post("/", status_code=status.HTTP_200_OK)
async def create_new_entry(creation_entry: CreationEntry):
    entries_db.create(creation_entry.title, creation_entry.description, creation_entry.sha1)

    return "gg"