# Vendor
from graphene import Mutation, Int, String, InputObjectType, Field

# Internal
from src.types.department import Department
from src.controllers.department import create_department, update_department, delete_department


class DepartmentCreateInput(InputObjectType):
    name = String(required=True)
    location = String(required=True)


class DepartmentUpdateInput(InputObjectType):
    id = Int(required=True)
    name = String()
    location = String()


class CreateDepartment(Mutation):
    """ CreateDepartment mutation. """
    class Arguments:
        """ Arguments of the mutation query. """
        data = DepartmentCreateInput(required=True)

    # Return type(s) of this mutations
    id = Int()

    def mutate(self, info, department_data: DepartmentCreateInput = None) -> Mutation:
        id = create_department(
            name=department_data.name,
            location=department_data.location,
        )
        return CreateDepartment(id)


class UpdateDepartment(Mutation):
    """ UpdateDepartment mutation. """
    class Arguments:
        """ Arguments of the mutation query. """
        id = Int(required=True)
        data = DepartmentUpdateInput(required=True)

    department = Field(Department)

    def mutate(self, info, id: int, data: DepartmentUpdateInput = None) -> Mutation:
        department = update_department(
            id,
            name=data.name,
            location=data.location,
        )

        return UpdateDepartment(department)


class DeleteDepartment(Mutation):
    """ Delete department mutation. """
    class Arguments:
        """ Arguments of the mutation query. """
        id = Int(required=True)

    # Return field(s) of the query
    department = Field(Department)

    def mutate(self, info, id: int):
        department = delete_department(id)

        return DeleteDepartment(department)
