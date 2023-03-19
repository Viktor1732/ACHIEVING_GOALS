from django import forms

from .models import *


class CreateGoalsForm(forms.ModelForm):
    CHOICES_CATEGORY = (
        ('', 'Категория не выбрана'),
        ('Личный рост', 'Личный рост'),
        ('Образование', 'Образование'),
        ('Иностранные языки', 'Иностранные языки'),
        ('Хобби', 'Хобби'),
        ('Творчество', 'Творчество'),
        ('Карьера и работа', 'Карьера и работа'),
        ('Финансы', 'Финансы'),
        ('Покупки', 'Покупки'),
        ('Здоровье', 'Здоровье'),
        ('Спорт', 'Спорт'),
        ('Отдых', 'Отдых'),
        ('Взаимоотношения', 'Взаимоотношения'),
        ('Другое', 'Другое'),
    )

    CHOICES_PRIVACY = (
        ('Приватная', 'Приватная'),
        ('Публичная', 'Публичная'),
    )

    category = forms.CharField(
        widget=forms.Select(choices=CHOICES_CATEGORY, attrs={
            'name': "category", 'id': "category", 'class': "form-control cursor-pointer"
        }))

    privacy = forms.CharField(
        widget=forms.Select(choices=CHOICES_PRIVACY, attrs={
            'name': "privacy", 'id': "privacy", 'class': "form-control cursor-pointer"
        }))

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


class UpdateGoalForm(forms.ModelForm):
    CHOICES_CATEGORY = (
        ('', 'Категория не выбрана'),
        ('Личный рост', 'Личный рост'),
        ('Образование', 'Образование'),
        ('Иностранные языки', 'Иностранные языки'),
        ('Хобби', 'Хобби'),
        ('Творчество', 'Творчество'),
        ('Карьера и работа', 'Карьера и работа'),
        ('Финансы', 'Финансы'),
        ('Покупки', 'Покупки'),
        ('Здоровье', 'Здоровье'),
        ('Спорт', 'Спорт'),
        ('Отдых', 'Отдых'),
        ('Взаимоотношения', 'Взаимоотношения'),
        ('Другое', 'Другое'),
    )

    CHOICES_PRIVACY = (
        ('Приватная', 'Приватная'),
        ('Публичная', 'Публичная'),
    )

    category = forms.CharField(
        widget=forms.Select(choices=CHOICES_CATEGORY, attrs={
            'name': "category", 'id': "category", 'class': "form-control cursor-pointer"
        }))

    privacy = forms.CharField(
        widget=forms.Select(choices=CHOICES_PRIVACY, attrs={
            'name': "privacy", 'id': "privacy", 'class': "form-control cursor-pointer"
        }))

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


class FormSendMessage(forms.Form):
    name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', }))
    email = forms.EmailField(
        max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', }))
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={'class': 'form-textarea-control', 'name': 'goal-desc', 'id': 'id_goal_desc'}))
