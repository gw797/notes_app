from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.note import Note


class ListNote(Note):
    __tablename__ = "list_notes"

    id: Mapped[int] = mapped_column(
        ForeignKey("notes.id"),
        primary_key=True
    )
    items: Mapped[list["ListItem"]] = relationship(
        back_populates="list_note"
    )

    __mapper_args__ = {
        "polymorphic_identity": "list"
    }