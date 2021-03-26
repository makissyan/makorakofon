class Currency:
    def __init__(self, name, date, b_rate, s_rate):
        self.name = name
        self.date = date
        self.b_rate = b_rate
        self.s_rate = s_rate

    def get_info(self):
        return "{}: {} / {}\n".format(self.name, self.b_rate, self.s_rate)