#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23111859"))
API_HASH = environ.get("API_HASH", "e83a8fc0c228487183f74de936eafd21")
BOT_TOKEN = environ.get("BOT_TOKEN", "8000600707:AAFLwRBWMnXRu6VisBcZxstPR4RHmi4tQs8")
OWNER = int(environ.get("OWNER", "7541970367"))
CREDIT = "GᗩᒍEᑎᗪᖇᗩ ᔕIᑎGᕼ"
AUTH_USER = os.environ.get('AUTH_USERS', '7541970367').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
