from django.shortcuts import render
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
    products = Product.objects.all()
    serialized_products = ProductSerializer(products, many=True)
    context = {
        'products': serialized_products.data
    }
    return Response(context)


def comment_list_view(request):
    comment = Comment('arefin@gmail.com', 'This is very good product')
    serialized_comment = CommentSerializer(comment, many=True)
    return Response(serialized_comment.data)