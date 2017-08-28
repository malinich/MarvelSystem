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
        user=request.user;
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
                Comixes =Comixes.filter(date__year=int(year))
            SerializerList=[models.ComixSerializer(item) for item in Comixes]
            separator="\|/"
            return HttpResponse(JSONRenderer().render(serializer.data)+separator.encode('ascii') for serializer in SerializerList)
        else:
            return HttpResponse("Oooops")

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
        return HttpResponse(output);

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

def auth(request):
    if 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('catalog/page=1?manuf=&model=&strings=&frets=&tremolo=&pickups=&frm=&priceto=&sort=new')
        else:
            return HttpResponseRedirect('auth')
    else:
        user=request.user;
        context={'user':user}
        context.update(csrf(request))
        return render('auth.html',context)