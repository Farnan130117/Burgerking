from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm
import math
from decimal import Decimal
from django.http import HttpResponse

def order_create(request): #order processing
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			#form.instance.first_name='test' #important 
			deposit_amount = form.instance.deposit_amount
			if deposit_amount >= cart.get_total_price():
				discount       = form.instance.discount #submitted discount value
				discount_f     =  math.floor( ( Decimal(cart.get_total_price()) ) * ( Decimal(discount)/Decimal(100) ) ) #percentage calculation
				print(discount_f ) 
				total = cart.get_total_price() - discount_f #Subtract discount amount from total order amount
				form.instance.paid_amount= total

				form.instance.return_amount= deposit_amount- total
				amount_return=form.instance.return_amount
				#getting submitted data from formdata to function 
				order = form.save()
				#total = cart.get_total_price();
				#amount=1000;
				#amount_return=amount-total;
			
				for item in cart:
					OrderItem.objects.create(order=order,
										 product=item['product'],
										 price=item['price'],
										 quantity=item['quantity'])
				# clear the cart
				cart.clear()

				return render(request,
						  'orders/order/created.html',
						  {
						   'order': order,
						   'total':total,
						   'amount_return':amount_return,
							})
			else:
				form = OrderCreateForm()
				return HttpResponse("""<h2> Wrong Input <a href="/orders/create/"> Fill Again</a>""")

			
	else:
		form = OrderCreateForm()
	return render(request,
				  'orders/order/create.html',
				  {'cart': cart, 'form': form})
