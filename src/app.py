# Standard
import os

# Vendor
from flask import Flask
from flask_graphql import GraphQLView

# Internal
from src import config
from src.database import Database

app = Flask(__name__)

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_PATH

db = Database.get_instance(app)

# Import here the schema to avoid circular import(s)
from src.schema import schema


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=False if os.environ["FLASK_ENV"].lower() != "development" else True,
    )
)

# After the models are defined, create all the tables associated
db.create_all()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
