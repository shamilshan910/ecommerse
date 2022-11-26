from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.AllProCat,name='AllProCat'),
    path('<slug:c_slug>/',views.AllProCat,name='Prod_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProDet, name='ProDet')

]
