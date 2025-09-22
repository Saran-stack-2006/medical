from django import forms
from .models import Profile


class ProfileCompletionForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["address", "health_details", "preferences"]


from .models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ["name", "mobile", "order_id", "issue"]


class TrackForm(forms.Form):
    mobile = forms.CharField(max_length=10)
    order_id = forms.CharField(max_length=100)


from django import forms
from .models import CallBackRequest


class CallBackRequestForm(forms.ModelForm):
    class Meta:
        model = CallBackRequest
        fields = ["name", "phone", "preferred_time"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "preferred_time": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Optional: e.g., 2 PM - 4 PM",
                }
            ),
        }


from django import forms
from .models import Report


class ReportUploadForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["test_name", "test_value", "report_file"]
