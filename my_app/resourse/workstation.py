from flask import request, jsonify
from models import Workstation
from my_app.app import app


@app.route('/workstations', methods=['POST'])
def create_workstation():
    data = request.get_json()
    name = data.get('workstation_name')
    employee_id = data.get('employee_id')
    office_id = data.get('office_id')

    if not all([name, employee_id, office_id]):
        return jsonify({'error': 'Please provide all required fields'}), 400

    new_workstation = Workstation.create_workstation(name, employee_id, office_id)
    return jsonify({'message': 'Workstation created successfully', 'workstation_id': new_workstation.id}), 201


@app.route('/workstations', methods=['GET'])
def get_all_workstations():
    workstations = Workstation.get_all_workstations()
    workstation_list = [{'id': ws.id, 'workstation_name': ws.workstation_name,
                         'employee_id': ws.employee_id, 'office_id': ws.office_id}
                        for ws in workstations]
    return jsonify(workstation_list)


@app.route('/workstations/<int:workstation_id>', methods=['GET'])
def get_workstation(workstation_id):
    workstation = Workstation.get_workstation_by_id(workstation_id)
    if workstation:
        return jsonify({'id': workstation.id, 'workstation_name': workstation.workstation_name,
                        'employee_id': workstation.employee_id, 'office_id': workstation.office_id})
    return jsonify({'error': 'Workstation not found'}), 404


@app.route('/workstations/<int:workstation_id>', methods=['PUT'])
def update_workstation(workstation_id):
    data = request.get_json()
    name = data.get('workstation_name')
    employee_id = data.get('employee_id')
    office_id = data.get('office_id')

    if not all([name, employee_id, office_id]):
        return jsonify({'error': 'Please provide all required fields'}), 400

    workstation = Workstation.get_workstation_by_id(workstation_id)
    if workstation:
        updated_workstation = workstation.update_workstation(name, employee_id, office_id)
        return jsonify({'message': 'Workstation updated successfully', 'workstation_id': updated_workstation.id})
    return jsonify({'error': 'Workstation not found'}), 404


@app.route('/workstations/<int:workstation_id>', methods=['DELETE'])
def delete_workstation(workstation_id):
    deleted = Workstation.delete_workstation(workstation_id)
    if deleted:
        return jsonify({'message': 'Workstation deleted successfully'})
    return jsonify({'error': 'Workstation not found'}), 404


@app.route('/workstations/<int:workstation_id>/issued_equipments')
def get_issued_equipments_for_workstation(workstation_id):
    workstation = Workstation.query.get(workstation_id)
    if not workstation:
        return jsonify({'error': 'Workstation not found'}), 404
    issued_equipments = workstation.issued_equipment
    issued_equipment_list = [{'id': eq.id, 'issue_date': eq.issue_date, 'return_date': eq.return_date,
                              'employee_id': eq.employee_id, 'equipment_id': eq.equipment_id,
                              'workstation_id': eq.workstation_id} for eq in issued_equipments]
    return jsonify(issued_equipment_list)
