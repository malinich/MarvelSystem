from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView
from MarvelComixStore import forms,models
from django.db.models import Q
from rest_framework.renderers import JSONRenderer
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class Search(DetailView):
    def get(self,request):
        form=forms.searchForm()
        user=request.user
        models.Comix.objects.first().__str__()
        return render(request,'marvel.html',{'form':form, 'user':user})
    def post(self,request):
        Comixes=models.Comix.objects.all()
        form=forms.searchForm(request.POST)

        if form.is_valid():
            keywords_str=form.cleaned_data.get('keywords',None)
            year = form.cleaned_data.get('year',None)
            keywords=keywords_str.split(' ')
            for keyword in keywords:
                Comixes=Comixes.filter(Q(Q(name__icontains=keyword)|Q(description__icontains=keyword)|Q(tags__name__icontains=keyword))).distinct()
            if year!='0':
                print('111')
                Comixes =Comixes.filter(date__year=int(year))
            SerializerList=[models.ComixSerializer(item) for item in Comixes]
            separator="\|/"
            return HttpResponse(JSONRenderer().render(serializer.data)+separator.encode('ascii') for serializer in SerializerList)
        else:
            return HttpResponse("Oooops")

class Comics(DetailView):
    def get(self,request,*args,**kwargs):
        #comixes=models.Comix.objects.all()
        #comixes.filter(cus)
        user=get_object_or_404(models.User,username=kwargs['username'])
        customer = models.Customer.objects.get(user=user)
        comics=models.Comix.objects.filter(customer=customer)

        context={ 'user':user, 'comics':comics}
        return render(request, 'comics.html', context)


class get_years(DetailView):
    def get(self,request):
        iquery = []
        for i in models.Comix.objects.all():
            iquery.append(str(i.getYear()))
        iset = set(iquery)
        output=""
        for inst in iset:
            output+=inst+"\n"
        return HttpResponse(output);


class get_tags(DetailView):
    def get(self,request):
        tags=models.Tag.objects.all()
        output=[]
        for tag in tags:
            output+=tag.name+"\n"
        return HttpResponse(output)

class ComixView(DetailView):
    def get(self,request,*args,**kwargs):
        ean=kwargs['ean']
        instance=get_object_or_404(models.Comix,ean=ean)
        tags=models.Tag.objects.filter(comix=instance)
        context={'comix':instance, 'tags':tags}
        return render(request,'comix.html',context)

class Index(DetailView):
    def get(self,requst):
        return HttpResponseRedirect('marvel')

def LogOut(request):
    logout(request)
    return HttpResponseRedirect('marvel')

def add(request,*args,**kwargs):
    user=request.user
    ean=kwargs['ean']
    if models.Comix.objects.exists(ean=ean):
        customer=models.Customer.objects.get(user=user)
