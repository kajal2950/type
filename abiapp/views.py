from django.shortcuts import render
from.models import*
from django.db.models import Max,Min




# Create your views here.
def index(request):
    obj = Video.objects.all()
    banner = Banner.objects.all()
    category = Category.objects.all()

    context = {
    'object' : obj,
    'banner' : banner,
    'cat' : category,
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')    

def contact(request):
    return render(request,'contact.html') 

def blog(request):
    return render(request,'blog.html')         

def videos(request):
    obj = Video.objects.all()
    category = Category.objects.all()
    min_price = Video.objects.all().aggregate(Min('price'))
    max_price = Video.objects.all().aggregate(Max('price'))

    VIDEOID=request.GET.get('categories')
    if VIDEOID:
        videos=Video.objects.filter(category=VIDEOID)
    

    context = {
        'min_price':min_price,
        'max_price':max_price,
        'obj':obj,
        'cat' : category,
    }
    return render(request,'allvideos.html',context) 

def category(request,slug):
    category=Category.objects.all()
    cat=Category.objects.get(slug=slug)
    products=Video.objects.filter(category=cat)
    video=Video.objects.filter(slug=slug)
    context={
        'pro':products,
        'cat':category,
        'videos':video,

        }
    return render(request,'allvideos.html', context)      