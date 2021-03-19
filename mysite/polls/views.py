from django.http import HttpResponse


def index(request):
    return HttpResponse("はろーわーるど。pollsの最初のページです")
