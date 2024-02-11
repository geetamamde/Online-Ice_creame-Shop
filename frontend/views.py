from django.shortcuts import render,redirect
from backend.models import Ice_creame,Category,payment
from frontend.models import userinfo, mycart, OrderMaster,Contact_info
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def home(request):
    icey = Category.objects.all()
    creame = Ice_creame.objects.all() 
    return render(request,"base1.html",{'icey':icey ,'creame':creame})

def showice(request,id):
    icey = Category.objects.all()
    creame = Ice_creame.objects.filter(cate = id)
    return render(request,"base1.html",{'icey':icey ,'creame':creame}) 

def viewdetails(request,id):
    icey = Category.objects.all()
    creame = Ice_creame.objects.filter (id = id)
    return render(request,"viewdetails.html",{'icey':icey ,'creame':creame})


def login(request):
    if(request.method == "GET"):
        return render (request,"login.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]

        try:
            user = userinfo.objects.get( username= uname , password = pwd)
            
        except:
             message = "Invalid Credentials,Plz try again!!"
             return render(request,"login.html",{"message":message})
        else:
            request.session["uname"] = uname
            return redirect(home)
            

def signup(request):
  if(request.method == "GET"):
      return render(request,"signup.html",{})
  else:
      uname = request.POST['uname']
      fname = request.POST['fname']
      pwd   = request.POST['pwd']
      email = request.POST['email']
      phone = request.POST['phone']
      try:
            user = userinfo.objects.get(username=uname)
      except:
            user = userinfo(username=uname, fname=fname,password=pwd, email=email, phone=phone)
            user.save()
            return redirect(home)
      else:
          message = "This User already exist"
          return render(request,"signup.html",{'message':message})
      
def signout(request):
    request.session.clear()
    return redirect(home)

def tocart(request):
     
    if('uname' in request.session):
        user = userinfo.objects.get(username=request.session['uname'])
        cre_id = request.POST['cid']
        ice_creame = Ice_creame.objects.get(id=cre_id)
        qty = request.POST['qty']
        try:
          item = mycart.objects.get(user=user,ice_creame=ice_creame)
        except:
            cart = mycart()
            cart.user = user
            cart.ice_creame = ice_creame 
            cart.qty = qty
            cart.save()
            messages.info(request, 'Item added successfully')
            
        else:
           messages.info(request, 'Item already in cart')
        return redirect(showcart)
   
     
    else:
         return redirect(login)
     
def showcart(request):
    icey = Category.objects.all()
    if (request.method == "GET"):
        items = mycart.objects.filter(user = request.session['uname'])
        total = 0
        for item in items:
            total += item.qty*item.ice_creame.price
        request.session["total"] = total
        return render(request,"showcart.html",{'items':items ,'icey':icey})
    
    else:
        cart_id = request.POST["cart_id"]
        item = mycart.objects.get(id=cart_id)
        action = request.POST["action"]
        if (action == "remove"):
            item.delete()
        else:
            qty = request.POST["qty"]
            item.qty = qty
            item.save()
        return redirect(showcart)

def MakePayment(request):
    if(request.method == "GET"):
        return render(request,"MakePayment.html",{}) 

    else:
        card_no = request.POST['card_no']
        cvv = request.POST['cvv']
        expiry = request.POST['expiry']
        try:
            buyer = payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry)
        
        except:
            return redirect(MakePayment)
        
        else:
            owner = payment.objects.get(card_no='owner',cvv='123',expiry='12/26')
            buyer.balance -= float(request.session['total'])
            owner.balance += float(request.session['total'])
            buyer.save()
            owner.save()

            myorder = OrderMaster()
            user = userinfo.objects.get(username=request.session['uname'])
            myorder.user  = user
            myorder.amount = request.session['total']
            items = mycart.objects.filter(user=user)
            details = " "
            for item in items:
                 details += item.ice_creame.chillin_name + " "
                 item.delete()

            myorder.details= details
            myorder.save()

            return redirect(thank)

def base1(request):
    icey = Category.objects.all()
    creame = Ice_creame.objects.all() 
    return render(request,"base1.html",{'icey':icey ,'creame':creame})

def viewde1(request,id):
    icey = Category.objects.all()
    creame = Ice_creame.objects.filter(id=id)
    return render (request,"viewde1.html",{'icey':icey ,'creame':creame})



def contact(request):
    icey = Category.objects.all()
    if(request.method == "GET"):
        return render(request,"contact.html",{"icey":icey}) 
    else:
        try:
            contact_info = Contact_info()
            first = request.POST['firstname']
            contact_info.firstname = first
            contact_info.save()

            last = request.POST['lastname']
            contact_info. lastname = last
            contact_info.save()
            
            coun = request.POST['country']
            contact_info.country = coun
            contact_info.save()

            subj = request.POST['subject']
            contact_info.subject=subj

            contact_info.save()
            return redirect(home)
          
        except:
            return redirect(contact)
      
def thank(request):
    return render (request,'thankyou.html',{})




     
         

  


   




     
