from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_search(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    products = Product.objects.all()
    
    # Filter based on query if provided
    if query:
        search_terms = query.split(',')
        query_filter = Q()
        for term in search_terms:
            query_filter |= Q(name__icontains=term.strip())
            query_filter |= Q(reference__icontains=term.strip())
            query_filter |= Q(position__icontains=term.strip())
        products = products.filter(query_filter)

    # Further filter by category if provided
    if category:
        products = products.filter(category=category)

    # Pagination
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'query': query,
        'category': category,
    }
    return render(request, 'products.html', context)


def clear_selection(request):
    if 'selected_product_ids' in request.session:
        del request.session['selected_product_ids']
    
    return redirect('product_search')

def print_products(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        selected_product_ids = request.POST.getlist('selected_products')
        
        if action == 'save_and_print':
            current_selected_ids = request.session.get('selected_product_ids', [])
            updated_selected_ids = list(set(current_selected_ids + selected_product_ids))
            request.session['selected_product_ids'] = updated_selected_ids
            
            selected_products = Product.objects.filter(id__in=updated_selected_ids)
            return render(request, 'print_preview.html', {'selected_products': selected_products})
        
        elif action == 'save_and_stay':
            current_selected_ids = request.session.get('selected_product_ids', [])
            updated_selected_ids = list(set(current_selected_ids + selected_product_ids))
            request.session['selected_product_ids'] = updated_selected_ids
            return redirect('product_search') 
        
    return redirect('product_search')
