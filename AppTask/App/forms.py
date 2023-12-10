# forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__title'}),
            'description': forms.Textarea(attrs={'class': 'form__description'}),
            # Puedes definir clases para otros campos aquí.
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Aquí aplicamos clases a los labels.
        self.fields['title'].label = 'Título'
        self.fields['description'].label = 'Descripción'
        self.fields['complete'].label = 'Completado'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form__title'
            # Esto añade la clase 'input-class' a todos los campos de entrada.
            field.label_classes = ('label-class',)
            # Esto crea un nuevo atributo en el campo para usarlo en la plantilla.
