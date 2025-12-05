from fastapi import FastAPI, Depends, HTTPException
from fastapi import UploadFile, File as UploadFileField
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import shutil
import os
from typing import List


from . import database, models, crud, ai, schemas
from .models import File

STORAGE_DIR = os.getenv("STORAGE_DIR", "./storage")
os.makedirs(STORAGE_DIR, exist_ok=True)


app = FastAPI(title="Mini Document Store")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=database.engine)

@app.post("/files/upload", response_model=schemas.FileOut)
async def upload_file(
    file: UploadFile = UploadFileField(...),
    db: Session = Depends(get_db)
):
    original_name = file.filename
    local_path = os.path.join(STORAGE_DIR, f"{int(os.times()[4])}_{original_name}")

    with open(local_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    size = os.path.getsize(local_path)
    file_record = crud.create_file_record(db=db, original_name=original_name, path=local_path, size=size, uploaded_by=1)
    return file_record

@app.get("/files", response_model=List[schemas.FileOut])
def list_files(db: Session = Depends(get_db)):
    files = crud.list_files(db)
    return files




@app.post("/files/{file_id}/analyze")
def analyze_file(file_id: int, db: Session = Depends(get_db)):
    file = crud.get_file(db, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    payload = {
    "file_name": file.original_name,
    "file_size": int(file.size or 0),
    "version": int(file.version),
    "uploaded_at": str(file.uploaded_at),
    }

    comment = ai.fake_ai_analyze(payload)
    analysis = crud.create_analysis(db=db, file_id=file.id, payload=payload, comment=comment)

    return {"analysis_id": analysis.id, "comment": comment}

@app.get("/files/{file_id}/analysis")
def get_analysis(file_id: int, db: Session = Depends(get_db)):
    file = crud.get_file(db, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")


    analyses = crud.get_analysis_for_file(db, file_id)
    out = []
    for a in analyses:
        out.append({
        "id": a.id,
        "file_id": a.file_id,
        "analyzed_at": a.analyzed_at,
        "payload": a.payload,
        "comment": a.comment,
        })
    return out