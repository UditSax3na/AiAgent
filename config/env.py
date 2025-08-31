from dotenv import load_dotenv
import os

# loading the environment to get the data
load_dotenv()

# getting the api key from teh .env
API_KEY = os.getenv("OPENROUTER_API_KEY")