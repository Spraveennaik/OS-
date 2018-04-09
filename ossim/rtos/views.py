

# Create your views here.
from django.shortcuts import render
from . import executer
# Create your views here.


def home(request):
    return render(request,'rtos/rtos_index.html')

def rms(request):
    if request == "POST":
        inp = request.args['input']
        out = executer.execute('RTOS/rate_monotonic', inp)
        print (out)
        return(out)
    else:
        return render(request, 'rtos/rtos_rms.html')
def wiki(request):
    return render(request,'rtos/rtos_wiki.html')
