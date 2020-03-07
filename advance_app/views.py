from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.http import HttpResponse
# Create your views here.

# Funtion Based View
def index(request):
    return render(request,'advance_app_template/index.html', {})


# Class Based Views(CBV)

# 1. View Class
class cbv_View(View):
    def get(self,request):
        # return HttpResponse("Example Class Based Views......")
        return render(request, 'advance_app_template/cbv_view.html', {'insert_me': 'Class Based Views using (Generic) View Class'})

# 2. Template View Class
class cbv_tempView(TemplateView):
    template_name = 'advance_app_template/cbv_template_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Example of CBV using Template View Class'
        return  context

# 3. List View Class
class SchoolListView(ListView):
    # By default the name context will generated as modelname_list (all in lowercase)....
    # So here the the context name would be like 'school_list' and we don't need to it pass out though the render.
    # if you have to change the context name then use the below code:
    # context_object_name = 'schools'
    # By using this the context name changed from 'school_list' to 'schools'
    model = models.School

# 4. Detail View Class
class SchoolDetailView(DetailView):
    # By default the context name will generated as the lowercase od modelname.....
    # so here the context would be like 'school'
    # if you want to change the context name then do as above as specified in the list view comment.
    model = models.School
    template_name = 'advance_app/school_details.html'



# CRUD Operations

# 1. CreateView
class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

# 2. UpdateView
class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

# 3. DeleteView
class SchoolDeleteView(DeleteView):
    # By default the context name will generated as the lowercase od modelname.....
    # so here the context would be like 'school'
    # if you want to change the context name then do as above as specified in the list view comment.
    model = models.School
    success_url = reverse_lazy("advance_app:school_view")
    # success_url means once you 'suceessfully' deleted the school redirect to this page