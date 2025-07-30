from django import forms
from .models import DDSRecord, Category, Subcategory

class DDSRecordForm(forms.ModelForm):
    class Meta:
        model = DDSRecord
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'type': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'category': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'subcategory': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Subcategory.objects.none() # Список подкатегорий пуст, пока не выбрана категория

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by('name') # Выбрали категорию-фильтруем подкатегории по ней
            except (ValueError, TypeError):
                pass # Некорректные данные пропускаем
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.all() # При редактировании загружаем связанные категории
        
    def clean(self):
        cleaned_data = super().clean()
        # Валидация обязательных полей
        amount = cleaned_data.get('amount')
        type = cleaned_data.get('type')
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')

        errors = {}

        if amount is None:
            errors['amount'] = 'Поле "Сумма" обязательно.'
        if not type:
            errors['type'] = 'Поле "Тип" обязательно.'
        if not category:
            errors['category'] = 'Поле "Категория" обязательно.'
        if not subcategory:
            errors['subcategory'] = 'Поле "Подкатегория" обязательно.'

        if errors:
            raise forms.ValidationError(errors)
