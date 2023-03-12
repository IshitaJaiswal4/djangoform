from django import forms
from .models import UserForm
from datetime import date, timedelta


from datetimewidget.widgets import DateWidget


class UserFormForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ['name', 'dob', 'email', 'phone_number']
        widgets = {
            'dob': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
        }

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        age = (date.today() - dob) // timedelta(days=365.2425)
        if age < 18:
            raise forms.ValidationError('You must be 18 years or older to submit the form')
        return dob
