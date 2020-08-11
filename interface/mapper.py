class Mapper:
    def __init__(self):
        self.map_array = []

    def generate_map_array(self, my_level):
        my_map_file = "./maps/" + my_level + ".map"
        self.map_array = []
        with open(my_map_file) as current_map:
            for row in current_map:
                row_list = list(row)
                self.map_array.append(row_list)
        return self.map_array
