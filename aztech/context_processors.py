from .models import *

def add_variable_to_context(request):
    client_details = OurClients.objects.all()
    project_detils = LatestProjects.objects.all()
    everyWhere = {
        'clientDetails': client_details,
        'projectDetails': project_detils,
    }
    return everyWhere
