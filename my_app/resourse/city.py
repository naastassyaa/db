from flask import request, jsonify
from models import City, Address
from my_app.app import app


@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    city_name = data.get('city_name')
    time_zone = data.get('time_zone')
    country_id = data.get('country_id')

    if not city_name or not time_zone or not country_id:
        return jsonify({'error': 'Please provide city_name, time_zone, and country_id'}), 400

    new_city = City.create_city(city_name, time_zone, country_id)
    return jsonify({'message': 'City created successfully', 'city_id': new_city.id}), 201


@app.route('/cities', methods=['GET'])
def get_all_cities():
    cities = City.get_all_cities()
    city_list = [
        {'id': city.id, 'city_name': city.city_name, 'time_zone': city.time_zone, 'country_id': city.country_id} for
        city in cities]
    return jsonify(city_list)


@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = City.get_city_by_id(city_id)
    if city:
        return jsonify(
            {'id': city.id, 'city_name': city.city_name, 'time_zone': city.time_zone, 'country_id': city.country_id})
    return jsonify({'error': 'City not found'}), 404


@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.get_json()
    new_city_name = data.get('city_name')
    new_time_zone = data.get('time_zone')
    new_country_id = data.get('country_id')

    if not new_city_name or not new_time_zone or not new_country_id:
        return jsonify({'error': 'Please provide city_name, time_zone, and country_id'}), 400

    city = City.get_city_by_id(city_id)
    updated_city = city.update_city(new_city_name, new_time_zone, new_country_id)
    if updated_city:
        return jsonify({'message': 'City updated successfully', 'city_id': updated_city.id})
    return jsonify({'error': 'City not found'}), 404


@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    deleted = City.delete_city(city_id)
    if deleted:
        return jsonify({'message': 'City deleted successfully'})
    return jsonify({'error': 'City not found'}), 404


@app.route('/cities/<int:city_id>/addresses', methods=['GET'])
def get_addresses_by_city(city_id):
    city = City.query.get(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    addresses = city.address
    address_list = [{'id': address.id, 'street': address.street, 'house_number': address.house_number,
                     'flat_number': address.flat_number, 'city_id': address.city_id}
                    for address in addresses]
    return jsonify(address_list)
