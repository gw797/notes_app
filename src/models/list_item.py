from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base


class ListItem(Base):
    __tablename__ = "list_items"

    id: Mapped[int] = mapped_column(primary_key=True)

    list_note_id: Mapped[int] = mapped_column(
        ForeignKey("list_notes.id"),
        nullable=False
    )

    item: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    list_note: Mapped["ListNote"] = relationship(
        back_populates="items"
    )