from django.urls import path, include
from cinema.views import MovieViewSet, ActorList, ActorDetail, GenreList, GenreDetail, CinemaHallViewSet
from rest_framework import routers


app_name = 'cinema'

cinemahall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)

cinemahall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns =[
    path("genres/", GenreList.as_view(), name="cinema_hall"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="cinema_hall_detail"),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("cinemahalls/", cinemahall_list, name="cinema_hall"),
    path("cinemahalls/<int:pk>/", cinemahall_detail, name="cinema_hall_detail"),
    path("", include(router.urls)),
]
