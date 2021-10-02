from django.http import HttpResponse
from django.shortcuts import render
from .models import brochure
from .models import testimonials
# Create your views here.

def demo(request):
    a = brochure.objects.all()
    b = testimonials.objects.all()
    return render(request,"index.html",{'result':a,'result1':b})

# def trial(request):
    # return HttpResponse("Home Page")

#
# def about(request):
#     return HttpResponse("About Page")
#
# def contact(request):
#     return render(request,"contact.html")
#
# def detail(request):
#     return render(request,"detail.html")
#
# def thank(request):
#     return render(request,"thank.html")
#
# def result(request):
#     x=int(request.GET['value 1'])
#     y=int(request.GET['value 2'])
#     tot_add=x+y
#
#     return  render(request,"result.html",{'result':tot_add})
#
#
# def result2(request):
#     x = int(request.GET['value 1'])
#     y = int(request.GET['value 2'])
#     tot_mul=x*y
#
#     return render(request, "result2.html", {'result2': tot_mul})
#
#
# def result3(request):
#     x = int(request.GET['value 1'])
#     y = int(request.GET['value 2'])
#     tot_div=x/y
#
#     return render(request, "result3.html", {'result3': tot_div})
#
# def result4(request):
#     x = int(request.GET['value 1'])
#     y = int(request.GET['value 2'])
#     tot_sub=x-y
#
#     return render(request, "result4.html", {'result4': tot_sub})
#
# def operation(request):
#     return  render(request,"distance.html")




