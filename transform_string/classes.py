csv_file = "output.csv"

class MagicString:
    @staticmethod
    def uppercase(string):
        return string.upper()

    @staticmethod
    def alternatecase(string):
        string_temp = [char.upper() if not index % 2 else char.lower()
                       for index, char in enumerate(string)]
        return "".join(string_temp)


class CSVSaver:
    @staticmethod
    def generate(string):
        string_temp = list(string)
        string = ",".join(string_temp)
        with open(csv_file, "w") as output_file:
            output_file.write(string)

        print("CSV created!")
