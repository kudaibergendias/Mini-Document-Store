from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class FileOut(BaseModel):
    id: int
    original_name: str
    version: int
    uploaded_at: datetime
    size: int


    model_config = ConfigDict(from_attributes=True)


class AnalysisOut(BaseModel):
    id: int
    file_id: int
    analyzed_at: datetime
    payload: dict
    comment: str


    model_config = ConfigDict(from_attributes=True)