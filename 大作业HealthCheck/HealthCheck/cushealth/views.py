from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomerHealth
from .forms import CustomerHealthForm


def health_check_list(request):
    customers = CustomerHealth.objects.all()
    return render(request, 'cushealth/health_check_list.html', {'customers': customers})

def add_health_check(request):
    if request.method == "POST":
        form = CustomerHealthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('health_check_list')
    else:
        form = CustomerHealthForm()
    return render(request, 'cushealth/health_check_form.html', {'form': form})

def edit_health_check(request, pk):
    customer = get_object_or_404(CustomerHealth, pk=pk)
    if request.method == "POST":
        form = CustomerHealthForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('health_check_list')
    else:
        form = CustomerHealthForm(instance=customer)
    return render(request, 'cushealth/health_check_form.html', {'form': form})

def delete_health_check(request, pk):
    customer = get_object_or_404(CustomerHealth, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('health_check_list')
    return render(request, 'cushealth/health_check_confirm_delete.html', {'customer': customer})



def search_health_check(request):
    results = []
    if request.method == 'POST':
        uId = request.POST.get('uId')
        if uId:
            results = CustomerHealth.objects.filter(uId=uId)
    return render(request, 'cushealth/search_health_check.html', {'results': results})
