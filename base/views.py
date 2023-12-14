from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string

# Create your views here.



class IndexView(View):
    def get(self,request):
        Product=[]
        Product1=product.objects.all()
        
        for p in Product1:
            if p.prix >= 10000:
                Product.append(p)
            
        context={
            'Product1':Product
        }
        return render(request,'front/index.html',context)

class ProductsView(View):
    def get(self,request,produits):
        image=imageP.objects.get(id_product=produits)
        produits=product.objects.get(pk=produits)

        Product=[]
        Product1=product.objects.all()
        
        for p in Product1:
            if p.prix >= 5000:
                Product.append(p)

        context={
            'Product1':Product,
            'p':produits,
            'img':image
        }

        return render(request,'front/products.html',context)

class CategorieView(View):
    def get(self,request,categorie):
       
        cat=Categorie.objects.get(Nom=categorie)
        products=product.objects.filter(id_Categorie=cat.pk)   
        p=Paginator(products,4)
        page_number = request.GET.get('page')

        try:
            R= p.page(page_number)
        except PageNotAnInteger:
            R=p.page(1) 
        except EmptyPage:
            R=p.page(p.num_pages) 
        
        Gammes=Gamme.objects.all()

        context={
            'products':R,
            'categorie':categorie,
            'Gammes' :Gammes,
            
        }
        return render(request,'front/categorie.html',context)

class GammeView(View):
    def get(self,request,Gammes):
        GA=Gamme.objects.get(Nom=Gammes)
        products=product.objects.filter(id_Gamme=GA.pk)   
        context={
            'products':products,
            'Gamme' :Gammes,
            'Gammes':Gamme.objects.all()
        }
        return render(request,'front/Gamme.html',context)

class Cartview(View):
    def get(self,request):
        total_amt=0
        for p_id,item in request.session['cartdata'].items():
            total_amt+=int(item['qty'])*float(item['price'])
        return render(request, 'front/Cart.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})


class AddtocartView(View):
    def get(self,request):
        # del request.session['cartdata']
        cart_p={}
        cart_p[str(request.GET['id'])]={
            'image':request.GET['image'],
            'title':request.GET['title'],
            'qty':request.GET['qty'],
            'price':request.GET['price'],
            
        }
        if 'cartdata' in request.session:
            if str(request.GET['id']) in request.session['cartdata']:
                cart_data=request.session['cartdata']
                cart_data[str(request.GET['id'])]['qty']=int(cart_p[str(request.GET['id'])]['qty'])
                cart_data[str(request.GET['id'])]['price']=float(cart_p[str(request.GET['id'])]['price'])
                cart_data.update(cart_data)
                request.session['cartdata']=cart_data
            else:
                cart_data=request.session['cartdata']
                cart_data.update(cart_p)
                request.session['cartdata']=cart_data
        else:
            request.session['cartdata']=cart_p
        
        return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})



#delete item 
class delete_item_cartView(View):
    def get(self,request):
        p_id=str(request.GET['id'])
        if 'cartdata' in request.session:
            if p_id in request.session['cartdata']:
                cart_data=request.session['cartdata']
                del request.session['cartdata'][p_id]
                request.session['cartdata']=cart_data
        total_amt=0
        for p_id,item in request.session['cartdata'].items():
            total_amt+=int(item['qty'])*float(item['price'])
        t=render_to_string('cart-list.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
        return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})


class update_item_cartView(View):
    def get(self,request):
        p_id=str(request.GET['id'])
        p_qty=request.GET['qty']
        if 'cartdata' in request.session:
            if p_id in request.session['cartdata']:
                cart_data=request.session['cartdata']
                cart_data[str(request.GET['id'])]['qty']=p_qty
                request.session['cartdata']=cart_data
        total_amt=0
        for p_id,item in request.session['cartdata'].items():
            total_amt+=int(item['qty'])*float(item['price'])
        t=render_to_string('cart-list.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
        return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})