#from django.http import HttpResponse
#
#def index(request):
#    # Get an HttpRequest - the request parameter
#    # perform operations using information from the request.
#    # Return HttpResponse
#    return HttpResponse('Hello from Django!')

from django.shortcuts import render
from .models import Team 

def index(request):
    list_teams = Team.objects.filter(team_level__exact="U09")
    context = {'youngest_teams': list_teams}
    return render(request, '/best/index.html', context)
    #return HttpResponse('Hello from Django!')
