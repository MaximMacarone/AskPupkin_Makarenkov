from app import models


def tag_list(request):
    tags = models.Tag.objects.get_popular()
    return {"tags": tags}

def member_list(request):
    members = models.Profile.objects.get_best()
    return {"members": members}