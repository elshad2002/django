from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "mainapp/index.html")

def products(request):
    return render(request, "mainapp/products.html")

def contact(request):
    return render(request, "mainapp/contact.html")

def context(request):
    context = {
        'title':'test context',
        'header':'Добро пожаловать на сайт',
        'username':'Djohn',
        'products':[
            {'name':'стулья','price':6789},
            {'name':'Диваны','price':12789},
            {'name':'столы','price':26789},
        ]
    }
    return render(request, "mainapp/test_context.html", context)

def menu(request):
    links_menu = [
        {'href':'products_all', 'name':'всё'},
        {'href':'products_home', 'name':'дом'},
        {'href':'products_office', 'name':'офис'},
        {'href':'products_classic', 'name':'классика'},
    ]
    return render(request, 'inc_categories_menu.html', links_menu)