class Emailing():
    def __init__(self, subcriber_info_list):
        self.email = subcriber_info_list[0]
        self.name = subcriber_info_list[1]
        self.departure = subcriber_info_list[2]
        self.arrival = subcriber_info_list[3]
        self.date = subcriber_info_list[4]
        self.airline = subcriber_info_list[5]
        self.time = subcriber_info_list[6]
        self.price = subcriber_info_list[7]

    def to_string(self):
        date_time = self.date.strftime("%Y/%M/%D")
        print("Hi %s! /n Your flight from %s to %s at the day %s with %s which have %s",
              self.name,self.departure,self.arrival,date_time,self.airline,self.price)
