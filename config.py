from dotenv import load_dotenv
import os

load_dotenv()

class ENV:
    
    db_host = os.getenv("DB_HOST")
    db_port = int(os.getenv("DB_PORT"))
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_type = os.getenv("DB_TYPE")


print("ENV is loaded")