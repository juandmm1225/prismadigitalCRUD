from database.db import get_connection
from .entities.Bill import Bill


class BillModel():

    @classmethod
    def get_bills(self):
        try:
            connection = get_connection()
            bills = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, date_bill, user_id, value, type, observation FROM bill ORDER BY date_bill ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    bill = Bill(row[0], row[1], row[2], row[3],row[4],row[5])
                    bills.append(bill.to_JSON())

            connection.close()
            return bills
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_bill(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, date_bill, user_id, value, type, observation FROM bill WHERE id = %s", (id,))
                row = cursor.fetchone()

                bill = None
                if row != None:
                    bill = Bill(row[0], row[1], row[2], row[3],row[4],row[5])
                    bills = bill.to_JSON()

            connection.close()
            return bills
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_bill(self, bill):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO bill (id, date_bill, user_id, value, type, observation) 
                                VALUES (%s, %s, %s, %s,%s,%s)""", (bill.id, bill.date_bill, bill.user_id, bill.value,bill.type,bill.observation))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_bill(self, bill):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE bill SET date_bill = %s, user_id = %s, value = %s, type = %s, observation = %s 
                                WHERE id = %s""", (bill.date_bill, bill.user_id, bill.value,bill.type,bill.observation, bill.id ))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_bill(self, bill):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM bill WHERE id = %s", (bill.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)