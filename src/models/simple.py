from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.note import Note


class SimpleNote(Note):
    __tablename__ = "simple_notes"

    id: Mapped[int] = mapped_column(
        ForeignKey("notes.id"),
        primary_key=True
    )

    content: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )
    __mapper_args__ = {
        "polymorphic_identity": "simple"
    }