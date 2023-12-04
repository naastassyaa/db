from my_app.app import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(45))
    creation_date = db.Column(db.DateTime)
    employee = db.relationship('Employee', backref='employee', lazy=True)

    def __repr__(self):
        return f"<Team {self.team_name}>"

    @staticmethod
    def create_team(team_name, creation_date):
        new_team = Team(team_name=team_name, creation_date=creation_date)
        db.session.add(new_team)
        db.session.commit()
        return new_team

    @staticmethod
    def get_all_teams():
        return Team.query.all()

    @staticmethod
    def get_team_by_id(team_id):
        return Team.query.get(team_id)

    def update_team(self, new_team_name, new_creation_date):
        self.team_name = new_team_name
        self.creation_date = new_creation_date
        db.session.commit()
        return self

    @staticmethod
    def delete_team(team_id):
        team = Team.query.get(team_id)
        if team:
            db.session.delete(team)
            db.session.commit()
            return True
        return False
