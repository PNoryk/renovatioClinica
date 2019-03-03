from django import forms


class UsersForm(forms.Form):
    clinic_id = forms.CharField()
    profession_id = forms.CharField()
    role = forms.CharField(required=False)
