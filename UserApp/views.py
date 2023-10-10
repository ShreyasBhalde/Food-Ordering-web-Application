from django.shortcuts import render,redirect
from django.http import HttpResponse
from AdminApp.models import Restaurant,menucategory,menuitem,Accounts
from UserApp.models import userinfo,mycart,deliverydetails

# Create your views here.
def Mainpage(request):
    restaurant=Restaurant.objects.all()
    Menucategory=menucategory.objects.all()
    return render(request,"Mainpage.html",{"Restaurants":restaurant,"menucategorys":Menucategory})

def menu(request,id1):
    restaurant=Restaurant.objects.get(id=id1)       
    Menucategory=menucategory.objects.all()
    Menuitem=menuitem.objects.all()
    data={}
    for menu in Menucategory:
        data[menu]=menuitem.objects.filter(cat_fk=menu.id)
    print(data)
    return render(request,"menu.html",{"Restaurants":restaurant,"Menucategory":Menucategory,"menuitems":Menuitem,"data":data})

def signup(request):
    if(request.method =="GET"):
        return render(request,"signup.html",{})
    else:
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        try :
            user=userinfo.objects.get(username=uname)
        except :
            user=userinfo(uname,pwd,email,phone)
            user.save()
            return redirect(Mainpage)
        else:
            return redirect(signup)

def login(request):
    if(request.method =="GET"):
        return render(request,"login.html",{})
    else:
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        try :
            user=userinfo.objects.get(username=uname,password=pwd)
        except :
            return redirect(login)
        else:
            request.session["uname"]=uname
            return redirect(Mainpage)

def logout(request):
    request.session.clear()
    return redirect(Mainpage)

def showcart(request):
    cats=menucategory.objects.all()
    items=mycart.objects.filter(user=request.session["uname"])
    total = 0 
    for item in items:
        total += item.qty * item.menuitem.price

    request.session["total"] = total
    return render(request,"showcart.html",{"items":items,"cats":cats})

def savedetails(request):
    if request.method == "POST":
        if "uname" in request.session:
            uname = request.session["uname"]
            name = request.POST["name"]
            ad = request.POST["ad"]
            city = request.POST["City"]
            zip = request.POST["Zip"]
            print(name, ad)  
            item = deliverydetails()
            item.name = name
            item.adddress = ad
            item.city = city
            item.zip=zip
            item.save()
            return redirect(showcart)


def addtocart(request):
   if request.method == "POST":
        if "uname" in request.session:
            uname = request.session["uname"]
            cid = request.POST["id"]
            qty = request.POST["qty"]
            print(cid, qty)  
            menu_item = menuitem.objects.get(id=cid)
            user_info = userinfo.objects.get(username=uname)
            item = mycart()
            item.user = user_info
            item.menuitem = menu_item
            item.qty = qty
            item.save()
            return redirect(showcart)
        else:
            return redirect(login)

    
def modifycart(request):
    action=request.POST["action"]
    cid=request.POST["cid"]
    item=mycart.objects.get(user=request.session["uname"],menuitem=cid)
    if(action=="Remove"):
        item.delete()
    else:
        item.qty=request.POST["qty"]
        item.save()
    return redirect(showcart)

def makepayment(request):
    if(request.method == "GET"):
        return render(request,"makepayment.html",{})
    else:
        cardno = request.POST["cardno"]
        cvv  = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = Accounts.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
            print(buyer)
        except:
            return redirect(makepayment)
        else:
            owner = Accounts.objects.get(cardno='2222',cvv='2222',expiry='12/01/2030')
            amount = request.session["total"]
            buyer.balance -= amount
            owner.balance +=amount
            buyer.save()
            owner.save()
            items = mycart.objects.filter(user = request.session["uname"])
            details = []
            for item in items:
                details.append(item.menuitem.id)
                item.delete()
            return redirect(Mainpage)

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")