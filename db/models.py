from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from db.database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String, index=True)
    tool_name = Column(String)
    payload = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)
