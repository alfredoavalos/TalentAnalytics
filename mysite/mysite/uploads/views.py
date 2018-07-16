from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .store_file import store_file_to_azure
from .logic import handle_uploaded_file
from .charts import charts, datasummary
import os
from datetime import datetime, timedelta

@login_required
def index(request):
    template = loader.get_template("uploads/index.html")
    context = {'show_upload_status': False, 'uploaded_file_url': False, 'form': UploadFileForm()}

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fs = FileSystemStorage()
            filename = fs.save('{}.xlsx'.format('_'.join([request.POST['tipo'],str(request.user),\
             request.POST['periodo']])),request.FILES['archivo'])
            url = fs.url(filename)

            upload_file_handle, errors = handle_uploaded_file(request.FILES['archivo'],request.POST['tipo'], ' '.join([str(request.POST['periodo']).title(),str(datetime.today().year)]))

            if upload_file_handle:

                store_file_to_azure(url)

                script, div = charts(request.FILES['archivo'], request.POST['tipo'])

                summary = datasummary(request.FILES['archivo'])

                context['resumen'] = summary
                context['show_upload_status'] = True
                context['uploaded_file_success'] = True
                context['script'] = script
                context['div'] = div

                return render(request, 'uploads/index.html', context)
            else:
                errors_list = '<ul style="background-color: white !important"> '
                for key, value in errors.items():
                    if not value:
                        errors_list += '<li> ' + key + '</li>'
                errors_list += '</ul>'
                context['show_upload_status'] = True
                context['uploaded_file_success'] = False
                context['error_list'] = errors_list
                os.remove(url)
                return render(request, 'uploads/index.html', context)
        else:
            return HttpResponse("Form not valid")
    else:
        return render(request, 'uploads/index.html', context)

@login_required
def get_user_profile(request,username):
    user = User.objects.get(username=username)
    return render(request, 'uploads')
