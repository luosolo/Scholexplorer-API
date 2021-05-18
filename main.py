from flask import Flask
from flask_restx import Api
from apis.v1.methods import *
from apis.v2.methods import *
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask("scholexplorerAPI")
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(
    title='Scholexplorer API',
    version='1.0',
    endpoint="api.scholexplorer.openaire.eu",
    contact_email="sandro.labruzzo@isti.cnr.it",
    description='The Scholix API allows clients to run REST queries over the Scholexplorer index in order to fetch '
                'links matching given criteria',
)

api.add_namespace(api_v1, path="/v1")
api.add_namespace(api_v2, path="/v2")
api.init_app(app, url_scheme="http")

app.config["RESTX_MASK_SWAGGER"] = False

if __name__ == '__main__':
    app.run(debug=True)
