from table.models import Category, Base, Note
from table.database import session, engine

Base.metadata.create_all(engine)

def test_add_cotegor():
    deaker = Category(name='Khava')
    session.add(deaker)
    session.commit()

    saved = session.query(Category).filter_by(name='Khava').first()
    assert saved is not None
def test_add_note():
    note = Note(title='NKnlk', content='na')
    session.add(note)
    session.commit()

    saved = session.query(Category).filter_by(title='NKnlk').first()
    assert saved is not None
