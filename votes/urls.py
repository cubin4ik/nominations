from django.urls import path
from .views import NominationList, VoteCreate, WinnerView

urlpatterns = [
    path('', NominationList.as_view(), name='index'),
    path('vote', VoteCreate.as_view(), name='vote'),
    path('nominations/<int:pk>/', WinnerView.as_view(), name='nomination'),
]
