from django.shortcuts import render,redirect
from .models import *

def dashboard(request):
    return render(request,'Dashboard.html')

def products(request):
    return render(request,'Products.html')

def companies(request):
    procompany=ProductCompany.objects.all()
    return render(request,'company.html',{'procompany':procompany})

def product_company_add(request):
     if request.method=="POST":
        pcomp_name=request.POST['pcname']
        pcomp_img=request.FILES.get('pclogo')

 #saving data

        procomp=ProductCompany(pro_comp_name=pcomp_name,pro_comp_logo=pcomp_img)

        procomp.save()
        message="Successfuly Data Saved"
        procompany=ProductCompany.objects.all()
        return render(request,'company.html',{'procompany':procompany,'message':message})


def our_products(request):
    company_names=ProductCompany.objects.all()
    return render(request,'our_products.html',{'company_names':company_names})

def product_add(request):
    if request.method=="POST":
        pro_name=request.POST['pro_name']
        pro_comp=request.POST['com_name']
        pro_price=request.POST['pro_price']
        pro_detail=request.POST['pro_discr']
        pro_img=request.FILES.get('pro_img')

 #saving data

        pro=Products(product_name=pro_name,product_company=pro_comp,product_price=pro_price,product_details=pro_detail,product_img=pro_img)

        pro.save()
        message="Successfuly Data Saved"
        company_names=ProductCompany.objects.all()
        return render(request,'our_products.html',{'company_names':company_names,'message':message})

def productslist(request):
    productlist=Products.objects.all()
    return render(request,'productlist.html',{'productlist':productlist})

def clients(request):
    clients_details=ClientsCompany.objects.all()
    return render(request,'Clients.html',{'clients_details':clients_details})

def client_add(request):
   if request.method=="POST":
        client_name=request.POST['clientcomp_name']
        status=request.POST['work_stauts']

        if(status=="0"):
            w_status='Ongoing Works'
        else:
             w_status='Finished Works'
        logo=request.FILES.get('comp_logo')

 #saving data

        clients=ClientsCompany(clientcomp_name=client_name,Work_status=w_status,comp_logo=logo)

        clients.save()
        message="Successfuly Data Saved"
        clients_details=ClientsCompany.objects.all()
        return render(request,'Clients.html',{'clients_details':clients_details,'message':message})


def services(request):
    services=Services.objects.all()
    return render(request,'services.html',{'services':services})

def services_add(request):
   if request.method=="POST":
        ser_name=request.POST['service_name']
        ser_content=request.POST['service_content']
        ser_img=request.FILES.get('service_imge')

 #saving data

        services=Services(service_name=ser_name,service_content=ser_content,service_img=ser_img)

        services.save()
        return redirect('services')

def internship(request):
    college=Colleges.objects.all()
    return render(request,'Internships.html',{'college':college})

def college_add(request):
    if request.method=="POST":
        college_name=request.POST['college_name']

 #saving data

        college=Colleges(college_names=college_name)

        college.save()
        return redirect('internship')
    

def gallery(request):
    return render(request,'Gallery.html')

def new_finised_works(request):
    allworks=Works.objects.all() 
    return render(request,'new_finished.html',{'allworks':allworks,})


def works_add(request):
    if request.method=="POST":
        w_category=request.POST['work_category']
        w_disc=request.POST['work_disc']
        status=request.POST['work_status']

        if(status=="0"):
            wk_status='New Works'
        elif(status=="1"):
             wk_status='Ongoing Works'
        else:
            wk_status="Finished Works"

        w_img=request.FILES.get('work_img')

 #saving data

        work=Works(w_category=w_category,w_status=wk_status,w_details=w_disc,w_img=w_img)

        work.save()
        message="Successfuly Data Saved"
        allworks=Works.objects.all()
        return render(request,'new_finished.html',{'allworks':allworks,'message':message})

def ongoing_works(request):
    allworks=Works.objects.filter(w_status='Ongoing Works')
    return render(request,'ongoingworks.html',{'allworks':allworks})

def workupdate(request,work_id):
    works=Works.objects.get(id=work_id)
    return render(request,'ongoingworks.html',{'works':works})