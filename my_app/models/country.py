from my_app.app import db


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(45))
    capital_city = db.Column(db.String(45))
    city = db.relationship('City', backref='city', lazy=True)

    def __repr__(self):
        return f"<Country {self.country_name}>"

    @staticmethod
    def create_country(country_name, capital_city):
        new_country = Country(country_name=country_name, capital_city=capital_city)
        db.session.add(new_country)
        db.session.commit()
        return new_country

    @staticmethod
    def get_all_countries():
        return Country.query.all()

    @staticmethod
    def get_country_by_id(country_id):
        return Country.query.get(country_id)

    def update_country(self, new_country_name, new_capital_city):
        self.country_name = new_country_name
        self.capital_city = new_capital_city
        db.session.commit()
        return self

    @staticmethod
    def delete_country(country_id):
        country = Country.query.get(country_id)
        if country:
            db.session.delete(country)
            db.session.commit()
            return True
        return False
