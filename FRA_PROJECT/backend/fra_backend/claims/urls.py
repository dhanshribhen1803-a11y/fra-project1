from django.urls import path
from .views import submit_claim, get_claims, update_status

urlpatterns = [
    path("submit/", submit_claim),
    path("list/", get_claims),
    path("update/", update_status),
]
