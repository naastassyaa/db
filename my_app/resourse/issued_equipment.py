from flask import request, jsonify
from models import IssuedEquipment
from my_app.app import app


@app.route('/issued_equipments', methods=['POST'])
def create_issued_equipment():
    data = request.get_json()
    issue_date = data.get('issue_date')
    return_date = data.get('return_date')
    employee_id = data.get('employee_id')
    equipment_id = data.get('equipment_id')
    workstation_id = data.get('workstation_id')

    if not all([issue_date, return_date, employee_id, equipment_id, workstation_id]):
        return jsonify({'error': 'Please provide all required fields'}), 400

    new_issued_equipment = IssuedEquipment.create_issued_equipment(issue_date, return_date, employee_id, equipment_id,
                                                                   workstation_id)
    return jsonify(
        {'message': 'Issued equipment created successfully', 'issued_equipment_id': new_issued_equipment.id}), 201


@app.route('/issued_equipments', methods=['GET'])
def get_all_issued_equipments():
    issued_equipments = IssuedEquipment.get_all_issued_equipments()
    issued_equipment_list = [{'id': eq.id, 'issue_date': eq.issue_date, 'return_date': eq.return_date,
                              'employee_id': eq.employee_id, 'equipment_id': eq.equipment_id,
                              'workstation_id': eq.workstation_id} for eq in issued_equipments]
    return jsonify(issued_equipment_list)


@app.route('/issued_equipments/<int:issued_equipment_id>', methods=['GET'])
def get_issued_equipment(issued_equipment_id):
    issued_equipment = IssuedEquipment.get_issued_equipment_by_id(issued_equipment_id)
    if issued_equipment:
        return jsonify({'id': issued_equipment.id, 'issue_date': issued_equipment.issue_date,
                        'return_date': issued_equipment.return_date, 'employee_id': issued_equipment.employee_id,
                        'equipment_id': issued_equipment.equipment_id,
                        'workstation_id': issued_equipment.workstation_id})
    return jsonify({'error': 'Issued equipment not found'}), 404


@app.route('/issued_equipments/<int:issued_equipment_id>', methods=['PUT'])
def update_issued_equipment(issued_equipment_id):
    data = request.get_json()
    issue_date = data.get('issue_date')
    return_date = data.get('return_date')
    employee_id = data.get('employee_id')
    equipment_id = data.get('equipment_id')
    workstation_id = data.get('workstation_id')

    if not all([issue_date, return_date, employee_id, equipment_id, workstation_id]):
        return jsonify({'error': 'Please provide all required fields'}), 400

    issued_equipment = IssuedEquipment.get_issued_equipment_by_id(issued_equipment_id)
    if issued_equipment:
        updated_issued_equipment = issued_equipment.update_issued_equipment(issue_date, return_date, employee_id,
                                                                            equipment_id, workstation_id)
        return jsonify(
            {'message': 'Issued equipment updated successfully', 'issued_equipment_id': updated_issued_equipment.id})
    return jsonify({'error': 'Issued equipment not found'}), 404


@app.route('/issued_equipments/<int:issued_equipment_id>', methods=['DELETE'])
def delete_issued_equipment(issued_equipment_id):
    deleted = IssuedEquipment.delete_issued_equipment(issued_equipment_id)
    if deleted:
        return jsonify({'message': 'Issued equipment deleted successfully'})
    return jsonify({'error': 'Issued equipment not found'}), 404
