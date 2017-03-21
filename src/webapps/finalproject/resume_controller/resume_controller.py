from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from finalproject.resume_controller.resume_utils import resume_utils
from finalproject.forms import File_form
from finalproject.models import ModelFile
@login_required
def page_upload_resume(request):
    if request.method == "GET":
        # try:
        file_to_edit = ModelFile.objects.get(user=request.user)
        form = File_form(instance=file_to_edit)
        # except:
        #     form = File_form()
        context = {'form': form}
        return render(request, 'profile.html', context)


def api_resume(request):
    if request.method == "POST":
        return resume_utils.upload_resume(request)
    return redirect('page_upload_resume')

