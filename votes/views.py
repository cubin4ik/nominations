from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView
from .models import Nominations, Votes
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import User
from .forms import VotesForm


class NominationList(LoginRequiredMixin, ListView):
    model = Nominations
    template_name = "votes/index.html"

    login_url = 'account:login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NominationList, self).get_context_data(**kwargs)
        context['user_list'] = User.objects.all()

        user_votes = Votes.objects.filter(voter__id=1).values_list('nomination__id', flat=True)
        context['voted'] = list(user_votes)
        print(context['voted'])

        return context


class VoteCreate(LoginRequiredMixin, CreateView):
    model = Votes
    form_class = VotesForm
    success_message = 'Ваш голос принят!'

    login_url = 'account:login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VoteCreate, self).get_context_data(**kwargs)

        for key, value in self.request.GET.items():
            context[key] = value

        context['fav'] = User.objects.get(pk=context['nominee'])
        return context

    def get_initial(self):
        context = {"voter": self.request.user}

        for key, value in self.request.GET.items():
            context[key] = value

        return context
