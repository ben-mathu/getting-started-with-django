from django.urls import path
from .views import home_page, lead_list, lead_detail, lead_create, lead_update, lead_delete

app_name = "leads"

urlpatterns = [
    path('', home_page),
    path('lists/', lead_list),
    path('lists/<id>/', lead_detail),
    path('lists/<id>/update', lead_update),
    path('lists/<id>/delete', lead_delete),
    path('create/', lead_create),
]
