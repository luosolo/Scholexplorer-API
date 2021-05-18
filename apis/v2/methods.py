from flask_restx import Resource

from .model import *
from .parser_arguments import *

lp = []


@api_v2.route('/LinkProvider', doc={
    "description": "Return a list of link provider and relative number of relations",

})
class LinkProviderMethod(Resource):
    @api_v2.expect(links_provider_parser)
    @api_v2.marshal_list_with(LinkProviderType)
    def get(self):
        """Get All Link Providers"""
        args = links_provider_parser.parse_args()
        print(args)
        return lp


@api_v2.route('/LinkPublisher/inSource', doc={
    "description": "Return a List of all Publishers that provide source objects in Scholix links and the total number "
                   "of links where the source object comes from this publisher "

})
class LinkPublisherSource(Resource):
    @api_v2.expect(links_provider_parser)
    @api_v2.marshal_list_with(LinkProviderType)
    def get(self):
        """Get All Publishers that provide source object"""
        return lp


@api_v2.route('/LinkPublisher/inTarget', doc={
    "description": "Return a List of all Publishers that provide source objects in Scholix links and the total number "
                   "of links where the target object comes from this publisher "

})
class LinkPublisherTarget(Resource):
    @api_v2.expect(links_provider_parser)
    @api_v2.marshal_list_with(LinkProviderType)
    def get(self):
        """Get All Publishers that provide target object"""
        return lp


@api_v2.route('/Links', doc={
    "description": "Return a List of scholix Links, this method require one of the following parameters (sourcePid, "
                   "targetPid, sourcePublisher, targetPublisher, linkProvider) all parameters can be combined "

})
class Links(Resource):
    @api_v2.expect(links_parser)
    @api_v2.marshal_list_with(ScholixResultType)
    def get(self):
        """Get Scholix Links"""
        return lp
