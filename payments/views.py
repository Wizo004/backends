from django.shortcuts import render, redirect
from .models import Payment
def payments(request):
    return render(request, 'payments/payments.html')


def payment_capture(request):
    if request.method == "POST":
        name                  = request.POST['name']
        id_number             = request.POST['id_number']
        phone_number          = request.POST['phone_number']
        amount                = request.POST['amount']
        pay_type              = request.POST['pay_type']
        transaction_code      = request.POST['transaction_code']

        payment = Payment(name=name, id_number=id_number, phone_number=phone_number, amount=amount,transaction_code=transaction_code, pay_type=pay_type)
        payment.save()

        return redirect('payments:payments')


    return render(request, 'payments/payments.html')


def payment_fetch(request):
    payment = Payment.objects.all()
    return render(request,'payments/payments.html',{'payments':payment})


def payment_edit(request, id):
    if request.method == "POST":
        name                  = request.POST['name']
        id_number             = request.POST['id_number']
        phone_number          = request.POST['phone_number']
        amount                = request.POST['amount']
        pay_type              = request.POST['pay_type']
        transaction_code      = request.POST['transaction_code']

        payment = Payment.objects.get(id=id)

        payment.name = name
        payment.id_number = id_number
        payment.phone_number = phone_number
        payment.amount = amount
        payment.pay_type = pay_type
        payment.transaction_code = transaction_code

        payment.save()

        payment = Payment.objects.get(id=id)
    return render(request, 'payments/payments.html', {'payments':payment})
