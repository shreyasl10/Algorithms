from flask import Flask
from flask_restful import Api, Resource
app=Flask(__name__)
api=Api(app)
class Hello(Resource):
    def get(self):
        return {"data":"hello"}
    
api.add_resource(Hello,"/hello")
app.run(debug=True)
