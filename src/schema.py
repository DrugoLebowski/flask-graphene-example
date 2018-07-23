#  Vendor
from graphene import Schema

# Internal
from src.query import Query
from src.mutation import Mutations

schema = Schema(
    query=Query,
    mutation=Mutations,
)
