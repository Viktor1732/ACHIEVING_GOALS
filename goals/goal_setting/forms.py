from django import forms

from .models import *


class CreateGoalsForm(forms.ModelForm):
    CHOICES_CATEGORY = (
        ('1', 'Категория не выбрана'),
        ('2', 'Творчество и хобби'),
        ('3', 'Дом'),
        ('4', 'Здоровье'),
        ('5', 'Семья'),
        ('6', 'Языки'),
        ('7', 'Образование'),
        ('8', 'Социальные навыки'),
        ('9', 'Карьера'),
        ('10', 'Бизнес'),
        ('11', 'Другое'),
    )

    CHOICES_PRIVACY = [
        ('1', 'Приватная'),
        ('2', 'Публичная'),
    ]

    category = forms.CharField(
        widget=forms.Select(choices=CHOICES_CATEGORY, attrs={
            'name': "category", 'id': "category", 'class': "form-control cursor-pointer"
        }))

    privacy = forms.ChoiceField(
        widget=forms.RadioSelect(choices=CHOICES_PRIVACY, )
    )

    class Meta:
        model = Goals
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'goal_title', 'name': 'goal-title', 'type': 'text'}),
            'description': forms.Textarea(
                attrs={'class': 'form-textarea-control', 'name': 'goal-desc', 'id': 'id_goal_desc'}),
            'time_of_end': forms.DateTimeInput(
                attrs={'name': "target", 'id': "target",
                       'class': "form-control cursor-pointer", 'type': "date"}),
            'image': forms.FileInput(attrs={'class': 'form-control-hidden', 'type': "file",
                                            'name': "goal-photo", 'accept': "image/png, image/jpg, image/jpeg",
                                            'required': "", 'id': "upload-file"}),
        }

