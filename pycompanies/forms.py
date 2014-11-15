from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, ButtonHolder, Layout, Submit

from .models import Company


class CompanyForm(forms.ModelForm):
    """A PyAr companies form."""

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                'name',
                'photo',
                'link',
                'description'
            ),
            ButtonHolder(
                Submit(_('Guardar'), _('Guardar'), css_class='btn btn-default')
            )
        )

    class Meta:
        fields = ['name', 'photo', 'link', 'description']
        model = Company
