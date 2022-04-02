from django.shortcuts import render

# View function rendering the react application on the django framework

def index(request, *args, **kwargs):
    return render(request, 'ideahub_index.html')
