from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import CreateProductForm
from main.models import Product
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    # Data produk didefinisikan secara manual dalam bentuk list of dictionaries
    main_products = [
        {
            'name': 'Lip Butter Balm for Hydration & Shine',
            'price': 24000,
            'description': 'Moisturizing lip balm for hydration and shine.',
            'category': 'Lip Care',
            'ratings': 9,
        },
        {
            'name': 'Soft Pinch Liquid Blush',
            'price': 14000,
            'description': 'Lightweight liquid blush for a soft, radiant finish.',
            'category': 'Blush',
            'ratings': 8,
        },
        {
            'name': 'Major Headlines Double-Take Crème & Powder',
            'price': 38000,
            'description': 'A dual-ended compact with crème and powder blush.',
            'category': 'Blush',
            'ratings': 10,
        },
    ]

    # Fetching products from the database
    product_entries = Product.objects.filter(user=request.user)

    # Merging manual data with database data
    new_products = [{'name': prod.name, 'price': prod.price, 'description': prod.description, 'category': prod.category, 'ratings': prod.ratings} for prod in product_entries]

    all_products = main_products + new_products

    # Creating context to pass to the template
    context = {
        'nama': request.user.username,
        'kelas': 'PBP F',
        'products': all_products,
        'last_login': request.COOKIES['last_login'],
    }

    # Rendering the main template
    return render(request, 'main.html', context)

def create_product_form(request):
    form = CreateProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user  # Assign the product to the logged-in user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_form.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
