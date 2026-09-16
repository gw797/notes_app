from src.database.database import Base, engine
from src.models import Note, SimpleNote, BookmarkNote, ListNote, ListItem


Base.metadata.create_all(engine)

print("Tables created successfully!")