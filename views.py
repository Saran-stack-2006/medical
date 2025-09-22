from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password  # For password hashing
from django.contrib.auth import logout
from .models import Account
from django.http import JsonResponse
from django.conf import settings
from .models import OTPModel
from .models import UserProfile
from twilio.rest import Client
import random
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
import pytesseract
from PIL import Image
from django.core.files.storage import default_storage

  # <- import the function

# Create your views here.


# myapp/views.py
# myapp/urls.py
# views.py

# Your OpenAI API key
# views.py 









def send_otp(request):
    if request.method == "POST":
        mobile = request.POST.get("mobile")
        otp = str(random.randint(100000, 999999))
        
        # Save OTP
        OTPModel.objects.update_or_create(mobile=mobile, defaults={'otp': otp})
        
        # Send OTP via Twilio
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f"Your OTP is {otp}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=mobile
        )
        request.session['mobile'] = mobile
        return redirect("verify_otp")
    
    return render(request, "send_otp.html")

def verify_otp(request):
    mobile = request.session.get("mobile")
    if request.method == "POST":
        user_otp = request.POST.get("otp")
        record = OTPModel.objects.filter(mobile=mobile).first()
        if record and record.otp == user_otp:
            return redirect("main")
        else:
            return render(request, "verify_otp.html", {"error": "Invalid OTP"})
    
    return render(request, "verify_otp.html")

def main_page(request):
    return render(request, "main.html")

def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("/")



def index(request):
    return render(request, "index.html")

def diagnostic(request):
    return render(request, "diagnostic.html")

def consult(request):
    return render(request, "consult.html")

def prescription(request):
    return render(request, "prescription.html")






     # For password hashing

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        
        Account.objects.create(username=username, email=email, password=password, mobile=mobile)

        return redirect('complete_profile')  # 👈 Redirect here after signup

    return render(request, "signup.html")
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = Account.objects.filter(email=email, password=password).first()
        if user:
            return HttpResponse(f"Welcome {user.username}")
        else:
            return HttpResponse("Invalid credentials")
    return render(request, "login.html")
def complete_profile(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.address = request.POST.get('address')
        profile.health_details = request.POST.get('health_details')
        profile.preferences = request.POST.get('preferences')
        profile.save()
        return redirect('home') 
    return render(request, 'complete_profile.html')


def prolo(request):
    product = Product.objects.get(name="prolo Tablet") 
    return render(request, "prolo.html", {'product': product})
def meftal(request):
     product = Product.objects.get(name="Meftal-P Tablet")
     return render(request, "meftal.html" , {'product': product})
def Tazl(request):
     product = Product.objects.get(name="Tazloc 40 Tablet")
     return render(request, "Tazl.html", {'product': product})
def shel(request):
     product = Product.objects.get(name="Shelcal 500 Tablet")
     return render(request, "shel.html", {'product': product})
def glyco(request):
     product = Product.objects.get(name="Glycomet 250 Tablet")
     return render(request, "glyco.html", {'product': product})
def rloc(request):
    product = Product.objects.get(name="rloc Tablet")  # or filter by ID
    return render(request, "rloc.html", {'product': product})
def germer(request):
  product = Product.objects.get(name="germer Tablet")  # or filter by ID
  return render(request, "germer.html", {'product': product})
 

def otp(request):
    return render(request, "otp.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def policy(request):
    return render(request, "policy.html")

def term(request):
    return render(request, "term.html")

def wellness(request):
     return render(request, "wellness.html")

def faqs(request):
      return render(request, "faqs.html")


    
    
def policy(request):
     return render(request, "policy.html")

def site(request):
     return render(request, "site.html")

def cbc(request):
     return render(request, "cbc.html")
    
def sample1(request):
     return render(request, "sample1.html")

def cmp(request):
     return render(request, "cmp.html")
    
def lft(request):
     return render(request, "lft.html")

def profile(request):
     return render(request, "profile.html")

def kidney(request):
     return render(request, "kidney.html")

def thyoid(request):
     return render(request, "thyoid.html")

def blood(request):
     return render(request, "blood.html")
def urin(request):
     return render(request, "urin.html")

def vitamin1(request):
     return render(request, "vitamin1.html")

def vitamin2(request):
     return render(request, "vitamin2.html")

def covid(request):
     return render(request, "covid.html")
def reactive(request):
     return render(request, "reactive.html")

def discout(request):
     return render(request, "discout.html")
def deals(request):
     return render(request, "deals.html")

def deals1(request):
     return render(request, "deals1.html")

def discount1(request):
     return render(request, "discount1.html")

def referral(request):
     return render(request, "referral.html")

def myorder(request):
    return render(request, "myorder.html")


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Medicine
from .models import MedicineInfo

@csrf_exempt
def upload_prescription(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        symptoms = request.POST.get('symptoms')
        lab_test = request.POST.get('lab_test')
        file = request.FILES.get('file')

        # 🔍 You can use OCR to extract text from image (e.g., pytesseract)
        # For now, mock extracted medicines:
        extracted_meds = ['Paracetamol 500mg', 'Amoxicillin']

        medicine_list = []
        for med_name in extracted_meds:
            try:
                med_obj = MedicineInfo.objects.get(name__iexact=med_name)
                tag = "(Prescription Required)" if med_obj.requires_prescription else ""
                medicine_list.append(f"{med_name} {tag}")
            except MedicineInfo.DoesNotExist:
                medicine_list.append(f"{med_name} (Not in database)")

        data = {
            "name": name,
            "age": age,
            "symptoms": symptoms,
            "lab_test": lab_test,
            "advice": "Stay hydrated. Consult doctor if symptoms persist.",
            "medicines": medicine_list
        }
        return JsonResponse(data)

    return JsonResponse({"error": "Invalid request"}, status=400)












# Set path to the tesseract executable (important for Windows)






from .models import Product, CartItem


def medicine(request):
    return render(request, "medicine.html")


from django.shortcuts import render, get_object_or_404, redirect


def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    return render(request, 'cart.html', {'cart_items': products})
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        request.session['cart'] = cart
    return redirect('view_cart')




def pant40(request):
    product = Product.objects.get(name="Pantocid 40 Tablet")  # or filter by ID
    return render(request, 'pant40.html', {'product': product})
 # Render the search.html template






from .forms import ComplaintForm, TrackForm
from .models import Complaint

def submit_complaint(request):
    submitted = False
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = ComplaintForm()
    return render(request, 'submit_complaint.html', {'form': form, 'submitted': submitted})

def track_status(request):
    status = None
    not_found = False
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile']
            order_id = form.cleaned_data['order_id']
            try:
                complaint = Complaint.objects.get(mobile=mobile, order_id=order_id)
                status = complaint.status
            except Complaint.DoesNotExist:
                not_found = True
    else:
        form = TrackForm()
    return render(request, 'track_status.html', {'form': form, 'status': status, 'not_found': not_found})

from .forms import CallBackRequestForm
def request_callback(request):
    submitted = False
    if request.method == 'POST':
        form = CallBackRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/request_callback/?submitted=True')
    else:
        form = CallBackRequestForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'request_callback.html', {'form': form, 'submitted': submitted})




from .models import Medicine
def search_medicines(request):
    term = request.GET.get('term', '')
    results = Medicine.objects.filter(name__icontains=term).values_list('name', flat=True)[:10]
    return JsonResponse(list(results), safe=False)



from django.shortcuts import render
from .models import Category, Medicines

def filter_by_category(request, category_id=None):
    categories = Category.objects.all().distinct()  # ensure no duplicates

    if category_id:
        mediciness = Medicines.objects.filter(category_id=category_id)
        selected_category = int(category_id)
    else:
        mediciness = Medicines.objects.all()
        selected_category = None

    return render(request, 'category_filter.html', {
        'categories': categories,
        'mediciness': mediciness,
        'selected_category': selected_category
    })
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Medicines

def medicine_detail(request, medicine_id):
    medicine = get_object_or_404(Medicines, id=medicine_id)
    alternatives = []

    if not medicine.available:
        alternatives = medicine.alternatives.filter(available=True)

    return render(request, 'medicine_detail.html', {
        'medicine': medicine,
        'alternatives': alternatives
    })


# myapp/views.py

# yourapp/views.py

from django.shortcuts import render, get_object_or_404
from .models import Tablet

def tablet_detail(request, tablet_id):
    tablet = get_object_or_404(Tablet, id=tablet_id)
    return render(request, 'tablet_detail.html', {'tablet': tablet})



def tablet_list(request):
    tablets = Tablet.objects.all().order_by('id')
    return render(request, 'tablet_list.html', {'tablets': tablets})

def tablet_search(request):
    query = request.GET.get('q')
    results = Tablet.objects.filter(name__icontains=query) if query else []
    return render(request, 'tablet_search.html', {'results': results, 'query': query})

def tablet_detail(request, tablet_id):
    tablet = get_object_or_404(Tablet, id=tablet_id)

    try:
        next_tablet = Tablet.objects.filter(id__gt=tablet_id).order_by('id').first()
    except Tablet.DoesNotExist:
        next_tablet = None

    return render(request, 'tablet_detail.html', {
        'tablet': tablet,
        'next_tablet': next_tablet
    })


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})



from .models import MedicineInstru


def usage_instructions(request):
    query = request.GET.get('q')
    medicines = []     
    if query:  # If user searched something
        medicines = MedicineInstru.objects.filter(name__icontains=query)

    return render(request, 'usage_instructions.html', {
        'medicines': medicines,
        'query': query or ""  # so the search box is not empty
    })

# models.py
# views.py


from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ReportUploadForm
from .models import Report, Speciality, Doctor

def upload_report(request):
    if request.method == 'POST':
        form = ReportUploadForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()

            # Step: Check for doctor suggestion
            suggestion = None
            try:
                specialty = Speciality.objects.get(test_name__iexact=report.test_name)
                if report.test_value < specialty.min_value or report.test_value > specialty.max_value:
                    suggestion = specialty.suggested_specialist
            except Speciality.DoesNotExist:
                suggestion = None

            return render(request, 'suggest_doctor.html', {
                'report': report,
                'suggestion': suggestion,
                'doctors': Doctor.objects.filter(specialty__iexact=suggestion) if suggestion else []
            })
    else:
        form = ReportUploadForm()
    return render(request, 'upload_report.html', {'form': form})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from django.contrib import messages

def find_order(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        mobile = request.POST.get('mobile')
        try:
            order = Order.objects.get(order_id=order_id, mobile=mobile)
            return render(request, 'order_detail.html', {'order': order})
        except Order.DoesNotExist:
            messages.error(request, "Order not found.")
    return render(request, 'find_order.html')

def cancel_order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    if order.is_cancellable():
        order.status = 'Cancelled'
        order.save()
        messages.success(request, "Order cancelled successfully. Refund will be processed.")
    else:
        messages.error(request, "Order already shipped. Cannot cancel.")
    return redirect('find_order')

# views.py

from django.shortcuts import render, redirect
from django.urls import reverse
import random
import string
from .models import Order
from django.views.decorators.csrf import csrf_exempt

def generate_order_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

@csrf_exempt
def buy_now(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        mobile = request.POST.get('mobile')
        product = request.POST.get('product')
        amount = request.POST.get('amount')

        order = Order.objects.create(
            order_id=generate_order_id(),
            customer_name=customer_name,
            mobile=mobile,
            product=product,
            amount=amount,
            status='Pending'
        )

        return redirect('order_success', order_id=order.order_id)  # 🛠️ Pass order_id here

    return render(request, 'buy_now_form.html')

def order_success(request, order_id):
    order = Order.objects.get(order_id=order_id)
    return render(request, 'order_success.html', {'order': order})
def himala(request):
    return render(request, 'himala.html')
def dabur(request):
    return render(request, 'dabur.html') 
def cofsils(request):
    return render(request, 'cofsils.html') 
def Koflet(request):
    return render(request, 'Koflet.html') 
def sara(request):
    return render(request, 'sara.html') 
def saran(request):
    return render(request, 'saran.html') 
def drops(request):
    return render(request, 'drops.html') 
def choles(request):
    return render(request, 'choles.html') 