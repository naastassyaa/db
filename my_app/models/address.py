from my_app.app import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(100))
    house_number = db.Column(db.Integer)
    flat_number = db.Column(db.Integer)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    office = db.relationship('Office', backref='office', lazy=True)

    def __repr__(self):
        return f"<Address {self.street} {self.house_number} {self.flat_number}>"

    @staticmethod
    def create_address(street, house_number, flat_number, city_id):
        new_address = Address(street=street, house_number=house_number, flat_number=flat_number, city_id=city_id)
        db.session.add(new_address)
        db.session.commit()
        return new_address

    @staticmethod
    def get_all_addresses():
        return Address.query.all()

    @staticmethod
    def get_address_by_id(address_id):
        return Address.query.get(address_id)

    def update_address(self, street, house_number, flat_number, city_id):
        self.street = street
        self.house_number = house_number
        self.flat_number = flat_number
        self.city_id = city_id
        db.session.commit()
        return self

    @staticmethod
    def delete_address(address_id):
        address = Address.query.get(address_id)
        if address:
            db.session.delete(address)
            db.session.commit()
            return True
        return False
