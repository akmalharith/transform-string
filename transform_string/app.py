csv_file = "output.csv"


class MagicString():
    def __init__(self, string) -> None:
        self.string = string
        self.uppercase = self._uppercase()
        self.alternatecase = self._alternatecase()

    def _uppercase(self):
        return self.string.upper()

    def _alternatecase(self):
        string_temp = [char.upper() if not index % 2 else char.lower()
                       for index, char in enumerate(self.string)]
        return "".join(string_temp)


class CSVSaver():

    @staticmethod
    def generate(string):
        string_temp = list(string)
        string = ",".join(string_temp)
        with open(csv_file, "w") as output_file:
            output_file.write(string)
