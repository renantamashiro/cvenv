from django.shortcuts import render, redirect

from .models import Product
from .forms import ProductModelForm


def list_products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/list.html', context=context)


def create_product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductModelForm()

    context = {'form': form}

    return render(request, 'products/create.html', context=context)


def delete_product(request, id_product):
    Product.objects.get(pk=id_product).delete()
    return redirect('products:list')


def update_product(request, id_product):
    product = Product.objects.get(pk=id_product)

    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductModelForm(instance=product)

    context = {'form': form}

    return render(request, 'products/update.html', context=context)
