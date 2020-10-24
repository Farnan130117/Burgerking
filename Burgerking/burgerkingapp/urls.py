from django.urls import path
from . import views

app_name = 'burgerkingapp'

urlpatterns = [
	#path('',views.home,name='home'),
	path('',views.products,name='products'),  #viewing all products
	path('<int:id>', views.product_detail, name='product_detail'),
]