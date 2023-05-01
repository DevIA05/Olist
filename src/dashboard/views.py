from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def test(request):
    return render(request, 'pages/test.html')

def charts(request):
    return render(request, 'pages/charts-chartjs.html')

def GeneralTables(request):
    return render(request, 'pages/tables-general.html')

def DataTables(request):
    return render(request, 'pages/tables-data.html')