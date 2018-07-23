# Internal
from src.app import db


def insert(element: db.Model) -> int:
    """
    Insert a new element of type ``Model`` inside the db  and return the associated id.

    :param db.Model element:
    :return int:
    """
    assert isinstance(element, db.Model), "The element is to be inserted must be of type ``db.Model``."

    db.session.add(element)
    db.session.commit()
    return element.id


def update(element: db.Model) -> bool:
    """
    Commit an existent and updated element of type ``Model`` into the db.

    :param db.Model element:
    :return bool:
    """
    assert isinstance(element, db.Model), "The element is to updated must be of type ``db.Model``."

    db.session.commit()
    return True


def delete(element: db.Model):
    """
    Commit the deletion of an element of type ``Model`` into the db.

    :param db.Model element:
    :return bool:
    """
    assert isinstance(element, db.Model), "The element is to be deleted must be of type ``db.Model``."

    db.session.delete(element)
    db.session.commit()
