import click
from src.app import service
from src.utils.note_logger import logger


@click.group()
def cli():
    pass


@cli.group()
def add():
    pass


@click.command()
@click.option("--type", required=True)
@click.option("--title", required=True)
@click.option("--content")
@click.option("--url")
@click.option("--items", multiple=True)
def create(type, title, content, url, items):
    ...

@cli.command()
def show():
    try:
        all_notes = service.get_all_notes()
        for note in all_notes:
            logger.info(note)
    except Exception as e:
        logger.error(e)


@cli.command()
@click.argument("note_id", type=int)
def show_note(note_id):
    try:
        note = service.get_note_by_id(note_id)
        if note is None:
            logger.info(f"Note with id {note_id} was not found.")
            return
        click.echo(note)
    except Exception as e:
        logger.error(e)


@cli.command()
@click.argument("note_id", type=int)
def delete(note_id):
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
def update(note_id, title, content, url, items):
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
