from django.shortcuts import render, get_object_or_404 
from .models import Product
from cart.forms	import	CartAddProductForm
# Create your views here.

def products(request):
	products = Product.objects.all()
	cart_product_form = CartAddProductForm()
	return render(request, 'burgerkingapp/product/products.html',
	              {
	              'products':products,
                'cart_product_form':  cart_product_form
	              }
	              )

def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id,
                                available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'burgerkingapp/product/detail.html',
                  {
                  'product': product,
                  'cart_product_form':	cart_product_form
                  })