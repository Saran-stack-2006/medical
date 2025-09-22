
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views 
from .views import upload_prescription # Import the entire views module
# Import views from myapp

urlpatterns = [
    # myapp/urls.py


    path('upload/', upload_prescription, name='upload_prescription'),    # ... other urls ...
    path('tablets/', views.tablet_list, name='tablet_list'),
path('search/', views.tablet_search, name='tablet_search'),
    path('upload/', upload_prescription, name='upload_prescription'),
path('medicine/<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),
    path('tablet/<int:tablet_id>/', views.tablet_detail, name='tablet_detail'),
 path('filter_by_category/', views.filter_by_category, name='all_medicines'),
    path('medicines/category/<int:category_id>/', views.filter_by_category, name='filter_by_category'),
    path("home/", views.home, name="home"),
     path("prolo/", views.prolo, name="prolo"),
     path("Tazl/", views.Tazl, name="Tazl"),
     path("shel/", views.shel, name="shel"),
     path("glyco/", views.glyco, name="glyco"),
    path('send_otp/', views.send_otp, name='send_otp'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path("rloc/", views.rloc, name="rloc"),
    path("meftal/", views.meftal, name="meftal"),
     path("germer/", views.germer, name="germer"),
    path('main/', views.main_page, name='main'),
    path("logout/", views.logout_view, name="logout"),
     path('complete-profile/', views.complete_profile, name='complete_profile'),
     path("pant40/", views.pant40, name="pant40"),
    path("index/", views.index, name="index"),
    path("diagnostic/", views.diagnostic, name="diagnostic"),
    path("consult/", views.consult, name="consult"),
    path("prescription/", views.prescription, name="prescription"),
     path("otp/", views.otp, name="otp"),
     path("signup/", views.signup, name="signup"),  # Correct URL pattern
       path("login/", views.login, name="login"),
       path("about/", views.about, name="about"),
       path("contact/", views.contact, name="contact"),
       path("policy/", views.policy, name="policy"),
       path("medicine/", views.medicine, name="medicine"),
        path("policy/", views.policy, name="policy"),
       path("term/", views.term, name="term"),
       path("faqs/", views.faqs, name="faqs"),
       path("wellness/", views.wellness, name="wellness"),
        path("site/", views.site, name="site"),
        path("cbc/", views.cbc, name="cbc"),
        path("sample1/", views.sample1, name="sample1"),
         path("cmp/", views.cmp, name="cmp"),
          path("lft/", views.lft, name="lft"),
           path("profile/", views.profile, name="profile"),
            path("kidney/", views.kidney, name="kidney"),
             path("thyoid/", views.thyoid, name="thyoid"),
               path("blood/", views.blood, name="blood"),
               path("urin/", views.urin, name="urin"),
               path("vitamin1/", views.vitamin1, name="vitamin1"),
               path('myorder/', views.myorder, name='myorder'),
 path("vitamin2/", views.vitamin2, name="vitamin2"),
 path("covid/", views.covid, name="covid"),
 path("reactive/", views.reactive, name="reactive"),
 path("discout/", views.discout, name="discout"),
 path("deals/", views.deals, name="deals"),
 path("discount1/", views.discount1, name="discount1"),
 path("deals1/", views.deals1, name="deals1"),
 path("referral/", views.referral, name="referral"),
path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
 path('submit/', views.submit_complaint, name='submit_complaint'),
    path('track/', views.track_status, name='track_status'),
    path('request_callback/', views.request_callback, name='request_callback'),
    path('instructions/', views.usage_instructions, name='usage_instructions'),
       path('upload/', views.upload_report, name='upload_report'),
    path('reports/', views.upload_report, name='view_reports'),
   path('search/', views.search_medicines, name='search_medicines'),
    path('buy-now/', views.buy_now, name='buy_now'),
path('order-success/<str:order_id>/', views.order_success, name='order_success'),
 path('buy/', views.buy_now, name='buy_now_form'),
 path('find-order/', views.find_order, name='find_order'),
 path('himala/', views.himala, name='himala'),
path('dabur/', views.dabur, name='dabur'),
path('cofsils/', views.cofsils, name='cofsils'),
path('Koflet/', views.Koflet, name='Koflet'),
path('sara/', views.sara, name='sara'),
path('saran/', views.saran, name='saran'),
path('drops/', views.drops, name='drops'),
path('choles/', views.choles, name='choles'),
 path('cancel/<str:order_id>/', views.cancel_order, name='cancel_order'),
  

]




if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
