from django.http import HttpResponse


class StripeWH_Handler:
    """Handle stripe webhooks"""

    # To access attributes from request coming from stripe 
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle generic/unknown/unexpected webhook events"""

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

