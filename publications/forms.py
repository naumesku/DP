from django import forms
from publications.models import Publication


class PublicationForm(forms.ModelForm):
    """Форма публикации"""
    class Meta:
        model = Publication
        fields = ['title', 'body', 'photo', 'is_active', 'is_pay']

    def __init__(self, user, *args, **kwargs, ):
        self.user = user
        super(PublicationForm, self).__init__(*args, **kwargs)

        if not user.is_vip:
            del self.fields['is_pay']

        for field_name, field in self.fields.items():
            if field_name != 'is_pay' and field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'
