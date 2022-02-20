from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from . import Pipeline


def handle_post(request):
    #print(request.META)
    #return HttpResponse("<h1> Hello </h1>", content_type='text/html')

    compressed_types = ['application/gzip', 'application/x-7z-compressed', 'application/zip', 'application/vnd.rar']

    if request.method != 'POST':
        return bad_request()

    zbytes = request.body
    #zid = request.cookie

    #z_file = open("./temp/input_%s.zip".format(zid), "wb")
    #z_file.write(bytes)
    #z_file.close()

    pipe = Pipeline()
    sendzip = pipe.process_all(zbytes)
    

    if request.content_type not in compressed_types:
        return bad_request()
    
    return HttpResponse(sendzip) #zipfile

def bad_request():
    return HttpResponseBadRequest('<h1>Invalid Request (400) </h1>', content_type='text/html')