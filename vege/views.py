from django.shortcuts import render, redirect
from vege.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from home.utils import send_email_to_client, send_email_to_client_with_attachment
# Create your views here.

@login_required(login_url = "/login/")
def create(request):
    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        return redirect('/receipe/create/')
    query_set = Receipe.objects.all()
    
    if request.GET.get('search'):
        query_set = Receipe.objects.filter(receipe_name__icontains = request.GET.get('search'))
    context = {'receipes' : query_set}
    return render(request, 'create.html', context)

@login_required(login_url = "/login/")
def delete(request, id):
    query_set = Receipe.objects.get(id = id)
    query_set.delete()
    return redirect('/receipe/create/')

@login_required(login_url = "/login/")
def update(request, id):
    query_set = Receipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        query_set.receipe_name = receipe_name
        query_set.receipe_description = receipe_description
        if receipe_image:
            query_set.receipe_image = receipe_image
        query_set.save()
        return redirect('/receipe/create/')
    context = {'receipe' : query_set}
    return render(request, 'update.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username):
            messages.error(request, "Username does not exists.")
            return redirect('/login/')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "Invalid Password");
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/receipe/create/')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "User name already exists.")
            return redirect('/register/')
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully.")
        return redirect('/login/')
    return render(request, 'register.html')

@login_required(login_url = "/login/")
def get_students(request):
    students = Student.objects.all()
    # students = Student.admin_objects.all() # for getting with trashed  students
    search = ''
    if(request.GET.get('search')):
        search = request.GET.get('search')
        students = students.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search)
        )
    paginator = Paginator(students, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'report/students.html', {'students' : page_obj, 'search': search})

@login_required(login_url = "/login/")
def see_marks(request, student_id):
    marks = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks = marks.aggregate(total_marks = Sum('marks'))
    return render(request, 'report/marks.html', {'marks': marks, 'total_marks': total_marks})

@login_required(login_url = "/login/")
def send_email(request):
    send_email_to_client()
    send_email_to_client_with_attachment()
    return redirect(request.META.get('HTTP_REFERER', '/'))