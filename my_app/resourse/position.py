from flask import request, jsonify
from models import Position
from my_app.app import app


@app.route('/positions', methods=['POST'])
def create_position():
    data = request.get_json()
    name = data.get('position_name')
    salary = data.get('salary')
    employment_type = data.get('employment_type')
    experience_required = data.get('experience_required')

    if not name or not salary or not employment_type or not experience_required:
        return jsonify({'error': 'Please provide all required fields'}), 400

    new_position = Position.create_position(name, salary, employment_type, experience_required)
    return jsonify({'message': 'Position created successfully', 'position_id': new_position.id}), 201


@app.route('/positions', methods=['GET'])
def get_all_positions():
    positions = Position.get_all_positions()
    position_list = [{'id': position.id, 'position_name': position.position_name, 'salary': position.salary,
                      'employment_type': position.employment_type, 'experience_required': position.experience_required}
                     for
                     position in positions]
    return jsonify(position_list)


@app.route('/positions/<int:position_id>', methods=['GET'])
def get_position(position_id):
    position = Position.get_position_by_id(position_id)
    if position:
        return jsonify({'id': position.id, 'position_name': position.position_name, 'salary': position.salary,
                        'employment_type': position.employment_type,
                        'experience_required': position.experience_required})
    return jsonify({'error': 'Position not found'}), 404


@app.route('/positions/<int:position_id>', methods=['PUT'])
def update_position(position_id):
    data = request.get_json()
    name = data.get('position_name')
    salary = data.get('salary')
    employment_type = data.get('employment_type')
    experience_required = data.get('experience_required')

    if not name or not salary or not employment_type or not experience_required:
        return jsonify({'error': 'Please provide all required fields'}), 400

    position = Position.get_position_by_id(position_id)
    updated_position = position.update_position(name, salary, employment_type, experience_required)
    if updated_position:
        return jsonify({'message': 'Position updated successfully', 'position_id': updated_position.id})
    return jsonify({'error': 'Position not found'}), 404


@app.route('/positions/<int:position_id>', methods=['DELETE'])
def delete_position(position_id):
    deleted = Position.delete_position(position_id)
    if deleted:
        return jsonify({'message': 'Position deleted successfully'})
    return jsonify({'error': 'Position not found'}), 404


@app.route('/positions/<int:position_id>/employees', methods=['GET'])
def get_employees_by_position(position_id):
    position = Position.query.get(position_id)
    if not position:
        return jsonify({'error': 'Position not found'})
    employees = position.employee
    employee_list = [{'id': emp.id, 'name': emp.name, 'last_name': emp.last_name, 'birth_date': emp.birth_date,
                      'email': emp.email, 'phone': emp.phone, 'position_id': emp.position_id, 'team_id': emp.team_id}
                     for emp in employees]
    return jsonify(employee_list)

