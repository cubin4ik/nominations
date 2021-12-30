from django.urls import path
from .views import NominationList, VoteCreate

urlpatterns = [
    path('', NominationList.as_view(), name='index'),
    path('vote', VoteCreate.as_view(), name='vote'),
]
