from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, DetailView
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

        user_votes = Votes.objects.filter(voter__id=self.request.user.id).values_list('nomination__id', flat=True)
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


class WinnerView(DetailView):
    model = Nominations

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WinnerView, self).get_context_data(**kwargs)

        nomination_id = self.object.pk
        attendees = User.objects.all()

        winner_votes = 0
        winners = []

        for attendee in attendees:
            votes_count = Votes.objects.filter(nomination=nomination_id, nominee=attendee.id).count()

            if votes_count > winner_votes:
                winners.clear()
                winners.append(attendee)
                winner_votes = votes_count
                print(f'WINNER: {attendee} ({votes_count} votes)')
            elif votes_count == winner_votes:
                winners.append(attendee)
                winner_votes = votes_count
                print(f'WINNER: {attendee} ({votes_count} votes)')

        context['winners'] = winners

        reasons = []
        for winner in winners:
            reasons = Votes.objects.filter(nomination=nomination_id, nominee=winner.pk)

        context['reasons'] = reasons

        return context
