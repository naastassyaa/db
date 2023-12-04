from my_app.app import db


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position_name = db.Column(db.String(45))
    salary = db.Column(db.Float(precision=2))
    employment_type = db.Column(db.Enum('Повна', 'Часткова'))
    experience_required = db.Column(db.Integer)
    employee = db.relationship('Employee', backref='employee_pos', lazy=True)

    def __repr__(self):
        return f"<Position {self.position_name}>"

    @staticmethod
    def create_position(name, salary, employment_type, experience_required):
        new_position = Position(position_name=name, salary=salary, employment_type=employment_type,
                                experience_required=experience_required)
        db.session.add(new_position)
        db.session.commit()
        return new_position

    @staticmethod
    def get_all_positions():
        return Position.query.all()

    @staticmethod
    def get_position_by_id(position_id):
        return Position.query.get(position_id)

    def update_position(self, name, salary, employment_type, experience_required):
        self.position_name = name
        self.salary = salary
        self.employment_type = employment_type
        self.experience_required = experience_required
        db.session.commit()
        return self

    @staticmethod
    def delete_position(position_id):
        position = Position.query.get(position_id)
        if position:
            db.session.delete(position)
            db.session.commit()
            return True
        return False

