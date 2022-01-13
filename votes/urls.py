from django.urls import path
from .views import NominationList, VoteCreate, WinnerView

urlpatterns = [
    path('', NominationList.as_view(), name='index'),
    path('vote', VoteCreate.as_view(), name='vote'),
    path('nomination/<int:pk>/', WinnerView.as_view(), name='winner'),
]
