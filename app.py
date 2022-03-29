from transform_string.classes import MagicString, CSVSaver

if __name__ == "__main__":
    string = input("Enter your string to be transformed: ")
    
    # if not string.isalpha():
    #    raise ValueError("Only alphabetical input is accepted.")

    upper_case = MagicString.uppercase(string)

    print(upper_case)

    alternate_case = MagicString.alternatecase(string)

    print(alternate_case)

    CSVSaver.generate(string)