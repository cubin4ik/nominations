from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from .models import Votes


class VotesForm(forms.ModelForm):
    class Meta:
        model = Votes
        fields = '__all__'
        widgets = {
            'nomination': forms.HiddenInput(),
            'voter': forms.HiddenInput(),
            'nominee': forms.HiddenInput(),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Вы уже проголосовали в этой номинации",
            }
        }
