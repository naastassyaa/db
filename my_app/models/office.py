from my_app.app import db


class Office(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    office_name = db.Column(db.String(45))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    workstation = db.relationship('Workstation', backref='workstation', lazy=True)

    def __repr__(self):
        return f"<Office {self.office_name}>"

    @staticmethod
    def create_office(office_name, address_id):
        new_office = Office(office_name=office_name, address_id=address_id)
        db.session.add(new_office)
        db.session.commit()
        return new_office

    @staticmethod
    def get_all_offices():
        return Office.query.all()

    @staticmethod
    def get_office_by_id(office_id):
        return Office.query.get(office_id)

    def update_office(self, new_office_name, new_address_id):
        self.office_name = new_office_name
        self.address_id = new_address_id
        db.session.commit()
        return self

    @staticmethod
    def delete_office(office_id):
        office = Office.query.get(office_id)
        if office:
            db.session.delete(office)
            db.session.commit()
            return True
        return False
