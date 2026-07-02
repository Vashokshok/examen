from table.models import Category, Base
from table.database import session, engine

Base.metadata.create_all(engine)

def test_add_dealer():
    deaker = Category(name='Khava')
    session.add(deaker)
    session.commit()

    saved = session.query(Category).filter_by(name='Khava').first()
    assert saved is not None

