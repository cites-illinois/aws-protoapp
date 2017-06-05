from __future__ import print_function

import sys
import time

from bcrypt import  gensalt, hashpw
from datetime import datetime

from django.views.generic import TemplateView

#####

class ProtoAppTemplateView(TemplateView):

    #####

    def get(self, request, *args, **kwargs):
        #   Add record to session history before rendering view.
        _add_session_entry(request)
        return super(ProtoAppTemplateView, self).get(request, args, kwargs)

#####

class AboutView(ProtoAppTemplateView):
    template_name   = 'about.html'

#####

class ContactView(ProtoAppTemplateView):
    template_name   = 'contact.html'

#####

class CryptView(ProtoAppTemplateView):
    template_name   = 'crypt.html'

    #####

    def dispatch(self, request, *args, **kwargs):
        #   Get number of rounds from keyword arguments.
        self.rounds = int(kwargs.get('rounds', 12))

        #   Take start timestamp.
        time_start = time.clock()

        #   Run hash operation, saving result in view object.
        self.hashed_pw  = hashpw('secret string', gensalt(self.rounds))

        #   Take end timestamp.
        time_end   = time.clock()

        #   Determine elapsed time, saving result in view object.
        self.elapsed_time = time_end - time_start

        #   Invoke superclass dispatcher.
        return super(CryptView, self).dispatch(request, *args, **kwargs)
        
    #####

    def get_context_data(self, **kwargs):
        context = super(CryptView, self).get_context_data(**kwargs)

        #   Put view variables in context for template processing. Elapsed
        #   time is rounded to nearest thousandth of a second.
        context['elapsed_time'] = '{:.3f}'.format(round(self.elapsed_time, 3))
        context['hashed_pw']    = self.hashed_pw
        context['rounds']       = self.rounds

        return context

#####

class HomeView(ProtoAppTemplateView):
    template_name   = 'home.html'

#####

class LipsumView(ProtoAppTemplateView):
    template_name   = 'lipsum.html'

#####

class SessionView(ProtoAppTemplateView):
    template_name   = 'session.html'

#####

def _add_session_entry(request):
    context = \
        {
        'method'    : request.method,
        'path'      : request.path,
        'timestamp' : datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        }

    #   Get request_list or empty list and append request context.
    request_list = request.session.get('request_list', list())
    request_list.append(context)

    #   Write updated request_list to session store.
    request.session['request_list'] = request_list

    print(context, file=sys.stderr)
    return
