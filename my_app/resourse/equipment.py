from flask import request, jsonify
from models import Equipment
from my_app.app import app


@app.route('/equipment', methods=['POST'])
def create_equipment():
    data = request.get_json()
    name = data.get('equipment_name')
    type = data.get('equipment_type')
    brand = data.get('equipment_brand')
    model = data.get('equipment_model')
    purchase_date = data.get('purchase_date')
    purchase_price = data.get('purchase_price')

    if not all([name, type, brand, model, purchase_date, purchase_price]):
        return jsonify({'error': 'Please provide all equipment details'}), 400

    new_equipment = Equipment.create_equipment(name, type, brand, model, purchase_date, purchase_price)
    return jsonify({'message': 'Equipment created successfully', 'equipment_id': new_equipment.id}), 201


@app.route('/equipment', methods=['GET'])
def get_all_equipment():
    equipment = Equipment.get_all_equipment()
    equipment_list = [{'id': e.id, 'equipment_name': e.equipment_name, 'equipment_type': e.equipment_type,
                       'equipment_brand': e.equipment_brand, 'equipment_model': e.equipment_model,
                       'purchase_date': e.purchase_date.strftime('%Y-%m-%d') if e.purchase_date else None,
                       'purchase_price': e.purchase_price} for e in equipment]
    return jsonify(equipment_list)


@app.route('/equipment/<int:equipment_id>', methods=['GET'])
def get_equipment(equipment_id):
    equipment = Equipment.get_equipment_by_id(equipment_id)
    if equipment:
        return jsonify({'id': equipment.id, 'equipment_name': equipment.equipment_name,
                        'equipment_type': equipment.equipment_type, 'equipment_brand': equipment.equipment_brand,
                        'equipment_model': equipment.equipment_model,
                        'purchase_date': equipment.purchase_date.strftime('%Y-%m-%d')
                        if equipment.purchase_date else None,
                        'purchase_price': equipment.purchase_price})
    return jsonify({'error': 'Equipment not found'}), 404


@app.route('/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    data = request.get_json()
    name = data.get('equipment_name')
    type = data.get('equipment_type')
    brand = data.get('equipment_brand')
    model = data.get('equipment_model')
    purchase_date = data.get('purchase_date')
    purchase_price = data.get('purchase_price')

    if not all([name, type, brand, model, purchase_date, purchase_price]):
        return jsonify({'error': 'Please provide all equipment details'}), 400

    equipment = Equipment.get_equipment_by_id(equipment_id)
    updated_equipment = equipment.update_equipment(name, type, brand, model, purchase_date, purchase_price)
    if updated_equipment:
        return jsonify({'message': 'Equipment updated successfully', 'equipment_id': updated_equipment.id})
    return jsonify({'error': 'Equipment not found'}), 404


@app.route('/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    deleted = Equipment.delete_equipment(equipment_id)
    if deleted:
        return jsonify({'message': 'Equipment deleted successfully'})
    return jsonify({'error': 'Equipment not found'}), 404


@app.route('/equipments/<int:equipment_id>/issued_equipments')
def get_issued_equipments_for_equipment(equipment_id):
    equipment = Equipment.query.get(equipment_id)
    if not equipment:
        return jsonify({'error': 'Equipment not found'}), 404
    issued_equipments = equipment.issued_equipment
    issued_equipment_list = [{'id': eq.id, 'issue_date': eq.issue_date, 'return_date': eq.return_date,
                              'employee_id': eq.employee_id, 'equipment_id': eq.equipment_id,
                              'workstation_id': eq.workstation_id} for eq in issued_equipments]
    return jsonify(issued_equipment_list)
