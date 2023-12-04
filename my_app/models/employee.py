from my_app.app import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(100))
    birth_date = db.Column(db.DateTime)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))

    workstation = db.relationship('Workstation', backref='workstation_emp', lazy=True)
    issued_equipment = db.relationship('IssuedEquipment', backref='issued_equipment_emp', lazy=True)

    def __repr__(self):
        return f"<Employee {self.name} {self.last_name}>"

    @staticmethod
    def create_employee(name, last_name, birth_date, email, phone, position_id, team_id):
        new_employee = Employee(name=name, last_name=last_name, birth_date=birth_date,
                                email=email, phone=phone, position_id=position_id, team_id=team_id)
        db.session.add(new_employee)
        db.session.commit()
        return new_employee

    @staticmethod
    def get_all_employees():
        return Employee.query.all()

    @staticmethod
    def get_employee_by_id(employee_id):
        return Employee.query.get(employee_id)

    def update_employee(self, name, last_name, birth_date, email, phone, position_id, team_id):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email
        self.phone = phone
        self.position_id = position_id
        self.team_id = team_id
        db.session.commit()
        return self

    @staticmethod
    def delete_employee(employee_id):
        employee = Employee.query.get(employee_id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return True
        return False
