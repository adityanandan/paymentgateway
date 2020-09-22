from django.shortcuts import render

# Create your views here.
import razorpay
from .models import User
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

def home(request):
    if request.method== "POST":
        name = request.POST.get("name")
        amount =int(request.POST.get("amount"))* 100
        email = request.POST.get("email")
        contact=request.POST.get("contact")
        client=razorpay.Client(auth=("rzp_test_8yjMqc2GDcAc1T","YpNCO2AeQH5UaOa3k9awH1Nw"))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        user = User(name=name, amount=amount,email=email, payment_id=payment['id'])
        user.save()
        return render(request,'home.html',{'payment':payment,'username':name,'email':email,'contact':contact})
    return render(request,'home.html')

@csrf_exempt
def success(request):
    if request.method=="POST":
        a=request.POST
        order_id=""
        for key,val in a.items():
            if key == "razorpay_order_id":
                order_id=val
                break
        user = User.objects.filter(payment_id=order_id).first()
        amount=int(user.amount) / 100
        temp="your donation of :"+str(amount) +" is recieved"
        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string('email.html')

        send_mail(temp,msg_plain,settings.EMAIL_HOST_USER,
                    [user.email],html_message=msg_html)
    return render(request,'main.html')


def main(request):
    return render(request,'main.html')
