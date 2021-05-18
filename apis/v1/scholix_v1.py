from flask_restx import Namespace

api_v1 = Namespace('Scholix Version 1.0', title='Scholexplorer API 1.0', description="scholexplorer API version 1.0")
import apis.v1.methods
