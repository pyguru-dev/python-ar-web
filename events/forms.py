from django import forms
from django_summernote.widgets import SummernoteInplaceWidget
from django.utils.translation import ugettext_lazy as _

from bootstrap3_datetime.widgets import DateTimePicker
from crispy_forms.layout import Submit, Reset, Layout, Div, Field
from crispy_forms.helper import FormHelper

from .models import Event


class EventForm(forms.ModelForm):

    description = forms.CharField(widget=SummernoteInplaceWidget())

    start_at = forms.DateField(
        required=False,
        label=_('Comienza'),
        widget=DateTimePicker(
            options={
                "format": "DD/MM/YYYY"
            }
        )
    )

    end_at = forms.DateField(
        required=False,
        label=_('Finaliza'),
        widget=DateTimePicker(
            options={
                "format": "DD/MM/YYYY"
            }
        )
    )

    class Meta:
        model = Event
        fields = (
            'name',
            'description',
            'place',
            'address',
            'url',
            'start_at',
            'end_at'
        )

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_method = "post"
        self.helper.add_input(Submit('job_submit', _('Guardar')))
        self.helper.add_input(Reset('job_reset', _('Limpiar'), css_class='btn-default'))
        self.helper.layout = Layout(
            Div(
                'name',
                'description',
                'place',
                'address',
                'url',
                'start_at',
                'end_at',
            )
        )

    def save(self, *args, **kwargs):
        super(EventForm, self).save(*args, **kwargs)
        self.instance.save()
