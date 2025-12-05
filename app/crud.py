import json
from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models




def create_file_record(db: Session, original_name: str, path: str, size: int, uploaded_by: int = 1):
    current = db.query(func.max(models.File.version)).filter(models.File.original_name == original_name).scalar()
    next_version = (current or 0) + 1
    file = models.File(original_name=original_name,version=next_version,path=path,size=size,uploaded_by=uploaded_by,)
    db.add(file)
    db.commit()
    db.refresh(file)
    return file




def list_files(db: Session):
    return db.query(models.File).order_by(models.File.original_name, models.File.version.desc()).all()




def get_file(db: Session, file_id: int):
    return db.query(models.File).filter(models.File.id == file_id).first()




def create_analysis(db: Session, file_id: int, payload: dict, comment: str):
    a = models.Analysis(file_id=file_id, payload=json.dumps(payload), comment=comment)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a




def get_analysis_for_file(db: Session, file_id: int):
    return db.query(models.Analysis).filter(models.Analysis.file_id == file_id).order_by(models.Analysis.analyzed_at.desc()).all()