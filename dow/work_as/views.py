from django.shortcuts import render,render_to_response
from django.views import generic
from .models import Note,Part
from django.http import HttpResponse
import json
# Create your views here.

def login(request):
    return render(request,'work_as/login.html',{})


class main(generic.ListView):
    template_name = 'work_as/main.html'
    context_object_name = 'all_notes'
    model = Note

class parts(generic.ListView):
    template_name = 'work_as/parts.html'
    context_object_name = 'all_parts'
    model = Part

class createPart(generic.CreateView):
    model = Part
    fields = [
        'code',
        'description',
        'price',
        'quantity',
        'storage'
    ]
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse("")

    def form_invalid(self, form):
        return render(self.request,"work_as/form-template.html",{'form':form},status=400)

class partDetail(generic.DetailView):
    context_object_name = 'part'
    template_name = 'work_as/partDetail.html'
    model = Part

    def get_object(self,queryset=None):
        return Part.objects.all().filter(code=self.kwargs['part_code'])[0]

def search(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        parts = Part.objects.filter(code__icontains = q )[:20]
        results = []
        for part in parts:
            part_json = {}
            part_json['id'] = part.code
            part_json['label'] = part.code
            part_json['value'] = part.code
            results.append(part_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)