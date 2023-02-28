from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view


# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    # It retrieves all objects from database
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    
    
class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    

# @api_view
# def menu_items(request):
#     items = MenuItem.objects.all()