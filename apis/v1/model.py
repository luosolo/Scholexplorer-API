from .scholix_v1 import api_v1
from flask_restx import fields

LinkProvider = api_v1.model("LinkProvider", {
    'name': fields.String(required=True, description='The name of the Provider that provides the links'),
    'totalRelationships': fields.Integer(required=True, description='The number of links that It provides'),
})

LinkPublisher = api_v1.model("LinkPublisher", {
    'name': fields.String(required=True, description='The name of the Publisher that provides the links'),
    'totalRelationships': fields.String(required=True, description='The number of links that It provides'),
})

IdentifierType = api_v1.model("IdentifierType", {
    'identifier': fields.String(required=False, description='The value of the identifier'),
    'schema': fields.String(required=False, description='the schema resource of the identifier')
})

ScholixProviderType = api_v1.model("ScholixProviderType", {
    'name': fields.String(required=True, description='The name of the provider'),
    'identifiers': fields.List(fields.Nested(IdentifierType))
})
RelationshipType = api_v1.model("RelationshipType", {
    'name': fields.String(required=True, description='The name of the Relation'),
    'schema': fields.String(required=False, description='The schema URL of the relationship'),
    'inverseRelationship': fields.String(required=False, description='The value of the inverse Relation')
})

CreatorType = api_v1.model("CreatorType", {
    'name': fields.String(required=False, description='The name of the author'),
    'identifiers': fields.List(fields.Nested(IdentifierType))
})

ScholixObjectType = api_v1.model("ScholixObjectType", {
    'type': fields.String(required=True, description='The typology of the object'),
    'subtype': fields.String(required=False, description='The subtype of the object'),
})

ScholixItemType = api_v1.model("ScholixItemType", {
    'identifiers': fields.List(fields.Nested(IdentifierType)),
    'title': fields.String(required=False, description='The Title'),
    'objectType': fields.Nested(ScholixObjectType),
    'creators': fields.List(fields.Nested(CreatorType)),
    'publisher': fields.List(fields.Nested(ScholixProviderType)),
    'objectProvider': fields.List(fields.Nested(ScholixProviderType)),

})


source_example = {
            "identifier": [{
                "identifier": "id1",
                "schema": "schema1"
            }, {
                "identifier": "id2",
                "schema": "schema2"
            }],
            "objectType": "dataset",
            "objectSubType": "table",
            "title": "title 0",
            "creator": [{
                "name": "Author1",
                "identifier": {
                    "identifier": "id1",
                    "schema": "schema1"
                }
            }, {
                "name": "Author2",
                "identifier": {
                    "identifier": "id1",
                    "schema": "schema1"
                }
            }],
            "publicationDate": "2006-05-04",
            "publisher": {
                "name": "publisher",
                "identifier": [{
                    "identifier": "id1",
                    "schema": "schema1"
                }, {
                    "identifier": "id2",
                    "schema": "schema2"
                }]
            }
        }

ScholixType = api_v1.model("ScholixType", {
    'linkProvider': fields.List(fields.Nested(ScholixProviderType)),
    'publicationDate': fields.String(required=False, description='The date of publication of scholix link'),
    'relationship': fields.Nested(RelationshipType),
    'source': fields.Nested(ScholixItemType, example=source_example),
    'target': fields.Nested(ScholixItemType, example=source_example)
})
