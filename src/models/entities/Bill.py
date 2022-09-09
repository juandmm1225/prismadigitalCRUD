from utils.DateFormat import DateFormat

class Bill():

    def __init__(self, id, date_bill=None, user_id=None, value=None, type=None, observation=None) -> None:
        self.id = id
        self.date_bill = date_bill
        self.user_id = user_id
        self.value = value
        self.type = type
        self.observation = observation

    def to_JSON(self):
        return {
            'id': self.id,
            'date_bill': DateFormat.convert_date(self.date_bill),
            'user_id': self.user_id,
            'value': self.value,
            'type': self.type,
            'observation': self.observation
        }