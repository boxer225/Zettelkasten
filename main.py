from typing import List
from fastapi import FastAPI

from db.repos.zettelkasten_repo import database, zettelkasten
from db.models import Note, NoteIn

app = FastAPI(
    title="Zettelkasten",
    description="Sample service",
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/zettelkasten/', response_model=List[Note])
async def read_all_notes():
    query = zettelkasten.select()
    return await database.fetch_all(query)


@app.post("/zettelkasten/", response_model=Note)
async def create_note(note: NoteIn):
    query = zettelkasten.insert().values(tag=note.tag, description=note.description, addiction_id=note.addiction_id)

    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}

@app.get('/zettelkasten/{note_id}')
async def read_note_by_id(note_id: int):
    query = zettelkasten.select().where(zettelkasten.c.id == note_id)
    return await database.fetch_all(query)

@app.get('/zettelkasten/tag/{tag}')
async def read_note_by_tag(tag: str):
    query = zettelkasten.select().where(zettelkasten.c.tag == tag)
    return await database.fetch_all(query)


@app.delete("/zettelkasten/delete/{note_id}")
async def delete_post_by_id(note_id: int):
    query = zettelkasten.delete().where(zettelkasten.c.id == note_id)
    await database.execute(query)
    return {"detail": "Note deleted", "status_code": 204}

@app.delete('/zettelkasten/delete/tag/{tag}')
async def delete_note_by_tag(tag: str):
    query = zettelkasten.delete().where(zettelkasten.c.tag == tag)
    await database.execute(query)
    return {"detail": "Note deleted", "status_code": 204}
