import os

class Cal():
    def add_num(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        return  result

    def save(self, dir_path, file_name):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, "w") as f:
            f.write("test")
