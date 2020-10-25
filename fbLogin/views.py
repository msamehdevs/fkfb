from django.shortcuts import render
from .models import InfoIn

def index(request):
    messages = []
    context = {}
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pwd']

        if username == '':
            messages.insert(len(messages),'Pease insert Username')

        if password == '':
            messages.insert(len(messages),'Please insert Password')

        if len(messages) == 0:
            info = InfoIn(username=username, password=password)
            info.save()
        else:
            context = {'messages': messages}



    return render(request, 'fbLogin/index.html', context)

def view_info(request):
    infos = InfoIn.objects.all()
    return render(request, 'fbLogin/info.html', {'infos': infos})