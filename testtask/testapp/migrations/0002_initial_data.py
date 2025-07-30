from django.db import migrations

def add_initial_data(apps, schema_editor):
    Status = apps.get_model('testapp', 'Status')
    Type = apps.get_model('testapp', 'Type')
    Category = apps.get_model('testapp', 'Category')
    Subcategory = apps.get_model('testapp', 'Subcategory')

    for name in ['Бизнес', 'Личное', 'Налог']:
        Status.objects.get_or_create(name=name)

    type_pop, _ = Type.objects.get_or_create(name='Пополнение')
    type_exp, _ = Type.objects.get_or_create(name='Списание')

    cat_marketing, _ = Category.objects.get_or_create(name='Маркетинг', type=type_exp)
    cat_infra, _ = Category.objects.get_or_create(name='Инфраструктура', type=type_exp)

    cat_retail, _ = Category.objects.get_or_create(name='Розница', type=type_pop)

    for name in ['Farpost', 'Avito']:
        Subcategory.objects.get_or_create(name=name, category=cat_marketing)

    for name in ['VPS', 'Proxy']:
        Subcategory.objects.get_or_create(name=name, category=cat_infra)

    for name in ['Wildberries','Ozon']:
        Subcategory.objects.get_or_create(name=name, category=cat_retail)

class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
