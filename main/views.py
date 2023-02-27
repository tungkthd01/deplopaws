from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import  AuthenticationForm
from .models import Post, Turial
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from .forms import NewUserForm,PostFormList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request= request,
                  template_name= "main/home.html",
                  context={"tutorials": Turial.objects.all()})

def register(request):
    if request.user.is_authenticated:
        return redirect('main:posts')
    else:
        form = NewUserForm()
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get("username")
                messages.success(request, f" New account created:{username}")
                return redirect("main:login")
            else:
                for msg in form.error_messages:
                    messages.error(request,f"{msg}:{form.error_messages[msg]}")
        return render(request,"main/register.html",context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.user.is_authenticated:
    		return redirect('main:posts')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username = username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request, f"You are now logged in as:{username}")
                    return redirect("main:posts")
                else:
                    messages.error(request,"Invalid username or password")
                    
            else:
                messages.error(request,"Invalid username or password")
        form = AuthenticationForm()
        return render(request,
                    "main/login.html",
                    {"form":form})
@login_required(login_url='login')
def home(request):
    post = Post.objects.all()
    user = request.user
    print(user)
    return render(request=request,template_name="posts/dashboard.html",context={"post":post})


@login_required(login_url='login')
def upload(request):
    forms = PostFormList()
    if request.method == "POST":
        if request.user.is_authenticated:
            #user = User.objects.get(pk=request.user.id)
            forms = PostFormList(request.POST, request.FILES)
            user = request.user
            forms.owner = user
            print(forms)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Creat successed")
                return redirect("main:posts")
            else:
                print("data is_vaild")
        else:
            print("chac la that")
    else:
        forms = PostFormList()
    return render(request,"posts/up_load.html",{"form":forms})  

# class UploadView(LoginRequiredMixin,CreateView):
#     model = Post
#     form_class =PostFormList
#     success_url = reverse_lazy('posts')
#     template_name = "posts/up_load.html"
    
# class PostList(APIView):
#     #permission_class = (permissions.IsAuthenticated)
#     def get(self, request,format=None):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts,many = True)
#         # form = PostList
#         # return render(request,"posts/dashboard.html",{"form":form})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request, format=None):
#         serilizer = PostSerializer(data= request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data, status=status.HTTP_201_CREATED)
#         return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)