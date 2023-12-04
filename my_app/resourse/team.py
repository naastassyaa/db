from flask import request, jsonify
from models import Team
from my_app.app import app


@app.route('/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    team_name = data.get('team_name')
    creation_date = data.get('creation_date')

    if not team_name or not creation_date:
        return jsonify({'error': 'Please provide both team_name and creation_date'}), 400

    new_team = Team.create_team(team_name, creation_date)
    return jsonify({'message': 'Team created successfully', 'team_id': new_team.id}), 201


@app.route('/teams', methods=['GET'])
def get_all_teams():
    teams = Team.get_all_teams()
    team_list = [{'id': team.id, 'team_name': team.team_name, 'creation_date': team.creation_date} for
                 team in teams]
    return jsonify(team_list)


@app.route('/teams/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = Team.get_team_by_id(team_id)
    if team:
        return jsonify({'id': team.id, 'team_name': team.team_name, 'creation_date': team.creation_date})
    return jsonify({'error': 'Team not found'}), 404


@app.route('/teams/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    data = request.get_json()
    new_team_name = data.get('team_name')
    new_creation_date = data.get('creation_date')

    if not new_team_name or not new_creation_date:
        return jsonify({'error': 'Please provide both team_name and creation_date'}), 400

    team = Team.get_team_by_id(team_id)
    updated_team = team.update_team(new_team_name, new_creation_date)
    if updated_team:
        return jsonify({'message': 'Team updated successfully', 'team_id': updated_team.id})
    return jsonify({'error': 'Team not found'}), 404


@app.route('/teams/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    deleted = Team.delete_team(team_id)
    if deleted:
        return jsonify({'message': 'Team deleted successfully'})
    return jsonify({'error': 'Team not found'}), 404


@app.route('/teams/<int:team_id>/employees', methods=['GET'])
def get_employees_by_team(team_id):
    team = Team.query.get(team_id)
    if not team:
        return jsonify({'error': 'Team not found'})
    employees = team.employee
    employee_list = [{'id': emp.id, 'name': emp.name, 'last_name': emp.last_name, 'birth_date': emp.birth_date,
                      'email': emp.email, 'phone': emp.phone, 'position_id': emp.position_id, 'team_id': emp.team_id}
                     for emp in employees]
    return jsonify(employee_list)
