from django.db.models import query
from django.shortcuts import render , redirect
from django.urls import reverse
from .models import *
from django.core.exceptions import MultipleObjectsReturned
from django.views import generic
from django.db import IntegrityError

# Create your views here.

def landing(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
    return render(request , 'landing.html')


def submitted(request):
    return render(request , 'submitted.html')


def index(request):
    client = Client.objects.all()
    client_view = Client.objects.all()
    project = Project.objects.all()
    billing_con = Billing.objects.all()
    billing = Billing.objects.all()
    alert =''
    ######################################## Getting User Input Start
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        transaction_id = request.POST['transaction_id']
        transaction_id = transaction_id.upper()
        invoice_no = request.POST['invoice_no']
        invoice_no = invoice_no.upper()
        age = request.POST['age']
        billing_user = request.POST['billing']
        project_user = request.POST['project']
        ######################################## Getting User Input End
        ######################################## Standarize Phone Number Start
        if phone.startswith('+'):
            phone = phone
        elif phone.startswith('88'): 
            phone = phone.split()  
            phone.append('+') 
            phone = phone[1] + phone[0]      
         
        elif phone.startswith('01'): 
            phone = phone.split()  
            phone.append('+88') 
            phone = phone[1] + phone[0]   
        else:
            alert = 'Wrong Number Format'    
        ######################################## Standarize Phone Number End
        if len(phone) == 14:  ########## Number Length Check 
            if alert == 'Wrong Number Format':
                pass
            else:
                try: ############# Check If User Exixts
                    clients = Client.objects.get(phone = phone)
                    # clients = Client.objects.get(first_name = first_name , last_name = last_name , age=age , phone = phone)
                    alert = "Existing User; Please Select From The Drop Down List"
                except:
                    client = Client (
                        first_name=first_name ,
                        last_name=last_name, 
                        phone = phone ,
                        age=age , 
                        billing= Billing.objects.get(type=billing_user) ,
                        project= Project.objects.get(name=project_user)
                        )
                    try:  ###################### Check If Transaction Id and Invoice is Unique
                        client.save()
                        account = Account (
                        billing = Billing.objects.get(type=billing_user) ,
                        client = Client.objects.get(phone = phone),
                        transaction_id = transaction_id,
                        invoice_no = invoice_no,
                        type = PaymentType.objects.get(id=1),
                            )
                        account.save()
                        return redirect('/submitted/')
                    except IntegrityError:
                        client = Client.objects.get(phone = phone)
                        client.delete()
                        alert = "Transaction and Invoice Must Be Unique" 
        else:
               alert = 'Number Error Must Be 11 Digits Except (+880)'             
    context = {
        'projects' : project,
        'billings' : billing_con , 
        'clients' : client_view,
        'alert' : alert,

    }
    return render(request , 'index.html' , context)


def UpdateExist(request , pk):
    ################### Initiraizing Context Data Start ##########################
    project = Project.objects.all()
    payment = PaymentType.objects.all()
    billing_con = Billing.objects.all()
    client = Client.objects.get(id=pk)
    first_name = client.first_name
    last_name = client.last_name
    project_user = client.project
    age = client.age
    phone = client.phone
    ################### Initiraizing Context Data End ##########################
    accounts = client.client.filter(client=client) ############### Getting Client Account Set
    if request.method == 'POST':
        ######################################## Getting User Input Start
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        billing_user = request.POST['billing']
        project_user = request.POST['project']
        payment_user = request.POST['payment']
        transaction_id = request.POST['transaction_id']
        transaction_id = transaction_id.upper() ############## Standarizing User Input to Uppercase
        invoice_no = request.POST['invoice_no']
        invoice_no = invoice_no.upper()  ############## Standarizing User Input to Uppercase
        ######################################## Getting User Input End
        account = Account (
                billing = Billing.objects.get(type=billing_user) ,
                client = Client.objects.get(id=pk),
                transaction_id = transaction_id,
                invoice_no = invoice_no,
                type = PaymentType.objects.get(name=payment_user)
        )
        account.save()
        return redirect('my_app:excli' , pk = pk) ################### Redirecting User with parameter
    context ={
        'first_name' : first_name,
        'last_name' : last_name,
        'age' : age,
        'projects' : project,
        'billings' : billing_con , 
        'project_user': project_user ,
        'phone' : phone,
        'payments' : payment,
        'accounts' : accounts,

    }
    return render(request , 'excli.html' , context)




############################ Existing User Search Function #########################
def Ex_User(request):
    if request.method == 'POST':
        value = request.POST['srcho']
        value = value.split(' ')
        value = value[3]
        client = Client.objects.get(phone = value)
        pk = client.id
        return redirect('my_app:excli' , pk = pk)
############################ Existing User Search Function #########################