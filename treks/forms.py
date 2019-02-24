from django import forms

from .models import Trek, Request

class TrekForm(forms.ModelForm):
    from_addr = forms.CharField(required=False,
                          widget=forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                                        'placeholder': 'Street Address (optional)'}))
    to_addr = forms.CharField(required=False,
                        widget=forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                                      'placeholder': 'Street Address (optional)'}))
    departure_time = forms.TimeField(input_formats=['%H:%M', '%I:%M%p', '%I%p', '%I%M%p', '%I%M %p', '%I:%M %p', '%H%M'],
                               widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mb-2'}))
    arrival_time = forms.TimeField(input_formats=['%H:%M', '%I:%M%p', '%I%p', '%I%M%p', '%I%M %p', '%I:%M %p', '%H%M'],
                               widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mb-2'}))
    class Meta:
        model = Trek
        fields = ('date', 'departure_time', 'arrival_time', 'from_addr',
                  'from_city', 'from_state', 'to_addr', 'to_city', 'to_state',
                  'seats', 'price', 'note', 'flexible_departure', 'pickup',
                  'pickup_radius', 'dropoff', 'dropoff_radius', 'fem_only',
                  'org_only', 'edu_only', 'mutuals_only')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-2'}),
            'from_city': forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                                'placeholder': 'City'}),
            'from_state': forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                                 'placeholder': 'State'}),
            'to_city': forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                              'placeholder': 'City'}),
            'to_state': forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                                 'placeholder': 'State'}),
            'pickup_radius': forms.NumberInput(attrs={'type': 'range', 'max': '10', 'min': '1', 'step': '1'}),
            'dropoff_radius': forms.NumberInput(attrs={'type': 'range', 'max': '10', 'min': '1', 'step': '1'}),
            'seats': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': '4'}),
        }

class ReqForm(forms.ModelForm):
    from_addr = forms.CharField(required=False,
                          widget=forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                                        'placeholder': 'Street Address (optional)'}))
    to_addr = forms.CharField(required=False,
                        widget=forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                                      'placeholder': 'Street Address (optional)'}))
    departure_time = forms.TimeField(input_formats=['%H:%M', '%I:%M%p', '%I%p', '%I%M%p', '%I%M %p', '%I:%M %p', '%H%M'],
                               widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mb-2'}))
    arrival_time = forms.TimeField(input_formats=['%H:%M', '%I:%M%p', '%I%p', '%I%M%p', '%I%M %p', '%I:%M %p', '%H%M'],
                               widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mb-2'}))
    class Meta:
        model = Request
        fields = ('date', 'departure_time', 'arrival_time', 'from_addr',
                  'from_city', 'from_state', 'to_addr', 'to_city', 'to_state',
                  'note', 'flexible_departure', 'pickup', 'pickup_radius',
                  'dropoff', 'dropoff_radius', 'fem_only', 'org_only',
                  'edu_only', 'mutuals_only')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-2'}),
            'from_city': forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                                'placeholder': 'City'}),
            'from_state': forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                                 'placeholder': 'State'}),
            'to_city': forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                              'placeholder': 'City'}),
            'to_state': forms.TextInput(attrs={'class': 'form-control mr-2 mb-2',
                                                 'placeholder': 'State'}),
            'pickup_radius': forms.NumberInput(attrs={'type': 'range', 'max': '10', 'min': '1', 'step': '1'}),
            'dropoff_radius': forms.NumberInput(attrs={'type': 'range', 'max': '10', 'min': '1', 'step': '1'}),
            'note': forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': '4'}),
        }
