from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns =[  path('',views.dashboard,name='dashboard'),
                path('products',views.products,name='products'),
                path('companies',views.companies,name='companies'),
                path('product_company_add',views.product_company_add,name='product_company_add'),
                path('our_products',views.our_products,name='our_products'),
                path('product_add',views.product_add,name='product_add'),
                path('productslist',views.productslist,name='productslist'),


                path('clients',views.clients,name='clients'),
                path('client_add',views.client_add,name='client_add'),

                path('internship',views.internship,name='internship'),
                path('college_add',views.college_add,name='college_add'),


                path('services',views.services,name='services'),
                path('services_add',views.services_add,name='services_add'),

                path('gallery',views.gallery,name='gallery'),

                path('new_finised_works',views.new_finised_works,name='new_finised_works'),
                path('works_add',views.works_add,name='works_add'),
                path('ongoing_works',views.ongoing_works,name='ongoing_works'),
                path('workupdate/<int:work_id>',views.workupdate,name='workupdate'),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)