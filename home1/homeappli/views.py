from django.shortcuts import render

# Create your views here.
def index(request):
    datas = {
        
    }
    return render(request, 'index.html', datas)


def about(request):
    datas = {
        
    }
    return render(request, 'about.html', datas)

def blog(request):
    datas = {
        
    }
    return render(request, 'blog.html', datas)


def contact(request):
    datas = {
        
    }
    return render(request, 'contact.html', datas)



def blogsingle(request):
    datas = {
        
    }
    return render(request, 'blog-single.html', datas)


def project(request):
    datas = {
        
    }
    return render(request, 'project.html', datas)


def team(request):
    datas = {
        
    }
    return render(request, 'team.html', datas)
