from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import IO

# Create your views here.
def index(request):
    compressed_types = ['application/gzip', 'application/x-7z-compressed', 'application/zip', 'application/vnd.rar']
    image_types = ['image/png', 'image/jpeg']

    zip_handler = IO()

    if request.method != 'POST':
        return bad_request()

    if request.content_type in image_types:
        img = request.body
        #tbd
    elif request.content_type in compressed_types:
        zipped = request.body
        images = zip_handler.read_zip(zipped)
        pass
        #tbd
    else:
        return bad_request()

    return HttpResponse()#zipfile)

def bad_request():
    return HttpResponseBadRequest('<h1>Invalid Request (400) </h1>', content_type='text/html')