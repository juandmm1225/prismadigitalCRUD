from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Bill import Bill
# Models
from models.BillModel import BillModel

main = Blueprint('bill_blueprint', __name__)


@main.route('/')
def get_bills():
    try:
        bills = BillModel.get_bills()
        return jsonify(bills)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_bill(id):
    try:
        bill = BillModel.get_bill(id)
        if bill != None:
            return jsonify(bill)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_bill():
    try:
        id = int(request.json['id'])
        date_bill = request.json['date_bill']
        user_id = int(request.json['user_id'])
        value = int(request.json['value'])
        type = int(request.json['type'])
        observation = request.json['observation']
        bill = Bill( id,date_bill, user_id, value, type, observation)

        affected_rows = BillModel.add_bill(bill)

        if affected_rows == 1:
            return jsonify(bill.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_bill(id):
    try:
         date_bill = request.json['date_bill']
         user_id = int(request.json['user_id'])
         value = int(request.json['value'])
         type = int(request.json['type'])
         observation = request.json['observation']
         bill = Bill( id,date_bill, user_id, value, type, observation)

         affected_rows = BillModel.update_bill(bill)

         if affected_rows == 1:
            return jsonify(bill.id)
         else:
            return jsonify({'message': "No bill updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_bill(id):
    try:
        bill = Bill(id)

        affected_rows = BillModel.delete_bill(bill)

        if affected_rows == 1:
            return jsonify(bill.id)
        else:
            return jsonify({'message': "No bill deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500