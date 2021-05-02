from django import forms
from .models import Ticketinfo


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticketinfo
        fields = '__all__'
        genderChoices = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others')
        )
        widgets = {
            'gender': forms.RadioSelect(choices=genderChoices, attrs={'class': "custom-list"}),
            'dateofdeparture': forms.DateInput(attrs={'type': 'date', 'required': True}),
        }
