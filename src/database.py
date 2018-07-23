# Vendor
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Database():
    """ Database singleton. """
    __instance = None # type: SQLAlchemy

    @classmethod
    def get_instance(cls, app: Flask = None):
        assert app is None or isinstance(app, Flask), "The type of app must be the Flask class."
        if cls.__instance is None:
            if app is None:
                raise Exception("The app variable during the instantiation must not be None.")
            cls.__instance = SQLAlchemy(app)
        return cls.__instance
