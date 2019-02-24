from django import forms

from .models import Profile, Message

class MsgForm(forms.ModelForm):
    sender = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))
    receiver = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))
    class Meta:
        model = Message
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control mb-2 mr-2'}),
        }

class ProfileForm(forms.ModelForm):
    car_make = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-2', 'placeholder': 'Make'}),
                               required=False)
    car_model = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-2', 'placeholder': 'Model'}),
                                required=False)
    plate = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-2', 'placeholder': 'Plate #'}),
                            required=False)
    class Meta:
        model = Profile
        fields = ('hometown', 'major', 'phone_number', 'affiliation', 'bio',
                  'org_email', 'venmo')
        widgets = {
            'hometown': forms.TextInput(attrs={'class': 'form-control mb-2 mr-2'}),
            'major': forms.TextInput(attrs={'class': 'form-control mb-2 mr-2'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control mb-2 mr-2', 'placeholder': '555-555-5555'}),
            'affiliation': forms.Select(attrs={'class': 'custom-select mb-2 mr-2', 'onchange': 'affiliate();'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'org_email': forms.TextInput(attrs={'class': 'form-control mb-2 mr-2'}),
            'venmo': forms.TextInput(attrs={'class': 'form-control mb-2 mr-2'}),
        }
