from django.shortcuts import render

posts = [
    {
        'author' : 'Pandit Hajari lal',
        'title'  : 'Poem',
        'content':'Or din dhal gaya',
        'date_posted':'28 Aug 2022',
    },
    {
        'author' : 'Kanhaiya lal',
        'title'  : 'Story',
        'content':'Mai gata nahi',
        'date_posted':'29 Aug 2022',
    }
]

def home(request) :
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
   return render(request, 'blog/about.html',{'title':'about'})
   