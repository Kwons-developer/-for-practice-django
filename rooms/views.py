# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage

from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     page = int(page or 1)
#     page_size = 10
#     limit = page_size * page
#     offset = limit - page_size
#     all_rooms = models.Room.objects.all()[offset:limit]
#     page_count = ceil(models.Room.objects.count() / page_size)
#     return render(
#         request,
#         "rooms/home.html",
#         context={
#             "rooms": all_rooms,
#             "page": page,
#             "page_count": page_count,
#             "page_range": range(1, page_count + 1),
#         },
#     )


# def all_rooms(request):
#     """ Use Paginator """
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.get_page(int(page))
#         return render(request, "rooms/home.html", {"page": rooms})
#     except EmptyPage:
#         return redirect("/")


class HomeView(ListView):
    """ Class Based View """

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ Room Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    room_types = models.RoomType.objects.all()

    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
    }

    choice = {
        "countries": countries,
        "room_types": room_types,
    }
    return render(
        request,
        "rooms/search.html",
        {**form, **choice},
    )
