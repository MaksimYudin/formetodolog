from django.forms import ModelForm
from .models import  Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
import account.forms
from datetime import datetime


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'birth_date')

class UserCreateForm(UserCreationForm):

    location = forms.CharField(max_length=100, required=False)
    birth_date = forms.DateField(required=False, widget=forms.DateInput(
                            attrs= {
                                    'class':'datepicker'
                                }), input_formats=['%d-%m-%Y'], localize=True)
    '''birth_date = forms.DateField(required=False, widget=forms.DateInput(format='%d-%m-%Y',
                                                attrs={
                                                            'type': 'date',
                                                            'data-provide': 'datepicker'
                                                   #        # 'data-date-format': 'dd-mm-yyyy',
                                                        }),
                                     initial=format(datetime.today().date(), '%d-%m-%Y'),
                                     input_formats=['%d-%m-%Y'],localize=True

                                 )'''

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        #user_profile = Profile(user=user, location=self.cleaned_data['location'],
        #                       birth_date=self.cleaned_data['birth_date'])
        user_profile = Profile.objects.get(user=user.id)
        user_profile.location = self.cleaned_data['location']
        user_profile.birth_date = self.cleaned_data['birth_date']
        user_profile.save()
        return user, user_profile

class SignupForm(account.forms.SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]

    location = forms.CharField(max_length=100, required=False)
    birthdate = forms.DateField(required=False, widget=forms.DateInput(
                            attrs= {
                                    'class':'datepicker'
                                }), input_formats=['%d-%m-%Y'], localize=True)
