from .models import *

def add_variable_to_context(request):
    try:
        companyInfo = SoftwareCompany.objects.get(company_code__exact="coded by Masum phone(+8801551805248)")
    except:
        companyInfo = SoftwareCompany.objects.all()

    client_details = OurClients.objects.all()
    project_detils = LatestProjects.objects.all()
    everyWhere = {
        'clientDetails': client_details,
        'projectDetails': project_detils,
        'companyInfo': companyInfo,
    }
    return everyWhere
