from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "search/index.html")


def results(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q", "").strip()
    return render(request, "search/results.html", {"query": query})
