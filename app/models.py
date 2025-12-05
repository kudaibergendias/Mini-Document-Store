from sqlalchemy import Column, Integer, String, DateTime, BigInteger, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base


class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    original_name = Column(String, index=True)
    version = Column(Integer, default=1)
    path = Column(String)
    size = Column(BigInteger)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    uploaded_by = Column(Integer, default=1)


    analyses = relationship("Analysis", back_populates="file")


class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey("files.id", ondelete="CASCADE"))
    analyzed_at = Column(DateTime(timezone=True), server_default=func.now())
    payload = Column(Text)
    comment = Column(Text)


    file = relationship("File", back_populates="analyses")