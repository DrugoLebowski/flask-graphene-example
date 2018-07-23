# Internal
from src.models.department import Department
from src.utils.db import insert, update, delete


def create_department(**kwargs) -> int:
    """
    Create a new department and return its ID of database.

    :param kwargs:
    :return int:
    """
    return insert(
        Department(
            name=kwargs.get('name'),
            location=kwargs.get('location'),
        )
    )


def update_department(id: int, **kwargs):
    """
    Update an existent department, associated to the ``id`` param.

    :param int id:
    :param kwargs:
    :return:
    """
    assert isinstance(id, int), 'The parameter ``id`` must be an integer.'
    assert id > 0, 'The parameter ``id`` must be greater or equal respect to ``0``'

    department = Department.query.get(id)

    # Avoid an unnecessary update
    if len(kwargs.items()) == 0:
        return department

    name = kwargs.get('name')
    if name is not None:
        department.name = name

    location = kwargs.get('location')
    if location is not None:
        department.location = location

    update(department)
    return department


def delete_department(id: int) -> bool:
    """
    Delete the department associated to the id.

    :param int id:
    :return bool:
    """
    assert isinstance(id, int), 'The parameter ``id`` must be an integer.'
    assert id > 0, 'The parameter ``id`` must be greater or equal respect to ``0``'

    department = Department.query.get(id)
    delete(department)
    return department
