from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow  
from flask_restful import Api, Resource 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
db = SQLAlchemy(app) 
ma = Marshmallow(app)
api = Api(app)

class Publication(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column( db.String(50) )
    content = db.Column( db.String(255) )

class Publication_Schema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content")

class ResourceListPublications(Resource):
    def get(self):
        publications = Publication.query.all()
        return posts_schema.dump(publications)
    
    def post(self):
            new_publication = Publication(
                title = request.json['title'],
                content=request.json['content']
            )
            db.session.add(new_publication)
            db.session.commit()
            return post_schema.dump(new_publication)

class ResourceOnePublication(Resource):
    def get(self, id_publication):
        publication = Publication.query.get_or_404(id_publication)
        return post_schema.dump(publication)
    
    def put(self, id_publication):
        publication = Publication.query.get_or_404(id_publication)

        if 'title' in request.json:
            publication.title = request.json['title']
        if 'content' in request.json:
            publication.content = request.json['content']

        db.session.commit()
        return post_schema.dump(publication)

    def delete(self, id_publication):
        publication = Publication.query.get_or_404(id_publication)
        db.session.delete(publication)
        db.session.commit()
        return '', 204

api.add_resource(ResourceListPublications, '/publications')
api.add_resource(ResourceOnePublication,'/publications/<int:id_publication>')

post_schema = Publication_Schema()
posts_schema = Publication_Schema(many = True)


if __name__ == '__main__':
    app.run(debug=True)