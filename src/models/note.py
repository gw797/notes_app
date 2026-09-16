from sqlalchemy import String,DateTime, func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from src.database.database import Base

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False)
    note_type: Mapped[str] = mapped_column(
        "type",
        String(50),
        nullable=False
    )
    __mapper_args__ = {
        "polymorphic_on": note_type,
        "polymorphic_identity": "note"
    }