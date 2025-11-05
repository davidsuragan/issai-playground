#  Configuration file for API settings
import os
from dotenv import load_dotenv

load_dotenv()

API_OYLAN = os.environ.get('API_OYLAN')

# Set the Assistant ID (#https://oylan.nu.edu.kz/api/v1/assistant/'ASSISTANT_ID', replace 'ASSISTANT_ID' with your actual ID )
ASSISTANT_ID = '1'  # Example: '1'

# OYLAN, Soyle App API endpoint base urls
URL_OYLAN = "https://oylan.nu.edu.kz/api/v1/"