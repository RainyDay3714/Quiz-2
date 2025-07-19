from django.urls import path
from .views import applicant_list_view, ApplicantDetailView, ApplicantDeleteView

urlpatterns = [
    path('', applicant_list_view, name='applicant.list'),
    path('portfolio/<str:username>/', ApplicantDetailView.as_view(), name='applicant.detail'),
    path('portfolio/<str:username>/delete/', ApplicantDeleteView.as_view(), name='applicant.delete'),
]