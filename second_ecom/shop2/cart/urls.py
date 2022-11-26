from django.urls import path
from .import views

app_name = 'cart'

urlpatterns=[
    path('add/<int:pro_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detial,name='cart_detials'),
    path('remove/<int:pro_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:pro_id>/', views.delete, name='delete')

]
