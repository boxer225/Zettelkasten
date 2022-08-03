import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./zettelkasten.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

zettelkasten = sqlalchemy.Table(
    "zettelkasten",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER, primary_key=True),
    sqlalchemy.Column("tag", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("addiction_id", sqlalchemy.INTEGER),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
