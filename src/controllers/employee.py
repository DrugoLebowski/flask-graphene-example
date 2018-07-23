# Internal
from src.models.employee import Employee
from src.utils.db import insert, update, delete


def create_employee(**kwargs) -> int:
    """
    Handle the creation of a new employee.

    :param kwargs:
    :return:
    """
    return insert(
        Employee(
            name=kwargs.get("name"),
            surname=kwargs.get("surname"),
            department_id=kwargs.get("department_id")
        )
    )


def update_employee(id: int, **kwargs) -> bool:
    """
    Handle the update of a record in the db.

    :param int id:
    :param kwargs:
    :return:
    """
    assert isinstance(id, int), "The parameter ``id`` must be an integer."
    assert id > 0, "The parameter ``id`` must be greater or equal respect to ``0``"

    employee = Employee.query.get(id)

    # Avoid an unnecessary update
    if len(kwargs.items()) == 0:
        return employee

    name = kwargs.get('name')
    if name is not None:
        employee.name = name

    surname = kwargs.get('surname')
    if surname is not None:
        employee.surname = surname

    update(employee)
    return employee


def delete_employee(id: int):
    """
    Handle the deletion of an employee
    :param id:
    :return:
    """
    assert isinstance(id, int), "The parameter ``id`` must be an integer."
    assert id > 0, "The parameter ``id`` must be greater or equal respect to ``0``"

    employee = Employee.query.get(id)
    delete(employee)
    return employee
