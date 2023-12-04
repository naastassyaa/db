from my_app.app import db


class IssuedEquipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    workstation_id = db.Column(db.Integer, db.ForeignKey('workstation.id'))

    def __repr__(self):
        return f"<IssuedEquipment {self.id}>"

    @staticmethod
    def create_issued_equipment(issue_date, return_date, employee_id, equipment_id, workstation_id):
        new_issued_equipment = IssuedEquipment(issue_date=issue_date, return_date=return_date,
                                               employee_id=employee_id, equipment_id=equipment_id,
                                               workstation_id=workstation_id)
        db.session.add(new_issued_equipment)
        db.session.commit()
        return new_issued_equipment

    @staticmethod
    def get_all_issued_equipments():
        return IssuedEquipment.query.all()

    @staticmethod
    def get_issued_equipment_by_id(issued_equipment_id):
        return IssuedEquipment.query.get(issued_equipment_id)

    def update_issued_equipment(self, issue_date, return_date, employee_id, equipment_id, workstation_id):
        self.issue_date = issue_date
        self.return_date = return_date
        self.employee_id = employee_id
        self.equipment_id = equipment_id
        self.workstation_id = workstation_id
        db.session.commit()
        return self

    @staticmethod
    def delete_issued_equipment(issued_equipment_id):
        issued_equipment = IssuedEquipment.query.get(issued_equipment_id)
        if issued_equipment:
            db.session.delete(issued_equipment)
            db.session.commit()
            return True
        return False
