from django import forms
from django.forms.utils import ErrorList

from clients.dataRequests import getClinics, getProfessions


class UsersForm(forms.Form):
    clinic_id = forms.ChoiceField(label="Clinic")
    profession_id = forms.ChoiceField(label="Profession")
    role = forms.CharField(required=False)

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None,
                 renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order,
                         use_required_attribute, renderer)

        clinic_id_choices = set()
        for client in getClinics()["data"]:
            clinic_id_choices.add((client["id"], client["title"]))
        self.fields["clinic_id"].choices = clinic_id_choices

        professions_id_choices = set()
        for client in getProfessions()["data"]:
            professions_id_choices.add((client["id"], client["name"]))
        self.fields["profession_id"].choices = professions_id_choices
