from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListCrudAPIView.as_view(), name="crud_list"),
    path("create/", views.CreateCrudAPIVeiw.as_view(), name="crud_create"),
    path("update/<int:pk>/", views.UpdateCrudAPIView.as_view(), name="crud_update"),
    path("delete/<int:pk>/", views.DeleteCrudAPIView.as_view(), name="crud_delete"),
]
