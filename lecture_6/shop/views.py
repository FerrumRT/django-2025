from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm


def index_category(request):
    if request.method == 'GET':
        form = CategoryForm()
        categories = Category.objects.all()
        return render(request, 'shop/index.html',
                      {
                          'categories': categories,
                          'form': form
                      })
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        return render(request, 'shop/update_category.html',
                      {
                          'category': category,
                          'form': form
                      })
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('/')


def delete_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        category.delete()
        return redirect('/')
    except Product.DoesNotExist as e:
        return redirect('index')


def category_details(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'GET':
        form = ProductForm()
        products = Product.objects.filter(category=category_id)
        return render(request, 'shop/category_details.html',
                      {
                          'products': products,
                          'category': category,
                          'form': form
                      })
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            amount = form.cleaned_data.get('amount')
            description = form.cleaned_data.get('description')
            image = form.cleaned_data.get('image')
            product = Product(
                name=name,
                price=price,
                amount=amount,
                description=description,
                category=Category.objects.get(id=category_id),
            )
            product.image.save(image.name, image)
            product.save()
        return redirect('category_details', category_id)


def update_product(request, category_id, product_id):
    category = Category.objects.get(id=category_id)
    product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'shop/update_product.html',
                      {
                          'product': product,
                          'category': category,
                          'form': form
                      })
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('category_details', category_id)


def products_details(request, category_id, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product-details.html', {'product': product})


def delete_product(request, category_id, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect('category_details', category_id)
    except Product.DoesNotExist as e:
        return redirect('index')
