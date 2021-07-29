from django.shortcuts import render


def landing_page(request):
    return render(request, 'common/../../templates/landing_page.html')
