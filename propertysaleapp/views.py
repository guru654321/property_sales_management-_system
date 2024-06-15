from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Contact,NewPropertyData,NewPropertyTypeData,NewstatusData,ClientData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

import re




def home(request):
    return render(request,'homepage.html')

def contact(request):
     if request.method=='GET':
         return render(request,"contactpage.html")
     else:
         name=request.POST.get("contact_name")
         email=request.POST.get("contact_email")
         phone=request.POST.get("contact_phone")
         message=request.POST.get("contact_message")

         Contact(
         name=name,
         email=email,
         phone=phone,
         message=message
         ).save()
         return render(request,"contactpage.html")
def about(request):
    return render(request,'about.html')
def registration(request):
    return render(request,'register.html')

def loginpage(request):
   if request.method == 'GET':
    return render(request,'login.html')
   else:
        username1 = request.POST.get('user')
        password1 = request.POST.get('pass')
        user = authenticate(username=username1, password=password1)
        client_type =  request.POST.get('client_type')

        if user is not  None  and client_type=='Seller':
            login(request,user)
            return render(request,'dashboardpage.html')

        elif user is not  None  and client_type=='Buyer':
            login(request,user)
            return render(request,'customerdashboard.html')

        else:
            message='Invalid Credentials'

            return   render(request, 'login.html',{'message':message})

def logout_view(request):
    logout(request)
    return render(request, 'homepage.html')

def is_valid_password(password):
    import re
    pattern = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[\W_]).{8,}$')
    return bool(pattern.match(password))


@login_required(login_url='loginpage')
def clientdata(request):
    if request.method == "GET":
        return render(request, 'registrationpage.html')
    else:
        client_name = request.POST.get('client_name')
        client_login_id = request.POST.get('client_login_id')

        if not client_name or not client_login_id or client_name != client_login_id:
            return HttpResponse('Please enter the same username and login id')

        client_password = request.POST.get('client_password')
        client_confirm_password = request.POST.get('client_confirm_password')

        # Check if the password meets the criteria
        if not is_valid_password(client_password):
            message = 'Password must contain at least one letter, one digit, and one special character. It should be at least 8 characters long.'
            return render(request, 'registrationpage.html', {'message': message})

        # Check if the passwords match
        if client_password and client_confirm_password and client_password != client_confirm_password:
            return HttpResponse('Please enter the same passwords')

        # Rest of your code for processing other form fields
        client_gender = request.POST.get('client_gender')
        client_email = request.POST.get('client_email')
        client_number = request.POST.get('client_number')
        client_DOB = request.POST.get('client_DOB')
        client_address1 = request.POST.get('client_address1')
        client_address2 = request.POST.get('client_address2')
        client_city = request.POST.get('client_city')
        client_state = request.POST.get('client_state')
        client_country = request.POST.get('client_country')
        client_picture = request.FILES.get('client_picture')

        # Save the ClientData instance
        client_data = ClientData(
            client_name=client_name,
            client_login_id=client_login_id,
            client_password=client_password,
            client_confirm_password=client_confirm_password,
            client_gender=client_gender,
            client_email=client_email,
            client_number=client_number,
            client_DOB=client_DOB,
            client_address1=client_address1,
            client_address2=client_address2,
            client_city=client_city,
            client_state=client_state,
            client_country=client_country,
            client_picture=client_picture
            # ... (other fields)
        )
        client_data.save()

        # Create a user using the provided credentials
        my_user = User.objects.create_user(username=client_name, email=client_email, password=client_password)
        my_user.is_staff = True
        my_user.save()

        return render(request, 'login.html')

@login_required(login_url='loginpage')
def dashboard(request):
    return render(request,"dashboardpage.html")

@login_required(login_url='loginpage')
def afterlogin(request):
    return render(request,'navbarafterlogin.html')

@login_required(login_url='loginpage')
def new_property_data(request):
    if request.method == 'POST':
        seller_name=request.POST.get('seller-name')
        property_name = request.POST.get("property-name")
        property_type = request.POST.get("property-type")
        status_name = request.POST.get("status-name")
        property_cost = request.POST.get("property-cost")
        property_size = request.POST.get("property-size")
        seller_contact_details = request.POST.get("seller-contact-details")
        email_property = request.POST.get("email-property")
        property_amenities = request.POST.get("property-amenities")
        property_specifications = request.POST.get("property-specifications")
        property_total_rooms = request.POST.get("property-total-rooms")
        property_balcony = request.POST.get("property-balcony")
        property_total_bathrooms = request.POST.get("property-total-bathrooms")
        property_address = request.POST.get("property-address")
        property_image = request.FILES.get("property-image-upload-type")
        property_description = request.POST.get("property-description")

        new_property_data = NewPropertyData(
            seller_name=seller_name,
            property_name=property_name,
            property_type=property_type,
            status_name=status_name,
            property_cost=property_cost,
            property_size=property_size,
            seller_contact_details=seller_contact_details,
            email_property=email_property,
            property_amenities=property_amenities,
            property_specifications=property_specifications,
            property_total_rooms=property_total_rooms,
            property_balcony=property_balcony,
            property_total_bathrooms=property_total_bathrooms,
            property_address=property_address,
            property_image=property_image,
            property_description=property_description
        )
        new_property_data.save()
        return redirect('display_properties')
    else:
        return render(request, 'addnewproperty.html')
@login_required(login_url='loginpage')
def display_properties(request):
    properties = NewPropertyData.objects.filter(seller_name=request.user.username)
    return render(request, 'display_properties.html', {'properties': properties})
@login_required(login_url='loginpage')
def newpropertytype(request):
    if request.method == 'POST':
        type_name = request.POST.get("add_type_name")
        type_description = request.POST.get("add_type_description")

        if type_name and type_description:
            NewPropertyTypeData.objects.create(
                add_type_name=type_name,
                add_type_description=type_description
            )

    return render(request, 'addnewproperty_type.html')

@login_required(login_url='loginpage')
def type_report(request):
    reporttype = NewPropertyTypeData.objects.filter(seller_name=request.user)
    return render(request, "typereport.html", {'reporttype': reporttype})

@login_required(login_url='loginpage')
def edit_type(request, id):
    type_data = NewPropertyTypeData.objects.get(id=id)

    if request.method == 'POST':
        type_data.add_type_name = request.POST.get('add_type_name')
        type_data.add_type_description = request.POST.get('add_type_description')
        type_data.save()
        return redirect('type_report')

    return render(request, 'edit_type.html', {'type_data': type_data})



@login_required(login_url='loginpage')
def addstatusname(request):

    if request.method == 'POST':
        sts_name = request.POST.get("Status_name")
        sts_description = request.POST.get("Status_description")

        if sts_name and sts_description:
            NewstatusData.objects.create(
                status_name=sts_name,
                status_description=sts_description
            )

    return render(request, 'addstatus.html')

@login_required(login_url='loginpage')
def statusreports(request):
    report=NewstatusData.objects.filter(seller_name=request.user.username)
    return render(request,"statusreports.html",{'report':report})


@login_required(login_url='loginpage')
def edit_status(request, id):
    status_data =NewstatusData.objects.get(id=id)

    if request.method == 'POST':
        status_data.status_name = request.POST.get('Status_name')
        status_data.status_description = request.POST.get('Status_description')
        status_data.save()
        return redirect('statusreports')

    return render(request, 'edit_status.html', {'status_data': status_data})

def delete_status(request, id):
    status_data =NewstatusData.objects.get(id=id)

    if request.method == 'POST':
        status_data.delete()
        return redirect('statusreports')
    return render(request, 'delete_status.html', {'status_data': status_data})




def edit_property(request, id):
    edit_data = NewPropertyData.objects.get(id=id)

    if request.method == 'POST':
        # Update fields based on your model structure
        edit_data.seller_name = request.POST.get('seller-name')
        edit_data.property_name = request.POST.get('property-name')
        edit_data.property_type = request.POST.get('property-type')
        edit_data.status_name = request.POST.get('status-name')
        edit_data.property_cost = request.POST.get('property-cost')
        edit_data.property_size = request.POST.get('property-size')
        edit_data.seller_contact_details = request.POST.get('seller-contact-details')
        edit_data.email_property = request.POST.get('email-property')
        edit_data.property_amenities = request.POST.get('property-amenities', 'Default Amenities')
        edit_data.property_specifications = request.POST.get('property-specifications')
        edit_data.property_total_rooms = request.POST.get('property-total-rooms')
        edit_data.property_balcony = request.POST.get('property-balcony')
        edit_data.property_total_bathrooms = request.POST.get('property-total-bathrooms')
        edit_data.property_address = request.POST.get('property-address')
        edit_data.property_description = request.POST.get('property-description')

        # Handle property image update
        if 'property-image-upload-type' in request.FILES:
            edit_data.property_image = request.FILES['property-image-upload-type']

        # Save the updated data
        edit_data.save()


        # Redirect to the display_properties page after successful update
        return redirect('display_properties')

    return render(request, 'edit_property.html', {'property': edit_data})

@login_required(login_url='loginpage')
def delete_property(request, id):
    property_to_delete = NewPropertyData.objects.get(id=id)
    property_to_delete.delete()
    return redirect('display_properties')

@login_required(login_url='loginpage')
def delete_type(request, id):
    type_data = NewPropertyTypeData.objects.get(id=id)

    if request.method == 'POST':
        type_data.delete()
        return redirect('type_report')
    return render(request, 'delete_type.html', {'type_data': type_data})


@login_required(login_url='loginpage')
def CustomerDashboard(request):
    return render(request,"customerdashboard.html")


def all_property(request):
    allproperty_details =  NewPropertyData.objects.all()
    return render(request,'allproperty.html',{'allproperty_details':allproperty_details})

def appartment_property(request):
    appartment= NewPropertyData.objects.filter(property_type=Apartment)
    return render(request,"appartment.html",{"appartment_details":appartment_details})


def independent_floor(request):
    pass
