from .scholix_v2 import api_v2
from flask_restx import fields

LinkProviderType = api_v2.model("LinkProvider 2.0", {
    'name': fields.String(required=True, description='The name of the Provider that provides the links'),
    'totalRelationships': fields.Integer(required=True, description='The number of links that It provides'),
})

ScholixRelationshipType = api_v2.model("ScholixRelationshipType  2.0", {
    "Name": fields.String(required=False,
                          description="The relationship type chosen from a Scholix controlled vocabulary"),
    "SubType": fields.String(required=False, description="The sub-type of  Relationship Type name"),
    "SubTypeSchema": fields.String(required=False,
                                   description="The name of the schema or controlled list from which Relationship "
                                               "Sub-type is sourced"),
})

ScholixTypeSchema = api_v2.model("ScholixTypeSchema  2.0", {
    "Name": fields.String(required=False, description="The object type chosen from a Scholix controlled vocabulary"),
    "SubType": fields.String(required=False, description="The sub-type of  Object Type name"),
    "SubTypeSchema": fields.String(required=False,
                                   description="The name of the schema or controlled list from which Object Sub-type "
                                               "is sourced"),
})

ScholixIdentifierType = api_v2.model("ScholixIdentifierType 2.0", {
    "ID": fields.String(required=False, description="The identifier string"),
    "IDScheme": fields.String(required=False, description="The scheme or namespace of the identifier string"),
    "IDURL": fields.String(required=False, description="The URL value of the Identifier"),
})

ScholixLinkProviderType = api_v2.model("ScholixLinkProviderType 2.0", {
    'name': fields.String(required=True, description='The name of the Link Provider'),
    'identifier': fields.List(fields.Nested(ScholixIdentifierType),
                              description="A unique string that identifies the Link Provider")
})

ScholixCreatorType = api_v2.model("ScholixCreatorType 2.0", {
    'name': fields.String(required=False, description='The name of the Object Creator'),
    'identifiers': fields.List(fields.Nested(ScholixIdentifierType),
                               description="A unique string that identifies the Object Creator")
})

ScholixItemType = api_v2.model("ScholixItemType 2.0", {
    'Identifier': fields.List(fields.Nested(ScholixIdentifierType),
                              description="A unique string that identifies the object"),
    "Type": fields.Nested(ScholixTypeSchema, description="Describes the nature of the object (its intended usage)"),
    'Title': fields.String(required=False, description='The name of the object'),
    'Creator': fields.List(fields.Nested(ScholixCreatorType),
                           description="Party responsible for the creation of the object"),
    'PublicationDate': fields.String(required=False,
                                     description="The date the object was formally issued, published or distributed"),
    'Publisher': fields.List(fields.Nested(ScholixLinkProviderType),
                             description="The name of the publisher of the object")
})

ScholixType = api_v2.model("ScholixType 2.0", {
    'LinkPublicationDate': fields.String(required=False, description='Date when this Link Information Package was '
                                                                     'first formally issued from this current '
                                                                     'Provider'),
    'LinkProvider': fields.List(fields.Nested(ScholixLinkProviderType), description="The source(s) of this Link "
                                                                                    "Information Package"),
    'relationship': fields.Nested(ScholixRelationshipType, required=True, description="The nature of the relationship "
                                                                                      "between the source object and "
                                                                                      "target object in this Link "
                                                                                      "Information Package"),
    "LicenseURL": fields.String(required=False, description="The URL of the license for the Scholix Link Information "
                                                            "Package"),

    "Source": fields.Nested(ScholixItemType,
                            description="Root element relative to all properties describing the link’s source object."),

    "Target": fields.Nested(ScholixItemType,
                            description="Root element relative to all properties describing the link’s target object."),

})

ScholixResultType = api_v2.model("ScholixResultType 2.0", {
    "currentPage": fields.Integer(required=True, description='The current page number'),
    "totalLinks": fields.Integer(required=True, description='The number of total links'),
    "totalPages": fields.Integer(required=True, description='The number of total pages'),
    "result": fields.List(fields.Nested(ScholixType))

})
