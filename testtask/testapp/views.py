from django.shortcuts import render, get_object_or_404, redirect
from .models import DDSRecord, Type, Category, Subcategory, Status
from .forms import DDSRecordForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def index(request):
    records = DDSRecord.objects.all()

    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    type_id = request.GET.get('type')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')
    status_id = request.GET.get('status')

    if date_from:
        records = records.filter(date__gte=date_from)
    if date_to:
        records = records.filter(date__lte=date_to)
    if type_id:
        records = records.filter(type_id=type_id)
    if category_id:
        records = records.filter(category_id=category_id)
    if subcategory_id:
        records = records.filter(subcategory_id=subcategory_id)
    if status_id:
        records = records.filter(status_id=status_id)

    return render(request, 'testapp/index.html', {
        'records': records,
        'types': Type.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
        'statuses': Status.objects.all(),
        'filters': {
            'date_from': date_from,
            'date_to': date_to,
            'type': type_id,
            'category': category_id,
            'subcategory': subcategory_id,
            'status': status_id,
        }
    })


def create_record(request):
    if request.method == 'POST':
        form = DDSRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DDSRecordForm()
    return render(request, 'testapp/create_edit_record.html', {'form': form})

def edit_record(request, pk):
    record = get_object_or_404(DDSRecord, pk=pk) # Поиск по PrimaryKey(ID) или 404
    if request.method == 'POST':
        # Обновляем запись
        form = DDSRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DDSRecordForm(instance=record)
    return render(request, 'testapp/create_edit_record.html', {'form': form})

@require_POST
def delete_record(request, pk):
    record = get_object_or_404(DDSRecord, pk=pk) # Удаление записи по PrimaryKey(ID)
    record.delete()
    return redirect('index')

def load_categories(request):
    type_id = request.GET.get('type')
    if type_id:
        categories = Category.objects.filter(type_id=type_id).order_by('name')
    else:
        categories = Category.objects.none()
    data = list(categories.values('id', 'name'))
    return JsonResponse(data, safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category')
    if category_id:
        subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    else:
        subcategories = Subcategory.objects.none()
    data = list(subcategories.values('id', 'name'))
    return JsonResponse(data, safe=False)