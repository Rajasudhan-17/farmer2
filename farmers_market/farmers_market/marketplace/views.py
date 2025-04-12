from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request):
    if request.user.role != 'farmer':
        return redirect('dashboard')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user
            product.save()
            return redirect('farmer_dashboard')
    else:
        form = ProductForm()
    return render(request, 'marketplace/add_product.html', {'form': form})


@login_required
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'marketplace/product_list.html', {'products': products})
