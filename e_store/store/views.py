from django.shortcuts import render
from .models import Product


# Create your views here.

def catalog(request):
    if 'cart' not in request.session:
        request.session['cart'] = []

    cart = request.session['cart']
    request.session.set_expiry(0)  # session does not expire unless browser is closed
    store_items = Product.objects.all()
    context = {'store_items': store_items, 'cart_items': len(cart)}
    return render(request, 'catalog.html', context)
