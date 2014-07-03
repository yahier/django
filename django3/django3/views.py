from django.http import HttpResponse
from django.http import Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

def ya(request):
	return HttpResponse("hello,yahier")

def html(request):
    t = get_template('gallery.html')
    html = t.render(Context())
    return HttpResponse(html)
   
def html2(request):
    return render_to_response('gallery.html')
    
def error(request):
	return HttpResponse("hello,yahier not find")
 
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    try:
      offset = int(offset)
    except ValueError:
        raise Http404()
    
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html);





