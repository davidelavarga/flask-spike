from flask import Flask, request, jsonify
from flask_jsonschema_validator import JSONSchemaValidator
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
JSONSchemaValidator(app=app, root="schemas")

todos = {}


@app.route('/register', methods=['POST'])
@app.validate('user', 'register')
def routeRegister():
    user = request.json
    return jsonify(user)

# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}
#
#     def put(self, todo_id):
#         todos[todo_id] = request.json
#         return {todo_id: todos[todo_id]}


# api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
