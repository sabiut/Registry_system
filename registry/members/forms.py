from .models import*
from django import forms
from django.contrib.admin import widgets

#testing bootstrap_datepicker_plus
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
#end testing datepiceker

import datetime




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ContactForm(forms.ModelForm):
    class Meta:
        model =contacts
        fields = ('First_Name','Middle_Name','Last_Name','Date_of_Birth','Gender','Island','Province','Date_of_Baptism','Congregation','Status','Comments',)
        widgets = {'Date_of_Birth': SelectDateWidget(years=range(1930, 2090)), 'Date_of_Baptism':SelectDateWidget(years=range(1930, 2090))}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Gender', 'Phone','island','city','country','organization',)

#adding minute forms
class addminuteform(forms.ModelForm):
    class Meta:
        model=minutes
        fields=('date','Taken_By','Agender','body','comment',)
        widgets = {'date': SelectDateWidget(years=range(1930, 2090))}




#uploading file form
class uploadfileform(forms.ModelForm):
	class Meta:
		model=uploadfolder
		fields=('File_to_upload',)
