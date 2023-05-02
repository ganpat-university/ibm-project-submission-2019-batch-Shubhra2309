from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse
class LockdownMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.redirected = False

    def __call__(self, request):
        # Check for the variable in the other file
        from AdvancedSecurity import GLOBAL_LOCKDOWN as lockdown_variable
        if lockdown_variable and not self.redirected:
            # Redirect to lockdown page
            self.redirected = True
            return redirect(reverse('lockdown'))

        response = self.get_response(request)
        return response