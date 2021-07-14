import re

if __name__ == '__main__':
    pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
    string = "021-434378473847837483"
    result = re.search(pattern, string)
    print(result)



