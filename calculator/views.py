from django.shortcuts import render, HttpResponse

#hlavná logika programu

def index(request):
    if request.method == "GET":
        answer = 0
    if request.method == "POST":
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        operator = request.POST['operator']
        if operator == '+':
            answer = a + b
        elif operator == '-':
            answer = a - b
        elif operator == '*':
            answer = a * b
        else:
            answer = a / b
    return render(request, 'calculator/index.html', dict(answer = answer))