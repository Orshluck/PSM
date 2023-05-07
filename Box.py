class Box:
    def __init__(self,value):
        self.value = value
        self.temporary_value = 0
        self.age = 1


    def grow_old(self):
        self.age += 1

    def get_age(self):
        return self.age
    def get_value(self):
        return self.value
    def get_temporary_value(self):
        return self.temporary_value
    def set_value(self,value):
        self.value = value
    def set_t_value(self, value):
        self.temporary_value = value
    def correct_value(self):
        self.value = self.temporary_value