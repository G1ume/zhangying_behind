class OneClassCsv:
    COL_NUM = 8
    class Lessons:
        def __init__(self):
            self.teacher=None
            self.week=None
    def __init__(self, input_path, output_path):
        self.csv_input = None
        self.csv_output = None
        self.in_path = input_path
        self.out_path = output_path
        self._read_file()
        self._deal_csv()

    def _read_file(self):
        import os
        if os.path.exists(self.in_path):
            f = open(self.in_path, encoding='gbk')
            tmp = f.read().split(',')
            self.csv_input = []
            for line in tmp:
                if line.startswith("\"") or line.find("\n") == -1:
                    self.csv_input.append(line.replace("，", ","))
                else:
                    for tmp2 in line.split("\n"):
                        self.csv_input.append(tmp2.replace("，", ","))
            # 格式重整
            # for
            print(self.csv_input)
        else:
            print("Error:file dose not exist!")

    def _deal_csv(self):
        pass

    def _output(self, type):
        if type == 1:
            pass
        elif type == 2:
            pass


if __name__ == '__main__':
    instance = OneClassCsv("C:/Users/Glume/Downloads/in.csv", None)
