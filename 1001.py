class Animals:
    this_is_a_property = {
        'key 1': 'Value'
    }
    this_list = ['Kane', 'Kan', 'Gully']

    def add_name(self, name):
        self.this_list.append(name)
        return self.this_list

    def this_is_method(self):
        print(self.this_list)

    @property
    def get_gully(self):
        return self.this_list[2]


the_animal = Animals()
the_animal.this_is_method()
gully = the_animal.get_gully
print("The cutest go of all time is", gully)
