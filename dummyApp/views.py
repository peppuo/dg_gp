from django.shortcuts import render


def render_template(request):
    return render(request, 'dummyApp/practice_template.html')
