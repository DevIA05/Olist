from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def component_alert(request):
    return render(request, 'components-alerts.html')

def test(request):
    return render(request, 'test.html')

def charts(request):
    return render(request, 'charts-chartjs.html')
