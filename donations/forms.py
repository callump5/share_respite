from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('donation', 'email', 'stripe_id')


    MONTHS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]

    MONTH_CHOICES = list(enumerate(MONTHS, 1))
    YEAR_CHOICES = [(i, i) for i in range(2019, 2029)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='CVV')
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)