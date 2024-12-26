from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer, CommentSerializer
from .other_classes import Comment

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True)
        context = {
            'products': serialized_products.data
        }
        return Response(context)

    elif request.method == 'POST':
        serialized_product = ProductSerializer(data=request.data)
        if serialized_product.is_valid():
            serialized_product.save()  # Save the new product
            return Response(serialized_product.data, status=status.HTTP_201_CREATED)
        return Response(serialized_product.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def comment_list_view(request):
    comment = Comment('arefin@gmail.com', 'This is very good product')
    serialized_comment = CommentSerializer(comment)
    return Response(serialized_comment.data)