from app import models
import jwt
import time
from AskPupkin_Makarenkov.settings import CENTRIFUGO_SECRET_KEY, CENTRIFUGO_WS_URL

def get_centrifugo_info(request):
    secret = CENTRIFUGO_SECRET_KEY
    ws_url = CENTRIFUGO_WS_URL
    claims = {"sub": str(request.user.id), "exp": int(time.time()) + 5*60}
    token = jwt.encode(claims, secret, algorithm="HS256")
    return {"token": token, "ws_url": ws_url}


def tag_list(request):
    tags = models.Tag.objects.get_popular()
    return {"tags": tags}

def member_list(request):
    members = models.Profile.objects.get_best()
    return {"members": members}
