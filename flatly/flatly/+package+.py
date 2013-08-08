from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='string')
def my_view(request):
    return "Hello world."


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    # Add your routes here.
    config.add_route('home', '/')

    config.scan()
    return config.make_wsgi_app()
