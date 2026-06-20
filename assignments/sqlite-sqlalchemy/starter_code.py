"""Starter code demonstrating SQLite + SQLAlchemy CRUD operations.

Creates a local SQLite file `sqlite_sqlalchemy.db` in the same folder and
demonstrates basic CRUD functions.
"""

from pathlib import Path
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, Session

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "sqlite_sqlalchemy.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"  # relative file path

Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(250), nullable=True)


def get_engine(echo: bool = False):
    return create_engine(DATABASE_URL, echo=echo, future=True)


def init_db(engine):
    Base.metadata.create_all(engine)


def create_item(session: Session, name: str, description: str | None = None) -> Item:
    item = Item(name=name, description=description)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def get_item(session: Session, item_id: int) -> Item | None:
    return session.get(Item, item_id)


def list_items(session: Session):
    return session.query(Item).order_by(Item.id).all()


def update_item(session: Session, item_id: int, **kwargs):
    item = session.get(Item, item_id)
    if not item:
        return None
    for k, v in kwargs.items():
        if hasattr(item, k):
            setattr(item, k, v)
    session.commit()
    session.refresh(item)
    return item


def delete_item(session: Session, item_id: int) -> bool:
    item = session.get(Item, item_id)
    if not item:
        return False
    session.delete(item)
    session.commit()
    return True


def demo():
    engine = get_engine()
    init_db(engine)
    with Session(engine) as session:
        print('Creating items...')
        a = create_item(session, 'Notebook', 'A ruled notebook')
        b = create_item(session, 'Pen', 'Blue ink pen')

        print('Listing items:')
        for it in list_items(session):
            print(f'  {it.id}: {it.name} — {it.description}')

        print('Updating item 1...')
        update_item(session, a.id, description='A lined notebook (200 pages)')

        print('Get item 1:')
        item = get_item(session, a.id)
        print(f'  {item.id}: {item.name} — {item.description}')

        print('Deleting item 2...')
        delete_item(session, b.id)

        print('Final items:')
        for it in list_items(session):
            print(f'  {it.id}: {it.name} — {it.description}')


if __name__ == '__main__':
    demo()
