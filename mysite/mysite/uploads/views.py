from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .store_file import store_file_to_azure
from .logic import handle_uploaded_file
from .charts import charts, datasummary

@login_required
def index(request):
    template = loader.get_template("uploads/index.html")
    context = {'show_upload_status': False, 'uploaded_file_url': False, 'form': UploadFileForm()}

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        fs = FileSystemStorage()
        filename = fs.save('{}.xlsx'.format('_'.join([request.POST['tipo'],str(request.user), request.POST['periodo']])),request.FILES['archivo'])
        upload_url = fs.url(filename)
        if handle_uploaded_file(request.FILES['archivo'],request.POST['tipo']):
            store_file_to_azure(upload_url)
            script, div = charts(request.FILES['archivo'], request.POST['tipo'])
            summary = datasummary(request.FILES['archivo'])
            print(summary)
            context['resumen'] = summary
            context['show_upload_status'] = True
            context['uploaded_file_success'] = True
            context['script'] = script
            context['div'] = div

            return render(request, 'uploads/index.html', context)
        else:
            context['show_upload_status'] = True
            context['uploaded_file_success'] = False
            context['error_list'] = ['a','b','c']
            return render(request, 'uploads/index.html', context)
        #else:
            #return HttpResponse("Form not valid")
    else:
        return render(request, 'uploads/index.html', context)

@login_required
def get_user_profile(request,username):
    user = User.objects.get(username=username)
    return render(request, 'uploads')
