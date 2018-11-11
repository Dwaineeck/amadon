from django.shortcuts import render, redirect
from decimal import Decimal as D
items = {'p1': 19.99 + (19.99 * 0.0825),
		 'p2': 24.99 + (24.99 * 0.0825),
		 'p3': 8.50 + (8.50 * 0.0825),
		 'p4': 49.99 + (49.99 * 0.0825)
}

def index(request):
	return render(request, 'index.html')

def buy(request):
	request.session['purchase'] = items[request.POST['product_id']] * int(request.POST['quantity'])

	if 'item_count' not in request.session:
		request.session['item_count'] = 0
	if 'total_spent' not in request.session:
		request.session['total_spent'] = 0

	request.session['item_count'] += int(request.POST['quantity'])
	request.session['total_spent'] += float(request.session['purchase'])
	return redirect('/checkout')

def checkout(request):
	return render(request, 'checkout.html')

def clear(request):
	request.session.clear()
	return redirect('/')