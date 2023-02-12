from order.models import Order


def get_or_create_order(session_key):
    order = Order.objects.filter(session_key=session_key)[0]
    if not order:
        order = Order.objects.create(session_key=session_key)[0]
    return order
