from django.shortcuts import render, HttpResponse

#hlavná logika programu

def index(request):
    if request.method == "GET":
        vysledok = " "
    if request.method == "POST":
        a = int(request.POST['cisloA'])
        b = int(request.POST['cisloB'])
        if (a > b):
            vysledok = ">"
        elif (b > a):
            vysledok = "<"
        else:
            vysledok = "="
    return render(request, 'cisla/index.html', {"vysledok": vysledok})