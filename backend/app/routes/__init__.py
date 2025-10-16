from flask import Blueprint
from flask_restful import Api
from .auth import RegisterResource, LoginResource, MeResource
from .auth import RegisterOrganizerResource
from .events import EventsListResource, EventResource
from .events import EventStatsResource
from .tickets import EventTicketsResource
from .orders import OrdersResource, UserOrdersResource, OrderDetailResource, EventOrdersResource
from .orders import VerifyCheckinResource, MarkCheckinResource
from .dashboard import OrganizerDashboardResource, AdminDashboardResource
from .users import UsersListResource, UserRoleResource
from .swagger import SwaggerSpecResource
from .uploads import ImageUploadResource


def register_routes(app):
    api_bp = Blueprint('api', __name__, url_prefix='/api')
    api = Api(api_bp)

    # Auth endpoints
    api.add_resource(RegisterResource, '/auth/register')
    api.add_resource(RegisterOrganizerResource, '/auth/register-organizer')
    api.add_resource(LoginResource, '/auth/login')
    api.add_resource(MeResource, '/auth/me')

    # Events endpoints
    api.add_resource(EventsListResource, '/events')
    api.add_resource(EventResource, '/events/<string:event_id>')
    api.add_resource(EventStatsResource, '/events/<string:event_id>/stats')

    # Tickets endpoints
    api.add_resource(EventTicketsResource, '/events/<string:event_id>/tickets')

    # Orders endpoints
    api.add_resource(OrdersResource, '/orders')
    api.add_resource(UserOrdersResource, '/orders/user')
    api.add_resource(OrderDetailResource, '/orders/<string:order_id>')
    api.add_resource(EventOrdersResource, '/events/<string:event_id>/orders')
    api.add_resource(VerifyCheckinResource, '/checkin/verify')
    api.add_resource(MarkCheckinResource, '/checkin/mark')

    # Dashboard endpoints
    api.add_resource(OrganizerDashboardResource, '/dashboard/organizer')
    api.add_resource(AdminDashboardResource, '/dashboard/admin')

    # Admin - Users
    api.add_resource(UsersListResource, '/users')
    api.add_resource(UserRoleResource, '/users/<string:user_id>/role')

    # Swagger
    api.add_resource(SwaggerSpecResource, '/docs/swagger.json')

    # Uploads
    api.add_resource(ImageUploadResource, '/uploads/image')

    app.register_blueprint(api_bp)
