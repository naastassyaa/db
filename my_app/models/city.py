from my_app.app import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(45))
    time_zone = db.Column(db.String(45))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    address = db.relationship('Address', backref='address', lazy=True)

    def __repr__(self):
        return f"<City {self.city_name}>"

    @staticmethod
    def create_city(city_name, time_zone, country_id):
        new_city = City(city_name=city_name, time_zone=time_zone, country_id=country_id)
        db.session.add(new_city)
        db.session.commit()
        return new_city

    @staticmethod
    def get_all_cities():
        return City.query.all()

    @staticmethod
    def get_city_by_id(city_id):
        return City.query.get(city_id)

    def update_city(self, new_city_name, new_time_zone, new_country_id):
        self.city_name = new_city_name
        self.time_zone = new_time_zone
        self.country_id = new_country_id
        db.session.commit()
        return self

    @staticmethod
    def delete_city(city_id):
        city = City.query.get(city_id)
        if city:
            db.session.delete(city)
            db.session.commit()
            return True
        return False
