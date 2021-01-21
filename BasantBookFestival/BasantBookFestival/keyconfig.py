import os


class Database:
    NAME = os.getenv("POSTGRES_DB") or "sqlite3"
    USER = os.getenv("POSTGRES_USER") or "default"
    PASSWORD = os.getenv("POSTGRES_PASSWORD") or "default"
    HOST = os.getenv("DATABASE_HOST") or "default"
    PORT = os.getenv("DATABASE_PORT") or 5432


class Secrets:
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY') or 'backend'
