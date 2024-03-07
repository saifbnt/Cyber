from django.shortcuts import render

# Create your views here.

# monapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import nmap
from .models import Site

import subprocess

@csrf_exempt
def scan_site(request):
    if request.method == 'POST':
        data = request.POST.get('url')
        if data:
            try:
                nm = nmap.PortScanner()
                nm.scan(data, arguments='-Pn')
                scan_result = nm.csv()
                site, created = Site.objects.get_or_create(url=data)
                site.scan_result = scan_result
                site.save()
                return JsonResponse({'result': scan_result})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'URL is required'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
######################### sqlmap **********

import subprocess


def sqlmap_test(request, url):
    try:
        # Utilisation de subprocess pour appeler SQLMap depuis Python
        result = subprocess.check_output(['sqlmap', '-u', url])
        return JsonResponse({'result': result.decode('utf-8')})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

