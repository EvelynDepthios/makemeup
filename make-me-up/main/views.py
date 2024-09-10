from django.shortcuts import render

def show_main(request):
    # Data produk didefinisikan secara manual dalam bentuk list of dictionaries
    products = [
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
        }
    ]
    
    # Data diteruskan ke template
    return render(request, 'main.html', {'products': products})
