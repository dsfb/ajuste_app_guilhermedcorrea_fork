import urllib
import pyodbc
import os
from urllib.parse import quote_plus
from urllib import parse
from dotenv import load_dotenv
from os import path


load_dotenv()
server = os.getenv('Server')
database = os.getenv('Database')
usuario = os.getenv('UID')
password = os.getenv('PWD')
basedir = path.abspath(path.dirname(__file__))


databaseuri = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                                 f"SERVER={server};"
                                 f"DATABASE={database};"
                                 f"UID={usuario};"
                                 f"PWD={password}")


uploads = r'/home/debian/Documentos/TESTES/dockerapp/uploads'

SQLALCHEMY_DATABASE_URI= ("mssql+pyodbc:///?odbc_connect=%s" % databaseuri)