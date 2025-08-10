from datetime import datetime

from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class Scan(Base):
    __tablename__ = "scans"
    id = Column(Integer, primary_key=True)
    module = Column(String)
    target = Column(String)
    args_json = Column(JSON)
    status = Column(String, default="queued")
    created_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime)
    returncode = Column(Integer)
    stdout_path = Column(String)
    stderr_path = Column(String)
    profile = Column(String)
    result = relationship("ScanResult", back_populates="scan", uselist=False)

class ScanResult(Base):
    __tablename__ = "scan_results"
    scan_id = Column(Integer, ForeignKey("scans.id"), primary_key=True)
    result_json = Column(JSON)
    scan = relationship("Scan", back_populates="result")

class Snapshot(Base):
    __tablename__ = "snapshots"
    target_key = Column(String, primary_key=True)
    last_snapshot_json = Column(JSON)
    history_json = Column(JSON)
