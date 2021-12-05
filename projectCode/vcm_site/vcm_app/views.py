from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from django.db.models import Q

from .models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the VCM index.")


"""no long using this version of the method
def vendors(request):
    #return HttpResponse("Hello, world. You're at the vendors page.") 

  
    #vendor_list = Vendor.objects.all() #maybe make this a get_list_or_404()
    vendor_list = Vendor.objects.order_by('vendor_name')

    context = {'vendor_list': vendor_list,}
    
    return render(request, 'vcm_app/vendors.html', context)
"""


class VendorsView(generic.ListView):
    template_name = 'vcm_app/vendors.html'
    context_object_name = 'vendor_list'

    def get_queryset(self):
        #return Vendor.objects.all()

        if(search_term := self.request.GET.get("search_term")):
            return Vendor.objects.filter( Q(vendor_name__icontains=search_term) |
                                          Q(vendor_email__icontains=search_term)
                                        ).order_by('vendor_name') #searches single field, vendor_name
            """to search multiple fields, see https://testdriven.io/blog/django-search/
                otherwise must add one line for every field"""

        else:
            return Vendor.objects.order_by('vendor_name') #alphebatize


"""
def vendor_detail(request, vendor_id):

    vendor = get_object_or_404(Vendor, pk=vendor_id)

    return render(request, 'vcm_app/vendor_detail.html', {'vendor':vendor})
    """


#vendor_detail but with a generic view
class VendorDetailView(generic.DetailView):
    model = Vendor
    template_name = 'vcm_app/vendor_detail.html'

def contracts(request):
    return HttpResponse("Hello, world. You're at the contracts page.") 

#this is a stub for now
def contract_detail(request, contract_id):
   return HttpResponse("You're looking at contract %s." % contract_id)
    

"""class ContractDetailView(generic.DetailView):
    model = Contract
    template_name = 'vcm_app/contract_detail.html'
"""


