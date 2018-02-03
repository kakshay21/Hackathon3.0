from django import forms
from .models import Reviews
from tastypie.utils.timezone import now


class user_review(forms.Form):
    reviews = forms.CharField()
    ratings = forms.FloatField()

    class Meta:
        model = Reviews()
        fields = ('reviews', 'ratings')