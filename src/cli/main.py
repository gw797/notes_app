import click

from app import service
from models.base_note import BaseNote
from utils.note_logger import logger


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option("--type", required=True)
@click.option("--title", required=True)
@click.option("--content", required=True)
def create(type: str, title: str, content: str) -> None:
    try:
        note = service.create(type, title, content)

        if note is not None:
            logger.info(f"Note {note.id} created successfully!")

    except Exception as e:
        logger.error(e)


@cli.command()
def show() -> None:
    try:
        all_notes = service.get_all_notes()

        for note in all_notes:
            logger.info(note)

    except Exception as e:
        logger.error(e)


@cli.command()
@click.argument("note_id", type=int)
def show_note(note_id: int) -> None:
    try:
        note = service.get_note_by_id(note_id)

        if note is None:
            logger.info(f"Note with id {note_id} was not found.")
            return

        click.echo(BaseNote.__str__(note))

    except Exception as e:
        logger.error(e)


@cli.command()
@click.argument("note_id", type=int)
def delete(note_id: int) -> None:
    try:
        deleted_note = service.delete_note(note_id)

        if deleted_note:
            logger.info(f"Note {note_id} deleted successfully!")
        else:
            logger.warning(f"Note {note_id} was not found.")

    except Exception as e:
        logger.error(e)


@cli.command()
@click.argument("note_id", type=int)
@click.option("--title")
@click.option("--content")
@click.option("--url")
@click.option("--items", multiple=True)
def update(
        note_id: int,
        title: str | None,
        content: str | None,
        url: str | None,
        items: tuple[str, ...]
) -> None:
    try:
        note = service.update_note(
            note_id,
            title=title,
            content=content,
            url=url,
            notes_list=list(items)
        )

        if note:
            logger.info(f"Note {note_id} updated successfully!")
        else:
            logger.warning(f"Note {note_id} not found.")

    except Exception as e:
        logger.error(e)