from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Product, Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/')
    
@login_required
def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart')

@login_required
def cart(request):
    items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'items': items})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})
cart = []

def home(request):

    search = request.GET.get("search")

    if search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()

    return render(request,"home.html",{"products":products})


def product_detail(request,id):

    product = get_object_or_404(Product,id=id)

    return render(request,"product.html",{"product":product})


from django.shortcuts import render, get_object_or_404
from .models import Product

cart = []

def add_to_cart(request, id):

    product = get_object_or_404(Product, id=id)

    cart.append(product)

    return render(request, "cart.html", {"cart": cart})


def view_cart(request):

    return render(request,"cart.html",{"cart":cart})