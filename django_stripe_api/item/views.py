from django.shortcuts import render, get_object_or_404, redirect

from django_stripe_api.settings import STRIPE_PUBLIC_KEY
from item.models import Item


def show_item(request, pk):
    context = {
        'item': get_object_or_404(klass=Item, pk=pk),
        'public_key': STRIPE_PUBLIC_KEY
    }
    return render(request, 'item/index.html', context)


def redirect_to_first_item(request):
    return redirect('item/1')
