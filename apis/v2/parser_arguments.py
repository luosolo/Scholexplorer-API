from .scholix_v2 import api_v2

links_provider_parser = api_v2.parser()
links_provider_parser.add_argument('name', required=False, help="Filter the link provider by a name")


links_parser = api_v2.parser()