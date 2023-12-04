from flask import request, jsonify

from models import Country, City
from my_app.app import app


@app.route('/countries', methods=['POST'])
def create_country():
    data = request.get_json()
    country_name = data.get('country_name')
    capital_city = data.get('capital_city')

    if not country_name or not capital_city:
        return jsonify({'error': 'Please provide both country_name and capital_city'}), 400

    new_country = Country.create_country(country_name, capital_city)
    return jsonify({'message': 'Country created successfully', 'country_id': new_country.id}), 201


@app.route('/countries', methods=['GET'])
def get_all_countries():
    countries = Country.get_all_countries()
    country_list = [{'id': country.id, 'country_name': country.country_name, 'capital_city': country.capital_city} for
                    country in countries]
    return jsonify(country_list)


@app.route('/countries/<int:country_id>', methods=['GET'])
def get_country(country_id):
    country = Country.get_country_by_id(country_id)
    if country:
        return jsonify({'id': country.id, 'country_name': country.country_name, 'capital_city': country.capital_city})
    return jsonify({'error': 'Country not found'}), 404


@app.route('/countries/<int:country_id>', methods=['PUT'])
def update_country(country_id):
    data = request.get_json()
    new_country_name = data.get('country_name')
    new_capital_city = data.get('capital_city')

    if not new_country_name or not new_capital_city:
        return jsonify({'error': 'Please provide both country_name and capital_city'}), 400

    country = Country.get_country_by_id(country_id)
    updated_country = country.update_country(new_country_name, new_capital_city)
    if updated_country:
        return jsonify({'message': 'Country updated successfully', 'country_id': updated_country.id})
    return jsonify({'error': 'Country not found'}), 404


@app.route('/countries/<int:country_id>', methods=['DELETE'])
def delete_country(country_id):
    deleted = Country.delete_country(country_id)
    if deleted:
        return jsonify({'message': 'Country deleted successfully'})
    return jsonify({'error': 'Country not found'}), 404


@app.route('/countries/<int:country_id>/cities', methods=['GET'])
def get_cities_by_country(country_id):
    country = Country.query.get(country_id)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    cities = country.city
    city_list = [{'id': city.id, 'city_name': city.city_name, 'time_zone': city.time_zone}
                 for city in cities]
    return jsonify(city_list)
