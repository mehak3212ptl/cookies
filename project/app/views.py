from django.shortcuts import render

# Create your views here.
def set(request):
    response=render(request,'home.html')
    response.set_cookie('name','mehak',max_age=5*24*60*60.,httponly=True,secure=True)
    response.set_cookie('city','pipariya',max_age=5*24*60*60,httponly=True,secure=True)
    response.set_cookie('age','21',max_age=5*24*60*60,httponly=True,secure=True)
    return response

def get(request):
    print(request.COOKIES)
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    city=request.COOKIES['city']
    data={
        'name':name,
        'city':city,
        'age':age
    }
    return  render(request,'get.html',data)