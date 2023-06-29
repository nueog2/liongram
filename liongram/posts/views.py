from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse

from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from .models import Post

def index(request): 
    post_list = Post.objects.all().order_by('-created_at') #post 전체 데이터 조회 
    #all()뒤에 .all().order_by('-created_at')를 넣으면 만들어진 순으로 (최신순으로)보여줌
    context = {
        'post_list': post_list,    
    }
    return render(request, 'index.html', context)


def post_list_view(request):
    post_list = Post.objects.all() #post 전체 데이터 조회 
    post_list = Post.objects.filter(writer=request.user) 
    #Post.wirter가 현재 로그인인 것 조회 
     
    context = {
        'post_list': post_list,    
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('index')
    context = {
        'post': post,    
    }
    return render(request, 'posts/post_detail.html', context)

def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            writer=request.user
        )
        return redirect('index')
    
#맨 마지막에 redirect를 하면 초록색으로 뜸! 

def post_update_view(request, id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')

# Create your views here.
def url_view(request):
    print('url_view()')
    data = { 'code': '001', 'msg':'OK'}
    return HttpResponse('<h1>url_view</h1>')
    # return JsonResponse(data)

def url_parameter_view(request,username):
    print('url_parameter_view()')
    # print(username)
    # print(request.GET)
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)
#요청해서 받을 수 있는 건
# 경로를 사용하거나 쿼리스트링과 쿼리파라미터를 활용하면 된다! 

def function_view(request):
    print(f'request.method: {request.method}')

    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')
#여기서 view_html은 템플릿이름을 말하는것임! 

class class_view(ListView): 
    model = Post
    ordering = ['-id']
    template_name = 'cbv_view.html'

def function_list_view(request):
    #함수기반뷰는 우리가 직접 모든걸 작성해야함. 
    #대신 코드가 직관적임
    object_list = Post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html', {'object_list' : object_list })