import configparser
import pathlib

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

username = config.get("DEV_DB", "USER")
password = config.get("DEV_DB", "PASSWORD")
db_name = config.get("DEV_DB", "DB_NAME")
domain = config.get("DEV_DB", "DOMAIN")
port = config.get("DEV_DB", "PORT")

url = f"postgresql://{username}:{password}@{domain}:{port}/{db_name}"

engine = create_engine(url, echo=True, pool_size=5, max_overflow=0)

DBSession = sessionmaker(bind=engine)
session = DBSession()
