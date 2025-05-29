from flask_restx import Namespace, Resource, fields
from models import db, Item

api = Namespace('items', description='Operations related to items')

item_model = api.model('Item', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, description='Item name'),
    'quantity': fields.Integer(required=True, description='Item quantity'),
})

@api.route('/')
class ItemList(Resource):
    @api.marshal_list_with(item_model)
    def get(self):
        return Item.query.all()

    @api.expect(item_model)
    @api.marshal_with(item_model, code=201)
    def post(self):
        data = api.payload
        item = Item(name=data['name'], quantity=data['quantity'])
        db.session.add(item)
        db.session.commit()
        return item, 201

@api.route('/<int:item_id>')
@api.response(404, 'Item not found')
@api.param('item_id', 'The item identifier')
class ItemResource(Resource):
    @api.marshal_with(item_model)
    def get(self, item_id):
        return Item.query.get_or_404(item_id)
