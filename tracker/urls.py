from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add/", views.add_application, name="add"),
    path("edit/<int:app_id>/", views.edit_application, name="edit"),
    path("delete/<int:app_id>/", views.delete_application, name="delete"),
    path("update-status/<int:app_id>/", views.update_status, name="update_status"),
    path("delete-ajax/<int:app_id>/", views.delete_ajax, name="delete_ajax")

]
