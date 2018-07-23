# Vendor
from graphene import Mutation, InputObjectType, String, Int, Field

# Internal
from src.types.employee import Employee
from src.controllers.employee import create_employee, update_employee, delete_employee


class CreateEmployeeInput(InputObjectType):
    name = String(required=True)
    surname = String(required=True)
    department_id = Int(required=True)


class UpdateEmployeeInput(InputObjectType):
    name = String()
    surname = String()


class CreateEmployee(Mutation):
    """ Create employee mutation. """
    class Arguments:
        """ Arguments of the mutation query. """
        data = CreateEmployeeInput(required=True)

    # Return type(s) of this mutation
    id = Int()

    def mutate(self, info, employee_data: CreateEmployeeInput = None) -> Mutation:
        id = create_employee(
            name=employee_data.name,
            surname=employee_data.surname,
            department_id=employee_data.department_id
        )
        return CreateEmployee(id)


class UpdateEmployee(Mutation):
    """ Update employee mutation. """
    class Arguments:
        id = Int(required=True)
        data = UpdateEmployeeInput(required=True)

    # Return field(s) of the query
    employee = Field(Employee)

    def mutate(self, info, id: int, data: UpdateEmployeeInput = None) -> Mutation:
        u_employee = update_employee(
            id,
            name=data.name,
            surname=data.surname,
        )

        return UpdateEmployee(u_employee)


class DeleteEmployee(Mutation):
    """ Delete employee mutation. """
    class Arguments:
        id = Int(required=True)

    employee = Field(Employee)

    def mutate(self, info, id) -> Mutation:
        employee = delete_employee(id)

        return DeleteEmployee(employee)
