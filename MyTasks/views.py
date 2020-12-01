from django.shortcuts import render, redirect
from .models import TodoModel
# Create your views here.
def home(request):
    if request.method=='POST':
        text=request.POST['todotext']
        TodoModel.objects.create(TodoText=text)
        return redirect('/')
    all=TodoModel.objects.all()
    all=all[::-1]
    return render(request, 'Todo_home.html', {'allTodo':all})
def delete(request,id):
    if request.method=='GET':
        text= TodoModel.objects.get(pk=id)
        text.delete()
        return redirect('/')
    else:
        return render(request, 'Todo_home.html')
def search(request):
    if request.method=='GET':
        st=request.GET.get('querytext')
        print(st)
        s=TodoModel.objects.all().filter(TodoText__icontains=st)
       
        return render(request, 'search.html', {'searchtext':s})
    return render(request, 'Todo_home.html')
def edit(request,id):
    if request.method=='POST':
        text= TodoModel.objects.get(pk=id)
        text.TodoText=request.POST['todotext']
        text.save()
        return redirect('home')
    else:
        text= TodoModel.objects.get(pk=id)
        return render(request, 'Edit_Todo.html', {'todoobject':text })