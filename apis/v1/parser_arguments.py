from .scholix_v1 import api_v1


links_from_datasource_parser = api_v1.parser()
links_from_datasource_parser.add_argument('datasource', required=True,
                                          help="Filter Scholix relationships collected from a LinkProvider")
links_from_datasource_parser.add_argument('page', required=False, help="select page of result")

links_from_pid_parser = api_v1.parser()
links_from_pid_parser.add_argument("pid", required=True, help="persistent Identifier")
links_from_pid_parser.add_argument("pidType", required=False, help="persistent Identifier Type")
links_from_pid_parser.add_argument("targetPidType", required=False,
                                   help="typology target filter should be publication, dataset or unknown")
links_from_pid_parser.add_argument("datasourceTarget", required=False,
                                   help="a datasource provenace filter of the target relation")
links_from_pid_parser.add_argument("page", required=False, help="select page of result")

links_from_publisher_parser = api_v1.parser()
links_from_pid_parser.add_argument("publisher", required=True, help="publisher name")
links_from_publisher_parser.add_argument("page", required=False, help="select page of result")