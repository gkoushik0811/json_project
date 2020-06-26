from django.shortcuts import render
from testapp.models import Employee
from django.views.generic import View
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import serializeMixin,HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utills import is_json
from testapp.forms import Employee_Form
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')

class Employee_Detail_View(HttpResponseMixin,serializeMixin,View):
    def object_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp
    def get(self,request,id,*args,**kwargs):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data=json.dumps({'msg':"required resource is not available"})
        else:
            json_data=self.serialize([emp,])

        return HttpResponse(json_data,content_type='application.json')
    def put(self,request,id,*args,**kwargs):
        emp=self.object_id(id)
        if emp is None:
            json_data=json.dumps({'msg':"required resource is not available"})
            return self.render_to_http_response(json_data,status=400)
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        provided_data=json.loads(data)
        original_data={
        'eno':emp.eno,
        'ename':emp.ename,
        'eLocation':emp.eLocation,
        'start_time':emp.start_time,
        'end_time':emp.end_time
        }
        original_data.update(provided_data)
        form=Employee_Form(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':' Resource Updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
    def delete(self,request,id,*args,**kwargs):
        emp=self.object_id(id)
        if emp is None:
            json_data=json.dumps({'msg':"required resource is not available"})
            return self.render_to_http_response(json_data,status=400)
        emp.delete()
        json_data=json.dumps({'msg':' Resource Deleted successfully'})
        return self.render_to_http_response(json_data)








@method_decorator(csrf_exempt,name='dispatch')
class Employee_cbv(HttpResponseMixin,serializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        empdata=json.loads(data)
        form=Employee_Form(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':' Resource Created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
