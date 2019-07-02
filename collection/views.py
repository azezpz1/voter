from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def user_home(request):
    return render(request, "collection/user_home.html")
