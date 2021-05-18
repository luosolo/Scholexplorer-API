# from .scholix_v2 import api_v2
# from .model import ScholixType
# from flask_restx import Resource, fields
#
# lp = [
# ]
#
# links_from_datasource_parser = api_v2.parser()
# links_from_datasource_parser.add_argument('datasource', required=True,
#                                           help="Filter Scholix relationships collected from a LinkProvider")
# links_from_datasource_parser.add_argument('page', required=False, help="select page of result")
#
# links_from_pid_parser = api_v2.parser()
# links_from_pid_parser.add_argument("pid", required=True, help="persistent Identifier")
# links_from_pid_parser.add_argument("pidType", required=False, help="persistent Identifier Type")
# links_from_pid_parser.add_argument("targetPidType", required=False,
#                                    help="typology target filter should be publication, dataset or unknown")
# links_from_pid_parser.add_argument("datasourceTarget", required=False,
#                                    help="a datasource provenace filter of the target relation")
# links_from_pid_parser.add_argument("page", required=False, help="select page of result")
#
# links_from_publisher_parser = api_v2.parser()
# links_from_pid_parser.add_argument("publisher", required=True, help="publisher name")
# links_from_publisher_parser.add_argument("page", required=False, help="select page of result")
#
#
# @api_v2.route('/linksFromDatasource', doc={
#     "description": "return a list of scholix object collected from a specific datasource",
#
# })
# class LinksFromDatasource(Resource):
#     @api_v2.expect(links_from_datasource_parser)
#     @api_api_v2v1.marshal_list_with(ScholixType)
#     def get(self):
#         """Get all scholix relation collected from a datasource"""
#         args = links_from_datasource_parser.parse_args()
#         print(args)
#         return lp
#
#
# @api_v1.route("/linksFromPid", doc={
#     "description": "The linksFromPid endpoint returns a list of scholix object related from a specific persistent "
#                    "identifier",
# })
# class LinksFromPid(Resource):
#     @api_v1.expect(links_from_pid_parser)
#     @api_v1.marshal_list_with(ScholixType)
#     def get(self):
#         """Retrieve all scholix links from a persistent identifier"""
#         args = links_from_pid_parser.parse_args()
#         print(args)
#         return lp
#
#
# @api_v1.route("/linksFromPublisher", doc=dict(description="return a list of scholix object published from a specific "
#                                                           "publisher"))
# class LinksFromPublisher(Resource):
#     @api_v1.expect(links_from_publisher_parser)
#     @api_v1.marshal_list_with(ScholixType)
#     def get(self):
#         """Get all scholix relation collected from a publisher"""
#         args = links_from_pid_parser.parse_args()
#         print(args)
#         return lp
#
#
# @api_v1.route("/listDatasources", doc=dict(description="returns a list of all datasources"))
# class ListDatasources(Resource):
#     @api_v1.marshal_list_with(fields.String)
#     def get(self):
#         """Get all datasources"""
#         return lp
