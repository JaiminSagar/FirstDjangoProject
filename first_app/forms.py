from django import forms
from django.contrib.auth.models import User
from first_app.models import User_Model,UserProfileInfo
# from django.core import validators

# For Own Custom Validators
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name Needs To START with Z")

# class FormName(forms.Form):
#     name = forms.CharField()  # validators=[check_for_z] inside parameters
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label="Enter Your Email Again:")
#     text = forms.CharField(widget=forms.Textarea)

#      Cleaning the entire form from one Method using special Clean Method
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         v_email = all_clean_data['verify_email']

#         if email != v_email:
#             raise forms.ValidationError("MAke sure Emails Match")

    # For Built-in Validators
    # bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # For Bot Catcher .......
    # bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput)
    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("Gotta Bot!....")
    #     return bot_catcher


class NewUserModelForm(forms.ModelForm):
    class Meta:
        model = User_Model
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')



