from django import forms
from .models import RegistrationData,FeedbackData
# from django.forms import extras
from multiselectfield import MultiSelectFormField

class RegistrationForm(forms.Form):
    fname = forms.CharField(
        label="Enter Your firstname",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control'
            }
        )
    )

    lname = forms.CharField(
        label="Enter Your lastname",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control'
            }
        )
    )

    uname = forms.CharField(
        label="Enter Username",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control'
            }
        )
    )

    password1 = forms.CharField(
        label="Enter Password",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )

    mobile = forms.IntegerField(
        label="Enter Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Mobile Number',
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        label="Enter Your E-mail",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email Address',
                'class': 'form-control'
            }
        )
    )

    age = forms.IntegerField(
        label="Enter Your age",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Age',
                'class': 'form-control'
            }
        )
    )

    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)

    No_of_marriage = (('1', 'one'), ('2', 'two'), ('3', 'three'))
    No_of_marriages = forms.ChoiceField(widget=forms.RadioSelect, choices=No_of_marriage)

    expectation1 = (('kat', 'Katrina Kaif'), ('deepu', 'Deepika Padukone'), ('sunney', 'Sunney Leoni'))
    Expectation1 = MultiSelectFormField(max_length=100, choices=expectation1, required=False)

    expectation2 = (('sallu', 'Salman Khan'), ('sahid', 'Shahid Kapoor'), ('ranveer', 'Ranveer Singh'))
    Expectation2 = MultiSelectFormField(max_length=100, choices=expectation2,required=False)

    alcohol = (('no', 'No alcoholic'), ('yes', 'Only on weekends'), ('yes', 'Occasionally'))
    alcoholic_status = forms.ChoiceField(widget=forms.RadioSelect, choices=alcohol)

    more_info = forms.CharField(required=False,
        label="More info",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Please enter more information about preferences',
                'class': 'form-control'
            }
        )
    )

class LoginForm(forms.Form):
    uname = forms.CharField(
        label="Enter Username",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control'
            }
        )
    )

    pwd1 = forms.CharField(
        label="Enter Password",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )

    pwd2 = forms.CharField(
        label="Confirm Password",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        check = RegistrationData.objects.filter(username=username)
        if check.exists():
            raise forms.ValidationError('Username already exists.')
        elif len(username) <= 5:
            raise forms.ValidationError('Username must have more than 5 characters.')
        return username

    def clean_email(self):
        email1 = self.cleaned_data.get('email')
        check = RegistrationData.objects.filter(email=email1)
        if check.exists():
            raise forms.ValidationError('Email already exists.')
        elif not '@gmail.com' in email1:
            raise forms.ValidationError("Email id should must contain '@gmail.com'.")
        return email1

    def clean_mobile(self):
        mob = self.cleaned_data.get('mobile')
        check = RegistrationData.objects.filter(mobile=mob)
        if check.exists():
            raise forms.ValidationError('Mobile Number already taken.')
        elif len(str(mob)) != 10:
            raise forms.ValidationError('Please Enter valid mobile number. ')
        return mob

    def clean(self):
        data = self.cleaned_data
        pwd1 = self.cleaned_data.get('password1')
        pwd2 = self.cleaned_data.get('password2')
        if pwd2 != pwd1:
            raise forms.ValidationError('Password not matched.')
        elif len(pwd1) <= 4 or len(pwd1) >= 15:
            raise forms.ValidationError('Password length should be in between 4 to 15 only')
        return data

class FeedbackForm(forms.Form):
    fname = forms.CharField(
        label="Enter Your firstname",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control'
            }
        )
    )

    lname = forms.CharField(
        label="Enter Your lastname",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control'
            }
        )
    )

    mobile = forms.IntegerField(
        label="Enter Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Mobile Number',
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        label="Enter Your E-mail",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email Address',
                'class': 'form-control'
            }
        )
    )

    rating = forms.IntegerField(
        label="Enter Your rating points",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Rating Points',
                'class': 'form-control'
            }
        )
    )

    feedback = forms.CharField(required=False,
        label="Feedback",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Please enter feedback massage',
                'class': 'form-control'
            }
        )
    )








