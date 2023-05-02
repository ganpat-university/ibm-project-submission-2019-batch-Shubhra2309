from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill
import logging
import sys
from . import urls
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import AuthenticationForm

# sys.path.append(r'C:\Users\dhair\PycharmProjects\DjangoERP\InventoryManagement-Django\core')
sys.path.append("..")
from core import AdvancedSecurity
from core import AdvancedLogging

logger = logging.getLogger(__name__)


class HomeView(View):
    template_name = "home.html"

    def get(self, request):

        labels = []
        data = []
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels': labels,
            'data': data,
            'sales': sales,
            'purchases': purchases
        }

        print("TEST", AdvancedSecurity.GLOBAL_LOCKDOWN, urls.urlpatterns)
        if AdvancedSecurity.GLOBAL_LOCKDOWN == True:
            return redirect('lockdown')
        else:
            return render(request, self.template_name, context)


def AboutView(request):
    if AdvancedSecurity.GLOBAL_LOCKDOWN == False:
        return render(request, 'about.html')
    else:
        return redirect('lockdown')


def Login(request):
    if AdvancedSecurity.GLOBAL_LOCKDOWN == True:
        return redirect('lockdown')

    # AdvancedLogging.LogLogin(REMOTE_ADDR=self.request.META.get('REMOTE_ADDR'), USER_NAME=user[0],CALLED_FROM="get_success_url")
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        print("HERE 0")
        print(request.META.get('REMOTE_ADDR'))
        print()
        AdvancedLogging.LogLogin(REMOTE_ADDR=request.META.get('REMOTE_ADDR'), USER_NAME=form.data.dict()['username'],
                                 CALLED_FROM="other")
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                x = login(request, user)
                AdvancedLogging.LogLogin(REMOTE_ADDR=request.META.get('REMOTE_ADDR'), USER_NAME=username,
                                         CALLED_FROM="success")
                return redirect('home')
    else:
        print("HERE 3")
        form = CustomAuthenticationForm(request=request)


    return render(request, 'login.html', {'form': form})
