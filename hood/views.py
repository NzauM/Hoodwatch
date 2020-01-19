from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile,Neighborhood,Business,Posts
from .forms import PostForm,BusinessForm,HoodForm
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    '''
    View function to render the home page
    '''
    all_hoods = Neighborhood.all_hoods()
    return render(request,'home.html',{'all_hoods':all_hoods})
    
@login_required(login_url='/accounts/login/')
def one_hood(request,id):
    '''
    View function to render details of one hood
    '''
    one_hood = Neighborhood.objects.get(id=id)
    businesses = Business.all_biz(bizhood_id = id)
    hood_occupants = Profile.get_occupants(hood_id = id)
    posts = Posts.post_by_hood(hood_id = id)
    return render(request,'one_hood.html',{'one_hood':one_hood,'businesses':businesses,'hood_occupants':hood_occupants})

@login_required(login_url='/accounts/login/')
def post(request):
    '''
    Function that will upload a new post
    '''
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()

            return redirect('home')

    else:
        form = PostForm()
    return render(request,'new_post.html',{'form':form})

@login_required(login_url='/accounts/login/')
def business(request):
    '''
    Function to upload a new business
    '''
    if request.method=='POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = request.user
            business.save()

            return redirect('home')


    else:
        form= BusinessForm()
    return render(request,'business.html',{'form':form})

@login_required(login_url='/accounts/login/')
def join_hood(request,id):
    '''
    Function for a user to join an neighbourhood
    '''
    neighborhood = get_object_or_404(Neighborhood,id=id)
    neighborhood=request.user.hood
    request.user.save()
    return redirect('home')


@login_required(login_url='/accounts/login/')
def leave_hood(request,id):
    hood = get_object_or_404(Neighborhood,id=id)
    request.user.neighborhood=None
    request.user.save()
    return redirect('home')


@login_required(login_url='/accounts/login/')
def profile(request):
    '''
    Function to render a user's profile
    '''
    all_posts = Posts.objects.filter(user = request.user)
    return render(request,'profile.html',{'all_posts':all_posts})


@login_required(login_url='/accounts/login/')
def new_hood(request):
    '''
    Function that will post a new neighborhood
    '''
    if request.method=='POST':
        form = HoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.occupant = request.user
            hood.save()

            return redirect('home')

    else:
        form = HoodForm()
    return render(request,'new_hood.html',{'form':form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    '''
    View function for searching a business
    '''
    if 'business' in request.GET and request.GET['business']:
        name = request.GET.get('business')
        searched_biz = Business.search_biz(name)
        message = f'{name}'

        return render(request,'search.html',{'message':message})

    else:
        message = 'You have not entered anything to search'
        return render(request,'search.html',{'message':message})




    


