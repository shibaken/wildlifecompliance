import json
import requests

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import RedirectView, View
from django.utils.http import urlencode
from django.conf import settings

from django.utils import timezone

from wildlifelicensing.apps.applications.models import Application

from wildlifelicensing.apps.payments.utils import generate_product_code, get_product, to_json
from wildlifelicensing.apps.payments.forms import PaymentsReportForm
from wildlifelicensing.apps.main.helpers import is_officer


JSON_REQUEST_HEADER_PARAMS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

PAYMENT_SYSTEM_ID = settings.WL_PAYMENT_SYSTEM_ID

SENIOR_VOUCHER_CODE = settings.WL_SENIOR_VOUCHER_CODE


class CheckoutApplicationView(RedirectView):
    def get(self, request, *args, **kwargs):
        application = get_object_or_404(Application, pk=args[0])
        product = get_product(generate_product_code(application))
        user = application.applicant_profile.user.id

        error_url = request.build_absolute_uri(reverse('wl_applications:preview'))
        success_url = request.build_absolute_uri(reverse('wl_applications:complete'))

        parameters = {
            'system': PAYMENT_SYSTEM_ID,
            'basket_owner': user,
            'associateInvoiceWithToken': True,
            'checkoutWithToken': True,
            'fallback_url': error_url,
            'return_url': success_url,
            'forceRedirect': True,
            'template': 'wl/payment_information.html',
            'proxy': is_officer(request.user),
            "products": [
                {"id": product.id if product is not None else None}
            ],
            "vouchers": []
        }

        # senior discount
        if application.is_senior_offer_applicable:
            parameters['vouchers'].append({'code': SENIOR_VOUCHER_CODE})

        url = request.build_absolute_uri(
            reverse('payments:ledger-initial-checkout')
        )

        response = requests.post(url, headers=JSON_REQUEST_HEADER_PARAMS, cookies=request.COOKIES,
                                 data=json.dumps(parameters))

        return HttpResponse(response.content)


class ManualPaymentView(RedirectView):
    def get(self, request, *args, **kwargs):
        application = get_object_or_404(Application, pk=args[0])

        url = reverse('payments:invoice-payment', args=(application.invoice_reference,))

        params = {
            'redirect_url': request.GET.get('redirect_url', reverse('wl_home'))
        }

        return redirect('{}?{}'.format(url, urlencode(params)))


class PaymentsReportView(View):
    success_url = reverse_lazy('wl_reports:reports')
    error_url = success_url

    def get(self, request):
        form = PaymentsReportForm(request.GET)
        if form.is_valid():
            start = form.cleaned_data.get('start')
            end = form.cleaned_data.get('end')
            # here start and end should be timezone aware (with the settings.TIME_ZONE
            start = timezone.make_aware(start) if not timezone.is_aware(start) else start
            end = timezone.make_aware(end) if not timezone.is_aware(end) else end
            url = request.build_absolute_uri(
                reverse('payments:ledger-report')
            )
            data = {
                'system': PAYMENT_SYSTEM_ID,
                'start': start,
                'end': end
            }
            response = requests.post(url,
                                     headers=JSON_REQUEST_HEADER_PARAMS,
                                     cookies=request.COOKIES,
                                     data=to_json(data))
            if response.status_code == 200:
                filename = 'wl_payments-{}_{}'.format(
                    str(start.date()),
                    str(end.date())
                )
                response = HttpResponse(response, content_type='text/csv; charset=utf-8')
                response['Content-Disposition'] = 'attachment; filename={}.csv'.format(filename)
                return response
            else:
                messages.error(request,
                               "There was an error while generating the payment report:<br>{}".format(response.content))
                return redirect(self.error_url)
        else:
            messages.error(request, form.errors)
            return redirect(self.error_url)
