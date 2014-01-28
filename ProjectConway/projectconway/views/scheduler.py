from pyramid.view import view_config

@view_config(route_name='scheduler', renderer='projectconway:templates/scheduler.mako')
def scheduler_view(request):
    '''
    Executes the logic for the scheduler, allowing the user to choose a time
    at which to play their game of life.
    '''
    return {}
