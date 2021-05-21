# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
#
# SQLALCHEMY_DATABASE_URL = "mysql://domos-user:domos-user-password@database/domos-db"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
# Base = declarative_base()

import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="192.168.1.5",
        user="domos-user",
        password="domos-user-password",
        database="domos-db"
    )
    return connection
