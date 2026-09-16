from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.note import Note


class BookmarkNote(Note):
    __tablename__ = "bookmark_notes"

    id: Mapped[int] = mapped_column(
        ForeignKey("notes.id"),
        primary_key=True
    )

    url: Mapped[str] = mapped_column(
        String(2048),
        nullable=False
    )

    __mapper_args__ = {
        "polymorphic_identity": "bookmark"
    }