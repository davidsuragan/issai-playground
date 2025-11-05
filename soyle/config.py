# 
import os
from dotenv import load_dotenv

load_dotenv()

API_MAIN = os.environ.get("API_MAIN")
API_SOYLE = os.environ.get("API_SOYLE")

URL_SOYLE = "https://mangisoz.nu.edu.kz/external-api/v1/"