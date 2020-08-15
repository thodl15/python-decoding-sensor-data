# STL Imports
from datetime import date, datetime

class HouseInfo():
    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area=0):
        field_data = []

        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record[field])

        return field_data

    def get_data_by_date(self, field, rec_date=date.today()):
        # Note: Step 4
        # I am concerned that the expression used in the
        # default parameter value will only evaluate once.
        # However, the test code explicitly checks to see
        # if I had set it to be that value, so I had to use
        # it as such.

        # Example:
        # def foo(rand=random.randint(3, 5000)):
        #     print(rand)
        #
        # The function above will always print the same
        # "default" value, even though the logical intention
        # is to produce some random value between 3 and 5000
        # each time the default is called.

        # if rec_date is None:
        #     rec_date = date.today()

        field_data = []

        for record in self.data:
            # Step 5
            # Worded very strangely; there was only a sublte
            # change in phrasing when referring to indices that
            # were "string" keys, versus ones that were meant
            # to be referenced as a variable.
            if rec_date.strftime("%m/%d/%y") == record['date']:
                field_data.append(record[field])

        return field_data
