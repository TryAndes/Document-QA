from flask import jsonify
from flask_restx import Resource
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from andes import app, api

# simple test route
@api.route('/test')
class Test(Resource):
    def get(self):
        return jsonify({'message': 'success version 1'})

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# run server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
