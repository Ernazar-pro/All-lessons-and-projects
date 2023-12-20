from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .forms import ProductForm


def home(request):
    return render(request, 'base.html')


 
def about(request):
    return render(request, 'scoop/about.html')


def contact(request):
    return render(request, 'scoop/contact.html')


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    
    context = {
        'form':form
    }
    return render(request, 'scoop/create.html', context)

def product_list(request, category_slug = None):
    category  = None
    categories = Category.objects.all()
    products  =Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category=category)
    return render (request, 'scoop/sale.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products' : products
                  })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available = True)
    return render(request, 'scoop/detail.html', {'product': product})