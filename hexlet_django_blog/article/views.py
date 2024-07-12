
from django.views import View
from django.shortcuts import render, redirect


class IndexView(View):

    def get(request, *args):
        response = redirect('python/42/')
        return response


def index(request, tags, id):
    return render(
        request,
        'articles/index.html',
        context={'tags': tags, 'id': id},
    )
