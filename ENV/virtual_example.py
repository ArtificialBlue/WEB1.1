import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv('MY_API_TOKEN')
print(secret_key)