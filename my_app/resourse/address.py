from flask import request, jsonify
from models import Address, Office
from my_app.app import app


@app.route('/addresses', methods=['POST'])
def create_address():
    data = request.get_json()
    street = data.get('street')
    house_number = data.get('house_number')
    flat_number = data.get('flat_number')
    city_id = data.get('city_id')

    if not street or not house_number or not city_id:
        return jsonify({'error': 'Please provide street, house_number, and city_id'}), 400

    new_address = Address.create_address(street, house_number, flat_number, city_id)
    return jsonify({'message': 'Address created successfully', 'address_id': new_address.id}), 201


@app.route('/addresses', methods=['GET'])
def get_all_addresses():
    addresses = Address.get_all_addresses()
    address_list = [{'id': address.id, 'street': address.street, 'house_number': address.house_number,
                     'flat_number': address.flat_number, 'city_id': address.city_id} for address in addresses]
    return jsonify(address_list)


@app.route('/addresses/<int:address_id>', methods=['GET'])
def get_address(address_id):
    address = Address.get_address_by_id(address_id)
    if address:
        return jsonify({'id': address.id, 'street': address.street, 'house_number': address.house_number,
                        'flat_number': address.flat_number, 'city_id': address.city_id})
    return jsonify({'error': 'Address not found'}), 404


@app.route('/addresses/<int:address_id>', methods=['PUT'])
def update_address(address_id):
    data = request.get_json()
    street = data.get('street')
    house_number = data.get('house_number')
    flat_number = data.get('flat_number')
    city_id = data.get('city_id')

    if not street or not house_number or not city_id:
        return jsonify({'error': 'Please provide street, house_number, and city_id'}), 400

    address = Address.get_address_by_id(address_id)
    updated_address = address.update_address(street, house_number, flat_number, city_id)
    if updated_address:
        return jsonify({'message': 'Address updated successfully', 'address_id': updated_address.id})
    return jsonify({'error': 'Address not found'}), 404


@app.route('/addresses/<int:address_id>', methods=['DELETE'])
def delete_address(address_id):
    deleted = Address.delete_address(address_id)
    if deleted:
        return jsonify({'message': 'Address deleted successfully'})
    return jsonify({'error': 'Address not found'}), 404


@app.route('/offices/address/<int:address_id>', methods=['GET'])
def get_offices_by_address(address_id):
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'error': 'Address not found'}), 404
    offices = address.office
    office_list = [{'id': office.id, 'office_name': office.office_name, 'address_id': office.address_id}
                   for office in offices]
    return jsonify(office_list)
