from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import CreateProductForm


def index_page(request):
    if request.method == 'GET':
        form = CreateProductForm()
        products = Product.objects.all()
        categories = Category.objects.all()
        return render(request, 'shop/index.html',
                      {
                          'products': products,
                          'categories': categories,
                          'form': form
                      })
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            name = form.data.get('name')
            price = form.data.get('price')
            amount = form.data.get('amount')
            description = form.data.get('description')
            category = form.data.get('category')
            product = Product(
                name=name,
                price=price,
                amount=amount,
                description=description,
                category=Category.objects.get(id=category),
            )
            product.save()
        return redirect('/')


def products_details(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'shop/product-details.html', {'product': product})


def delete_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('/')
    except Product.DoesNotExist as e:
        form = CreateProductForm()
        products = Product.objects.all()
        return render(request, 'shop/index.html',
                      {'products': products,
                       'form': form,
                       'error': 'Could delete product since it does not exist'
                       })
