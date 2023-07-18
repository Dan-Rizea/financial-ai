import os

# SQLite database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
database_name = 'your_database_name.db'
database_path = os.path.join(basedir, database_name)

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + database_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False