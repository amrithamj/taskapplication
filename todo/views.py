from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,ListView,DetailView,UpdateView
from todo.forms import TaskForm,RegistrationForm,LoginForm
from todo.models import Tasks
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy





class IndexView(TemplateView):
    template_name="index.html"


class TaskCreateView(CreateView):
    model=Tasks
    form_class=TaskForm
    template_name="task-add.html"
    success_url=reverse_lazy("task-list")
    # def get(self,request,*args,**kwargs):
    #     form=TaskForm()
    #     return render(request,"task-add.html",{"form":form})

    # def post(self,request,*args,**kwargs):
    #     form=TaskForm(request.POST)
    #     if form.is_valid():
    #         # Tasks.objects.create(**form.cleaned_data)
    #         form.save()
    #         print("record saved")
    #         messages.success(request,"Task has been added")
    #         return redirect("task-list")
    #     else:
    #         messages.error(request,"Task creation failed!!")
    #         return render(request,"task-add.html",{"form":form})

class TaskListView(ListView):
    model=Tasks
    template_name="task-list.html"
    context_object_name="tasks"

    # def get(self,request,*args,**kwargs):
    #     qs=Tasks.objects.all()
    #     return render(request,"task-list.html",{"tasks":qs})
    
class TaskDetailView(DetailView):
    model=Tasks
    template_name="task-detail.html"
    context_object_name="task"
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Tasks.objects.get(id=id)
    #     return render(request,"task-detail.html",{"task":qs})

def task_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    Tasks.objects.get(id=id).delete()
    return redirect("task-list")
# class TaskDeleteView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         Tasks.objects.get(id=id).delete()
#         messages.success(request,"Task has been removed")
#         return redirect("task-list")

class TaskEditView(UpdateView):
    model=Tasks
    form_class=TaskForm
    template_name="task-edit.html"
    success_url=reverse_lazy("task-list")
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Tasks.objects.get(id=id)
    #     form=TaskForm(instance=qs)
    #     return render(request,"task-edit.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Tasks.objects.get(id=id)
    #     form=TaskForm(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"Task was updated successfully")
    #         return redirect("task-list")
    #     else:
    #         messages.error(request,"task updation failed!!")
    #         return render(request,"task-edit.html",{"form":form})

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            # User.objects.create(**form.cleaned_data)
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"Congragulations..Your account has been successfully created")
            return redirect("home")
        else:
            messages.error(request,"Registration failed!!")
            return render(request,"register.html",{"form":form})

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"You are successfully logged in")
                return redirect("home")
            else:
                messages.error(request,"Invalid credentials..Login failed!!")
                return render(request,"login.html",{"form":form})

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
# class SignOutView(View):
#     def get(self,request,*args,**kwargs):
#         logout(request)
#         return redirect("signin")

            



        


    





