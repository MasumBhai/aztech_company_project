from .models import *

def add_variable_to_context(request):
    client_details = OurClients.objects.all()
    everyWhere = {
        'clientDetails':client_details,
    }
    return everyWhere
