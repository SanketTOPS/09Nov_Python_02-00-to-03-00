from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
import razorpay
import json
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def payment_page(request):
    """Render a simple payment page where user can enter amount."""
    return render(request, 'payments/pay.html', {
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
    })

def create_order(request):
    """Create a Razorpay order and return the order_id as JSON.
    Expected GET param: amount (in rupees). Razorpay expects amount in paise.
    """
    amount_rupees = request.GET.get('amount')
    if not amount_rupees:
        return HttpResponseBadRequest('Missing amount')
    try:
        amount = int(float(amount_rupees) * 100)  # convert to paise
    except ValueError:
        return HttpResponseBadRequest('Invalid amount')
    data = {
        'amount': amount,
        'currency': 'INR',
        'payment_capture': 1,
    }
    order = client.order.create(data=data)
    return JsonResponse({'order_id': order['id'], 'amount': amount, 'currency': 'INR'})

def verify_payment(request):
    """Verify Razorpay payment signature.
    Expects POST JSON with razorpay_order_id, razorpay_payment_id, razorpay_signature.
    """
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid method')
    try:
        payload = json.loads(request.body)
        razorpay_order_id = payload['razorpay_order_id']
        razorpay_payment_id = payload['razorpay_payment_id']
        razorpay_signature = payload['razorpay_signature']
    except (KeyError, json.JSONDecodeError):
        return HttpResponseBadRequest('Invalid payload')
    try:
        client.utility.verify_payment_signature({
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature,
        })
    except razorpay.errors.SignatureVerificationError:
        return JsonResponse({'status': 'failure'}, status=400)
    return JsonResponse({'status': 'success'})
