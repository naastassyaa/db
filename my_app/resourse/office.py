from flask import request, jsonify
from models import Office, Workstation
from my_app.app import app


@app.route('/offices', methods=['POST'])
def create_office():
    data = request.get_json()
    office_name = data.get('office_name')
    address_id = data.get('address_id')

    if not office_name or not address_id:
        return jsonify({'error': 'Please provide both office_name and address_id'}), 400

    new_office = Office.create_office(office_name, address_id)
    return jsonify({'message': 'Office created successfully', 'office_id': new_office.id}), 201


@app.route('/offices', methods=['GET'])
def get_all_offices():
    offices = Office.get_all_offices()
    office_list = [{'id': office.id, 'office_name': office.office_name, 'address_id': office.address_id} for
                   office in offices]
    return jsonify(office_list)


@app.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    office = Office.get_office_by_id(office_id)
    if office:
        return jsonify({'id': office.id, 'office_name': office.office_name, 'address_id': office.address_id})
    return jsonify({'error': 'Office not found'}), 404


@app.route('/offices/<int:office_id>', methods=['PUT'])
def update_office(office_id):
    data = request.get_json()
    new_office_name = data.get('office_name')
    new_address_id = data.get('address_id')

    if not new_office_name or not new_address_id:
        return jsonify({'error': 'Please provide both office_name and address_id'}), 400

    office = Office.get_office_by_id(office_id)
    updated_office = office.update_office(new_office_name, new_address_id)
    if updated_office:
        return jsonify({'message': 'Office updated successfully', 'office_id': updated_office.id})
    return jsonify({'error': 'Office not found'}), 404


@app.route('/offices/<int:office_id>', methods=['DELETE'])
def delete_office(office_id):
    deleted = Office.delete_office(office_id)
    if deleted:
        return jsonify({'message': 'Office deleted successfully'})
    return jsonify({'error': 'Office not found'}), 404


@app.route('/offices/<int:office_id>/workstations', methods=['GET'])
def get_workstations_for_office(office_id):
    office = Office.query.get(office_id)
    if not office:
        return jsonify({'error': 'Office not found'}), 404
    workstations = office.workstation
    workstation_list = [{'id': ws.id, 'workstation_name': ws.workstation_name, 'employee_id': ws.employee_id, 'office_id': ws.office_id}
                        for ws in workstations]
    return jsonify(workstation_list)
