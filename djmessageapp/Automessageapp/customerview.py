from django.shortcuts import render
from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import json
from Automessageapp.serializers import CustomerSerializer
from Automessageapp.models import Customers
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt
from subprocess import call
import subprocess
import threading

from .tuple_to_dict import ParseDict
import os

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def CustomerInterface(request):
    
    return render(request,'CustomerInterface.html')


@api_view(['GET','POST'])
def CustomerSubmit(request):
    if request.method == 'POST':
        customer_serializer = CustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            
            return render(request,"CustomerInterface.html",{"message":"Record Submitted Successfully"})
        return render(request,"CustomerInterface.html",{"message":"Fail to Submit Record"})
    

@xframe_options_exempt 
@api_view(['GET','POST'])
def DisplayCustomerrec(request):
  try:
    if request.method == 'GET':
      list_customer=Customers.objects.all()
      list_customer_serializer=CustomerSerializer(list_customer,many=True)
      records=tuple_to_dict.ParseDict(list_customer_serializer.data)
      print(records)
      # def open_py_file():
      #    call(["python","Whatsauto.py"])

      # open_py_file()
      return render(request,'DisplayCustomer.html',{'data':records})
  except Exception as e:
       print("Error:",e)
       return render(request,'DisplayCustomer.html',{'data':{}})   
  

@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayByCustomerId(request):
  try:
    if request.method == 'GET':
      q="Select * from automessageapp_customers where id={0} ".format(request.GET['id'])
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseDictSingleRecord(cursor)
    #   print("xxxx",record)
       
      return render(request,'DisplayByCustomerId.html',{'data':record})
  except Exception as e:
       print("Error:",e)
       return render(request,'DisplayByCustomerId.html',{'data':{}})
  

@xframe_options_exempt
@api_view(['GET','POST'])
def EditCustomerrec(request):
   try:
      if request.method =='GET':
         if(request.GET['btn']=="EDIT"):
            customer=Customers.objects.get(pk=request.GET['id'])#hidden id
            customer.customername=request.GET['customername']
            customer.contactno = request.GET['contactno']
            customer.lastdate = request.GET['lastdate']
            customer.hourtime = request.GET['hourtime']
            customer.mintime = request.GET['mintime']
            customer.save()
            print("xyz")

         else:
            print("XXXXX")
            customer=Customers.objects.get(pk=request.GET['id'])
            customer.delete()

         return redirect('/api/displaycustomer')
   except Exception as e:
      print("Error:",e)
      return redirect('/api/displaycustomer')
   



def open_py_file():
    script_path = os.path.join('E:', 'djmessageapp', 'Whatsauto.py')
    subprocess.call(["python", script_path])

def Message_search(request):
    try:
        if request.method == 'GET':
            list_customer = Customers.objects.all()
            list_customer_serializer = CustomerSerializer(list_customer, many=True)
            records = ParseDict(list_customer_serializer.data)
            print(records)

            # Create a new thread to run the open_py_file() function
            thread = threading.Thread(target=open_py_file)
            thread.start()

            return render(request, 'DisplayCustomer.html', {'data': records})
    except Exception as e:
        print("Error:", e)
        return render(request, 'DisplayCustomer.html', {'data': {}})
