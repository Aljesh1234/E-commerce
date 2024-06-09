
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import messages




from .models import *

# Create your views here.

class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['barands'] = Brand.objects.all()
    views['site'] = StieInfo.objects.all()


class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['slideritems'] = Slider.objects.all()
        self.views['ads'] = ADD.objects.all()
        self.views['hots'] = Product.objects.filter(labels = 'hot')
        self.views['news'] = Product.objects.filter(labels = 'new')
        self.views['sales'] = Product.objects.filter(labels = 'sale')

        return render (request,'index.html',self.views)

class CatoegoryView(BaseView):
    def get(self,request,slug):
        cat_id = Category.objects.get(slug = slug).id
        self.views['cat_products'] = Product.objects.filter(category_id = cat_id)

        return render(request,'category.html',self.views)

class BrandView(BaseView):
    def get(self,request,slug):
        br_id = Brand.objects.get(slug = slug)
        self.views['brand_products'] = Product.objects.filter(brand_id = br_id)

        return render(request,'brand.html',self.views)


class DetailView(BaseView):
    def get(self,request,slug):
        self.views['detail_products'] = Product.objects.filter(slug = slug)
        cat_id = Product.objects.get(slug = slug).category_id
        self.views['related_product'] = Product.objects.filter(category_id = cat_id)
        self.views['product_reviews'] = ProductReviews.objects.filter(slug = slug)
        return render(request, 'product-detail.html', self.views)


class SearchView(BaseView):

    def get(self,request):
        self.views
        #if request.method == 'GET':
            #query = request
        query = request.GET.get('search')
        if query != '':
            self.views['search_products'] = Product.objects.filter(name__icontains = query)
        elif query == ' ':
            return redirect('/')
        else:
            return redirect('/')
        return  render(request,'search.html',self.views)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,"This username is already used!")
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, "This email is already exists!")
                return redirect('/signup')
            else:
                User.objects.create_user(
                    username = username,
                    email = email,
                    first_name = first_name,
                    last_name = last_name,
                    password= password
                ).save()
        else:
            messages.error(request, "The passwords do not match!")
            return redirect('/signup')

    return render(request,'signup.html')

class CartView(BaseView):
    def get(self,request):
        total_price = 0
        username = request.user.username
        self.views['cart_products'] = Cart.objects.filter(name = username, checkout = False)
        for i in Cart.objects.filter(name = username, checkout = False):
            total_price = total_price + i.total
        self.views['total_price'] = total_price
        self.views['delivery_charge']= 50
        self.views['all_total_price'] = total_price + self.views['delivery_charge']
        return render(request,'cart.html',self.views)


def cart(request,slug):
    username = request.user.username
    original_price = Product.objects.get(slug = slug).price
    discounted_price = Product.objects.get(slug = slug).discounted_price
    if Cart.objects.filter(slug = slug).exists():
        qty = Cart.objects.get(slug=slug).quantity
        qty = qty + 1
        if discounted_price > 0:
            price = original_price
        else:
            price = original_price
        total = price * qty
        Cart.objects.filter(name = username,checkout = False,slug = slug).update(
            total = total,quantity = qty
        )
    else:
        price = original_price
        total = original_price
        Cart.objects.create(
            name = username,
            price = price,
            quantity = 1,
            total = total,
            slug = slug,
            product = Product.objects.filter(slug = slug)[0]
        )
    return redirect('/cart')



def reduce_quantity(request,slug):
    username = request.user.username
    original_price = Product.objects.get(slug = slug).price
    discounted_price = Product.objects.get(slug = slug).discounted_price
    if Cart.objects.filter(slug = slug).exists():
        qty = Cart.objects.get(slug=slug).quantity
        if qty >1:
            qty = qty - 1
            if discounted_price > 0:
                price = original_price
            else:
                price = original_price
            total = price * qty
            Cart.objects.filter(name = username,checkout = False,slug = slug).update(
                total = total,quantity = qty
            )
        else:
            messages.error(request, "The quantity is already 1")
            return redirect('/cart')
        return redirect('/cart')



def delete_cart(request,slug):
    username = request.user.username
    Cart.objects.filter(name = username, slug = slug,checkout = False).delete()
    return redirect('/cart')


def submit_review(request,slug):
    if request.method == "POST":
        username = request.user.email
        email = request.user.email
        star = request.user['star']
        review = request.POST['review']
        ProductReviews.objects.create(
            username = username,
            email = email,
            star = star,
            review = review,
            slug = slug
        ).save()
    return redirect(f'/detail/{slug}')


