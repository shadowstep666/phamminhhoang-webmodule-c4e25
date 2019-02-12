from mongoengine import Document, StringField

class Bike(Document):
    model=StringField()
    daily_fee=StringField()
    image=StringField()
    year=StringField()