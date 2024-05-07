from django import forms
from .models import Contact

select_mode_of_contact = (
    ("email", "E-Mail"),
    ("phone", "Phone"),
)

select_question_categories = (
    ("certification", "Certification"),
    ("interview", "Interview"),
    ("material", "Material"),
    ("access_duration","Access and Duration"),
    ("other", "Others"),
)

class ContactForm(forms.ModelForm):
    phone = forms.CharField(required=False)
    mode_of_contact = forms.CharField(required=False, widget=forms.RadioSelect(choices=select_mode_of_contact))
    question_categories = forms.CharField(required=False, widget=forms.Select(choices=select_question_categories))

    class Meta:
        model = Contact
        fields = '__all__'


# *****************************************************
# Newsletter
from .models import NewsletterUser
from crispy_forms.helper import FormHelper
class NewsletterUserSignUpForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email
