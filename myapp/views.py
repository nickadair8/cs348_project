from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from .models import LegoSet, Theme, Customer, Reviews
from .forms import LegoSetFilterForm, CustomerFilterForm, LegoSetForm, CustomerForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def sets(request):
    form = LegoSetFilterForm(request.GET or None)

    lego_sets = LegoSet.objects.all() #ORM

    if form.is_valid():
        selected_theme = form.cleaned_data.get('theme') #ORM
        selected_status = form.cleaned_data.get('status')
        selected_price_range = form.cleaned_data.get('price_range')

        if selected_theme:
            lego_sets = lego_sets.filter(theme_id=selected_theme)

        if selected_status:
            lego_sets = lego_sets.filter(status=selected_status)

        if selected_price_range:
            with connection.cursor() as cursor:
                sql_query = "SELECT set_id FROM myapp_legoset WHERE " #prepared statment
                params = []

                if selected_price_range == 'below_100':
                    sql_query += "price < %s"
                    params.append(100)
                elif selected_price_range == '100_300':
                    sql_query += "price >= %s AND price <= %s"
                    params.extend([100, 300])
                elif selected_price_range == '300_500':
                    sql_query += "price >= %s AND price <= %s"
                    params.extend([300, 500])
                elif selected_price_range == 'above_500':
                    sql_query += "price > %s"
                    params.append(500)

                cursor.execute(sql_query, params)
                rows = cursor.fetchall()

            set_ids = [row[0] for row in rows]
            lego_sets = lego_sets.filter(set_id__in=set_ids)

    context = {
        'form': form,
        'sets': lego_sets,
    }
    return render(request, 'sets.html', context)

def set_create(request):
    if request.method == 'POST':
        form = LegoSetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sets')
    else:
        form = LegoSetForm()
    return render(request, 'set_form.html', {'form': form})

def set_update(request, set_id):
    lego_set = get_object_or_404(LegoSet, pk=set_id)
    if request.method == 'POST':
        form = LegoSetForm(request.POST, instance=lego_set)
        if form.is_valid():
            form.save()
            return redirect('sets')
    else:
        form = LegoSetForm(instance=lego_set)
    return render(request, 'set_form.html', {'form': form})

def set_delete(request, set_id):
    lego_set = get_object_or_404(LegoSet, pk=set_id)
    if request.method == 'POST':
        lego_set.delete()
        return redirect('sets')
    return render(request, 'set_confirm_delete.html', {'lego_set': lego_set})

def customers(request):
    form = CustomerFilterForm(request.GET or None)

    customers = Customer.objects.all() #ORM

    if form.is_valid():
        selected_lego_set = form.cleaned_data.get('lego_set')
        selected_budget_range = form.cleaned_data.get('budget_range')

        if selected_lego_set:
            customers = customers.filter(set_id=selected_lego_set)

        if selected_budget_range:
            with connection.cursor() as cursor:
                sql_query = "SELECT lego_rewards_id FROM myapp_customer WHERE " #prepared statment
                params = []

                if selected_budget_range == 'below_100':
                    sql_query += "budget < %s"
                    params.append(100)
                elif selected_budget_range == '100_300':
                    sql_query += "budget >= %s AND budget <= %s"
                    params.extend([100, 300])
                elif selected_budget_range == '300_500':
                    sql_query += "budget >= %s AND budget <= %s"
                    params.extend([300, 500])
                elif selected_budget_range == 'above_500':
                    sql_query += "budget > %s"
                    params.append(500)

                cursor.execute(sql_query, params)
                rows = cursor.fetchall()

            customer_ids = [row[0] for row in rows]
            customers = customers.filter(lego_rewards_id__in=customer_ids)

    context = {
        'form': form,
        'customers': customers,
    }
    return render(request, 'customers.html', context)

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')  
        else:
            return render(request, 'customer_form.html', {'form': form, 'errors': form.errors})
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def customer_update(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.lego_rewards_id = request.POST.get('lego_rewards_id')
        customer.set_id = request.POST.get('set_id')
        customer.budget = request.POST.get('budget')
        customer.save()
        return redirect('customers')
    return render(request, 'customer_form.html', {'customer': customer})

def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers')
    return render(request, 'customer_confirm_delete.html', {'customer': customer})

def review_detail(request, review_id):
    review = get_object_or_404(Reviews, id=review_id)
    return render(request, 'review_detail.html', {'review': review})