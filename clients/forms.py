import datetime

from django import forms
from django.forms import Select, SelectDateWidget
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
            clinic_id_choices.add((client["id"], str(client["id"]) + " " + client["title"]))
        self.fields["clinic_id"].choices = sorted(clinic_id_choices)

        professions_id_choices = set()
        for professions in getProfessions()["data"]:
            professions_id_choices.add((professions["id"], professions["name"]))
        self.fields["profession_id"].choices = professions_id_choices


class ScheduleForm(forms.Form):
    clinic_id = forms.ChoiceField(label="Clinic")
    user_id = forms.CharField(label="User", widget=Select)
    current_year = datetime.date.today().year
    time_start = forms.DateField(widget=SelectDateWidget(years=range(current_year - 1, current_year + 2)))
    time_end = forms.DateField(initial=datetime.date.today,
                               widget=SelectDateWidget(years=range(current_year - 1, current_year + 2)))

    STEP_CHOICES = ("10", "15", "20", "30", "60")
    step = forms.IntegerField(initial="60", widget=Select(choices=((i, i) for i in STEP_CHOICES)))

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None,
                 renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order,
                         use_required_attribute, renderer)

        clinic_id_choices = set()
        for client in getClinics()["data"]:
            clinic_id_choices.add((client["id"], f"{client['id']}. {client['title']}"))
        self.fields["clinic_id"].choices = sorted(clinic_id_choices)
