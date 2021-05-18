from flask import Flask
from flask_restx import Api
from apis.v1.scholix_v1 import api_v1
from apis.v2.scholix_v2 import api_v2
from werkzeug.middleware.proxy_fix import ProxyFix



app = Flask("scholexplorerAPI")
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(
    title='Scholexplorer API',
    version='1.0',
    contact_email= "sandro.labruzzo@isti.cnr.it",    
    description='The Scholix API allows clients to run REST queries over the Scholexplorer index in order to fetch links matching given criteria.',
)

api.add_namespace(api_v1, path="/v1")
api.add_namespace(api_v2, path="/v2")
api.init_app(app)



app.config["RESTX_MASK_SWAGGER"]=False

if __name__ == '__main__':
    app.run(debug=True)
