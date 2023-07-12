from django.http import HttpResponse
from django.shortcuts import render

from supercats.models import Cat

# Create your views here.

def hello_cat(request):
    cat_list = Cat.objects.order_by("-created")[:5]

    context = {
        "cat_list": cat_list,
    }
    return render(request, "hello_cat.html", context)


def results(request, cat_id: int) -> HttpResponse:
    response = "You're looking at the results of cat %s."
    return HttpResponse(response % cat_id)


def vote(request, cat_id):
    return HttpResponse("You're voting on cat %s." % cat_id)