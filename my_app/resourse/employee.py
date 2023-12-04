from flask import request, jsonify

from models import Employee
from my_app.app import app


@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    name = data.get('name')
    last_name = data.get('last_name')
    birth_date = data.get('birth_date')
    email = data.get('email')
    phone = data.get('phone')
    position_id = data.get('position_id')
    team_id = data.get('team_id')

    if not all([name, last_name, birth_date, email, phone, position_id, team_id]):
        return jsonify({'error': 'Please provide all required fields'}), 400

    new_employee = Employee.create_employee(name, last_name, birth_date, email, phone, position_id, team_id)
    return jsonify({'message': 'Employee created successfully', 'employee_id': new_employee.id}), 201


@app.route('/employees', methods=['GET'])
def get_all_employees():
    employees = Employee.get_all_employees()
    employee_list = [{'id': emp.id, 'name': emp.name, 'last_name': emp.last_name, 'birth_date': emp.birth_date,
                      'email': emp.email, 'phone': emp.phone, 'position_id': emp.position_id, 'team_id': emp.team_id}
                     for emp in employees]
    return jsonify(employee_list)


@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = Employee.get_employee_by_id(employee_id)
    if employee:
        return jsonify({'id': employee.id, 'name': employee.name, 'last_name': employee.last_name,
                        'birth_date': employee.birth_date, 'email': employee.email, 'phone': employee.phone,
                        'position_id': employee.position_id, 'team_id': employee.team_id})
    return jsonify({'error': 'Employee not found'}), 404


@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.get_json()
    name = data.get('name')
    last_name = data.get('last_name')
    birth_date = data.get('birth_date')
    email = data.get('email')
    phone = data.get('phone')
    position_id = data.get('position_id')
    team_id = data.get('team_id')

    if not all([name, last_name, birth_date, email, phone, position_id, team_id]):
        return jsonify({'error': 'Please provide all required fields'}), 400

    employee = Employee.get_employee_by_id(employee_id)
    if employee:
        updated_employee = employee.update_employee(name, last_name, birth_date, email, phone, position_id, team_id)
        return jsonify({'message': 'Employee updated successfully', 'employee_id': updated_employee.id})
    return jsonify({'error': 'Employee not found'}), 404


@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    deleted = Employee.delete_employee(employee_id)
    if deleted:
        return jsonify({'message': 'Employee deleted successfully'})
    return jsonify({'error': 'Employee not found'}), 404


@app.route('/employees/<int:employee_id>/workstations', methods=['GET'])
def get_workstations_for_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'error': 'Employee not found'}), 404
    workstations = employee.workstation
    workstation_list = [
        {'id': ws.id, 'workstation_name': ws.workstation_name, 'employee_id': ws.employee_id, 'office_id': ws.office_id}
        for ws in workstations]
    return jsonify(workstation_list)


@app.route('/employees/<int:employee_id>/issued_equipments')
def get_issued_equipments_for_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'error': 'Employee not found'}), 404
    issued_equipments = employee.issued_equipment
    issued_equipment_list = [{'id': eq.id, 'issue_date': eq.issue_date, 'return_date': eq.return_date,
                              'employee_id': eq.employee_id, 'equipment_id': eq.equipment_id,
                              'workstation_id': eq.workstation_id} for eq in issued_equipments]
    return jsonify(issued_equipment_list)
