from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import StudentResult, Testimonial, ContactSubmission

def home(request):
    toppers = StudentResult.objects.filter(is_topper=True).order_by('-year', '-score')[:6]
    testimonials = Testimonial.objects.filter(is_featured=True)[:3]
    total_students = StudentResult.objects.count()
    years_active = 15
    top_scores = StudentResult.objects.filter(score__gte=90).count()
    context = {
        'toppers': toppers,
        'testimonials': testimonials,
        'total_students': total_students,
        'years_active': years_active,
        'top_scores': top_scores,
    }
    return render(request, 'core/home.html', context)

def results(request):
    board_filter = request.GET.get('board', '')
    year_filter = request.GET.get('year', '')
    search_query = request.GET.get('search', '')

    results_qs = StudentResult.objects.all()
    if board_filter:
        results_qs = results_qs.filter(board=board_filter)
    if year_filter:
        results_qs = results_qs.filter(year=year_filter)
    if search_query:
        results_qs = results_qs.filter(name__icontains=search_query)

    paginator = Paginator(results_qs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    years = StudentResult.objects.values_list('year', flat=True).distinct().order_by('-year')
    context = {
        'page_obj': page_obj,
        'years': years,
        'board_filter': board_filter,
        'year_filter': year_filter,
        'search_query': search_query,
        'total_count': results_qs.count(),
    }
    return render(request, 'core/results.html', context)

def testimonials(request):
    all_testimonials = Testimonial.objects.all().order_by('-year')
    context = {'testimonials': all_testimonials}
    return render(request, 'core/testimonials.html', context)

def subjects(request):
    return render(request, 'core/subjects.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if name and phone and message:
            ContactSubmission.objects.create(name=name, phone=phone, email=email, message=message)
            messages.success(request, 'Thank you! We will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all required fields.')
    return render(request, 'core/contact.html')
