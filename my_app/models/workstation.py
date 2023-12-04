from my_app.app import db


class Workstation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workstation_name = db.Column(db.String(45))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    office_id = db.Column(db.Integer, db.ForeignKey('office.id'))
    issued_equipment = db.relationship('IssuedEquipment', backref='issued_equipment_wrk', lazy=True)

    def __repr__(self):
        return f"<Workstation {self.workstation_name}>"

    @staticmethod
    def create_workstation(name, employee_id, office_id):
        new_workstation = Workstation(workstation_name=name, employee_id=employee_id, office_id=office_id)
        db.session.add(new_workstation)
        db.session.commit()
        return new_workstation

    @staticmethod
    def get_all_workstations():
        return Workstation.query.all()

    @staticmethod
    def get_workstation_by_id(workstation_id):
        return Workstation.query.get(workstation_id)

    def update_workstation(self, name, employee_id, office_id):
        self.workstation_name = name
        self.employee_id = employee_id
        self.office_id = office_id
        db.session.commit()
        return self

    @staticmethod
    def delete_workstation(workstation_id):
        workstation = Workstation.query.get(workstation_id)
        if workstation:
            db.session.delete(workstation)
            db.session.commit()
            return True
        return False
