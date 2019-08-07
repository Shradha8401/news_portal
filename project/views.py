from django.shortcuts import render

def home(request): #browser bta j auxa tesko sabai info request ma hunx
    print(request)
    template_name="index.html"
    return render(request,template_name)