from django.http import HttpResponse


class StripeWH_Handler:
    """Handle stripe webhooks"""

    # To access attributes from request coming from stripe
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle generic/unknown/unexpected webhook events"""

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle payment_intent.succeeded webhook from stripe"""

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle payment_intent.payment_failed webhook from stripe"""

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

