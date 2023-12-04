from my_app.app import db


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_name = db.Column(db.String(100))
    equipment_type = db.Column(db.String(15))
    equipment_brand = db.Column(db.String(50))
    equipment_model = db.Column(db.String(45))
    purchase_date = db.Column(db.DateTime)
    purchase_price = db.Column(db.Float(precision=2))
    issued_equipment = db.relationship('IssuedEquipment', backref='issued_equipment', lazy=True)

    def __repr__(self):
        return f"<Equipment {self.equipment_name}>"

    @staticmethod
    def create_equipment(name, type, brand, model, purchase_date, purchase_price):
        new_equipment = Equipment(
            equipment_name=name,
            equipment_type=type,
            equipment_brand=brand,
            equipment_model=model,
            purchase_date=purchase_date,
            purchase_price=purchase_price
        )
        db.session.add(new_equipment)
        db.session.commit()
        return new_equipment

    @staticmethod
    def get_all_equipment():
        return Equipment.query.all()

    @staticmethod
    def get_equipment_by_id(equipment_id):
        return Equipment.query.get(equipment_id)

    def update_equipment(self, name, type, brand, model, purchase_date, purchase_price):
        self.equipment_name = name
        self.equipment_type = type
        self.equipment_brand = brand
        self.equipment_model = model
        self.purchase_date = purchase_date
        self.purchase_price = purchase_price
        db.session.commit()
        return self

    @staticmethod
    def delete_equipment(equipment_id):
        equipment = Equipment.query.get(equipment_id)
        if equipment:
            db.session.delete(equipment)
            db.session.commit()
            return True
        return False

