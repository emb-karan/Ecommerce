from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import Cart, Profile, product, UserRole , Order, comment_buyer 
from django.contrib import messages
import requests
from .forms import Login_user, Product
from django.views.generic import UpdateView, ListView
from django.urls import reverse
from django.views.generic.edit import DeleteView
# from Project_1.models import product
from django.views.generic import UpdateView
from django import forms


# Create your views here.
def home(request):
    return redirect(reverse("home"))


def signup_User(request):
    if request.method == "POST":

        email = request.POST['email']
        pwd = request.POST['pwd']
        firstname = request.POST['fn']
        lastname = request.POST['ln']
        # u=User(username=Un, password=make_password(pwd), email=email,first_name=firstname,last_name=lastname)
        u = User(username=email, password=make_password(pwd), first_name=firstname, last_name=lastname)
        u.save()
        mobile = request.POST['mobile']
        role = request.POST['role']

        user_role = UserRole(user=u, mobile=mobile, role=role)
        user_role.save()
        return redirect(reverse("login_user"))
    return render(request, "signup.html")


def login_user(request):
    if request.method == "POST":
        un = request.POST["email"]
        pwd = request.POST["pwd"]
        print(un, pwd)
        user = authenticate(username=un, password=pwd)
        print(user)

        if user:
            login(request, user)
            # return  render (request, 'index.html')
            # return redirect('/index/')
            uObj = UserRole.objects.get(user__username=request.user)
            if uObj.role == 'seller':
                return redirect(reverse("sellerhome"))
            elif uObj.role == 'buyer':
                return redirect(reverse("buyer_home"))
    return render(request, "login.html")


def homebuyer(request):
    product_1 = product.objects.all()

    return render(request, "welBuyer.html", {'product': product_1})


def homeseller(request):
    prod = product.objects.filter(user_name_id=request.user.id)

    return render(request, "welsell.html", {'product': prod})


def add_product(request):
    form = Product(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect('/add_product/')

    return render(request, "product2.html", {'form': form})


def buyer_cart(request):
    form = Cart(request.POST or None)
    

    if request.method == "POST":
        catid = request.POST['catId']

        print(catid)

        if form.is_valid():
            form.save()
            return redirect('/buyer_cart/')
        
    

    return render(request, "buyer_cart.html", {'form': form})

def profile_user(request):

    if request.method == "POST":
        nick_N = request.POST.get('nick_name')
        Adhaar = request.POST.get('addhar_no')
        birth_date = request.POST.get('birthdaytime')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        state = request.POST.get('state')
        Address = request.POST.get('Address')
        p = Profile(profile_id=request.user, Nnikename=nick_N,
                    Adhaar_card_No=int(Adhaar), Birth_Date=birth_date, address = Address, city = city , state = state )
        p.save()

    return render(request, "profile.html")

def updateprofile(request):
    upObj = Profile.objects.filter(profile_id_id=request.user.id)	
    uObj = User.objects.filter(id = request.user.id)
    if request.method == 'POST':
        nick_N = request.POST.get('nick_name')
        Adhaar = request.POST.get('addhar_no')
        birth_date = request.POST.get('birthdaytime')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        state = request.POST.get('state')
        Address = request.POST.get('Address')
        first1=request.POST.get('firstname')
        last1=request.POST.get('lastname')

        current_user = request.user
        user_id = current_user.id


        upObj.update(profile_id=request.user, Nnikename=nick_N,Adhaar_card_No=int(Adhaar), Birth_Date=birth_date, address = Address, city = city , state = state , pincode=pincode)

        uObj.update(first_name=first1,last_name=last1)
        return redirect(reverse("next_user"))
        
    return render(request,"update_profile.html",{'upObj':upObj,'uObj':uObj})                    


def next(request):

    upObj = Profile.objects.filter(profile_id=request.user)

    return render(request, "next.html", {'upObj': upObj})


def logout_user(request):
    logout(request)
    return redirect('/login_user/')


class ProductUpdateview(UpdateView):
    template_name = 'savetemplate.html'
    fields = ['id', 'Product_No', 'Product_Price', 'Descreption', 'comment']
    model = product
    success_url = "/homeseller/"  # posts list url


class ProductDeleteView(DeleteView):
    template_name = 'delte_product.html'
    model = product
    success_url = "/homeseller/"



def cart_save(request):
    # upObj = Profile.objects.filter(profile_id=request.user)
    upObj = Cart.objects.filter(user_id=request.user)


    if request.method == 'POST':
        pname = request.POST.get('Product_Name')
        pno = request.POST.get('Product_No')
        pprice = request.POST.get('Product_Price')
        desc = request.POST.get('Descreption')
        pid = request.POST.get('id')
        a=product.objects.filter(id=pid)
        print(a)
        for i in a:
            a=i.quantity
            print(i.quantity)
            b=Cart.objects.all()
            for x in b:
                c=x.id
                print(c)
                d=Order.objects.filter(cart=c)

                

            # order = Order.objects.filter(cart_id=)



        # print(" hello i am a Quantity   ",a.quantity)
        u = Cart(product_name=pname, order_price =pno , descreption = desc ,product_id=pid,user_id = request.user.id)
        u.save()
        print("Save Good")
    return render(request, "cart.html",{'upObj':upObj})
    

def delcart(request,id):
    print("i am a ID ",id)

   
     
    # upObj = Cart.objects.filter(user_id=request.user.id, product = id)
    upObj = Cart.objects.filter(id=id)
    print("i am a UpObj", upObj)

    upObj.delete()
    # return render(request, "homebuyer")
    return redirect(reverse("cart_save1"))
    # return redirect(reverse("buyer_home"))

def order_now(request,cart_id):
    print("i am a cart ID", cart_id )
    order = Order(cart_id = cart_id  ,user_id =request.user.id  )
    order.save()


    upObj = Cart.objects.filter(id=cart_id)
    userD = User.objects.filter(id = request.user.id  )


    return render(request,"order.html" ,{'upObj':upObj,'userD':userD})

def order_view(request):
    # uObj = UserProile.objects.get(user__username = request.user)
	# obj = Book.objects.filter(placedby_id=uObj.id)

    userD=User.objects.get(id = request.user.id)
    profile_b = Profile.objects.filter(profile_id_id = request.user.id)


   
    # upObj = Cart.objects.filter(user_id=userD.id)
    orderl = Order.objects.filter(user_id =userD.id)

    # order_u = Order.objects.filter(user_id =request.user.id )

    # order = Order(cart_id = cart_id  ,user_id =request.user.id  )
    return render(request,"order_view.html",{'orderl':orderl,'profile_b':profile_b})

def order_del(request,id):
    upObj = Order.objects.filter(id=id)
    upObj.delete()
    return redirect(reverse("order_see"))



         
    

def commentbuyer(request):

    if request.method == "POST":
        comment = request.POST.get('comment1')
        product_id = request.POST.get('product_id')

        # print("I am a comment ",comment , " i am a product_id",product_id , request.user.id)

        c = comment_buyer(comment=comment,product_id=product_id,user_id =request.user.id )
        c.save()
        com = comment_buyer.objects.filter(product_id=product_id)
        product_1 = product.objects.all()
        print("I am a c ",c)
        print("Iam a com",com)

        return redirect(reverse("commentsee"))
        


    # return redirect(reverse("buyer_home"))

    
def commentsee(request):
    # userD=User.objects.get(id = request.user.id)
    prod = product.objects.filter()
    # prod = product.objects.all()
    # comm = comment_buyer.objects.filter(product_id=prod.id)
    a = product.objects.all()
    return render(request, "comment.html", {'a':a})


    # com = comment_buyer.objects.filter()

    


def login_user2(request):
    if request.method == "POST":
        fm = Login_user(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data['email_user']
            password2 = fm.cleaned_data['password_user']

            print(email,password2)
            user2 = authenticate(username=email, password=password2)
            print(user2)
            if user2:
                login(request,user2)
               
                return redirect('/index/')
            else:
                raise forms.ValidationError("Email or Password is incorrect")
                # raise forms.ValidationError("You have forgotten about Fred!")
                # return Login_user()
    else:
        fm=Login_user()
    return render(request,"login2.html",{'form':fm})
    







    










