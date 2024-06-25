from django.shortcuts import render, redirect
from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_search(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    if query:
        search_terms = query.split(',')
        query_filter = Q()
        for term in search_terms:
            query_filter |= Q(name__icontains=term.strip())
            query_filter |= Q(reference__icontains=term.strip())
            query_filter |= Q(position__icontains=term.strip())
            


        products = Product.objects.filter(query_filter)

        if category:
            products = products.filter(category=category)
    elif category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    
    # selected_product_ids = request.session.get('selected_product_ids', [])
    paginator = Paginator(products, 10)  # Show 10 products per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'query': query,
        'category': category,
        # 'selected_product_ids': selected_product_ids,
    }
    return render(request, 'products.html', context)

def print_products(request):
    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('selected_products')
        
        current_selected_ids = request.session.get('selected_product_ids', [])
        updated_selected_ids = list(set(current_selected_ids + selected_product_ids))
        request.session['selected_product_ids'] = updated_selected_ids
        
        selected_products = Product.objects.filter(id__in=updated_selected_ids)
        return render(request, 'print_preview.html', {'selected_products': selected_products})
    
    return redirect('product_search')

def clear_selection(request):
    if 'selected_product_ids' in request.session:
        del request.session['selected_product_ids']
    
    return redirect('product_search')

def select_products(request):
    selected_product_ids = request.session.get('selected_product_ids', [])
    selected_products = Product.objects.filter(id__in=selected_product_ids)
    return render(request, 'selected_products.html', {'selected_products': selected_products})
    


