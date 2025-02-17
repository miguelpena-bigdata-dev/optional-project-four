from dotenv import load_dotenv
import os


load_dotenv()

DJANGO_SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
NYT_API_KEY = os.environ.get("NYT_API_KEY")
NYT_API_SECRET = os.environ.get("NYT_API_SECRET")
