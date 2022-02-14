from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .forms import PostForm


def upload_image_file(request):
    f = request.FILES['image']
    fs = FileSystemStorage()
    filename = str(f).split('.')[0]
    file = fs.save(filename, f)
    fileurl = fs.url(file)
    return JsonResponse({'success': 1, 'file':{'url':fileurl}})

def upload_file_view(request):
    f = request.FILES['file']
    fs = FileSystemStorage()
    filename,ext = str(f).split('.')
    file = fs.save(filename, f)
    fileurl = fs.url(file)
    return JsonResponse(
        {
            'success': 1,
            'file':{
                'url':fileurl,
                'size': fs.size(filename),
                'name': str(f),
                'extension': ext
            }
        }
    )

def editjs_home_view(request):
    template_name = "djs/posts.html"
    if request.method == "POST":
        print('-' * 50, 'post')
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return render(request, template_name, {'form': form})
    print('-' * 50, 'get')
    form = PostForm(request.POST or None)
    return render(request, template_name, {'form': form})

def editjs_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'djs/post_detail.html', {'post': post})
