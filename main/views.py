from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import CreateProductForm
from main.models import Product

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

    product_entries = Product.objects.all()

    new_products = [{'name': Product.name, 'price': Product.price, 'description': Product.description, 'category': Product.category, 'ratings' : Product.ratings} for Product in product_entries]
    
    all_products = main_products + new_products
    
    # Data diteruskan ke template
    return render(request, 'main.html', {'products': all_products})

def create_product_form(request):
    form = CreateProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_form.html", context)

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