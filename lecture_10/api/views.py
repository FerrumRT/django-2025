from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import ProductSerializer
from shop.models import Product


# Create your views here.
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response("Product doesn't exist", status=404)

    if request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        product.delete()
        return Response("Product deleted", status=204)

    serializer = ProductSerializer(product)
    return Response(serializer.data, status=200)
