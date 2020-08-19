
import psycopg2
from psycopg2 import OperationalError
import os

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URI = 'postgres+psycopg2://${DB_USERNAME}:${DB_PASSWORD}@localhost:5432/url_short'
