def count_chars(input_file):
    count = {}
    with open(input_file) as info:
        read_file = info.read()
        for character in read_file.upper():
            count[character] = count.get(character, 0) + 1
    return count


input_file = input("file path:")
print(count_chars(input_file))


def count_chars(input_file):
    count = {}
    with open(input_file) as info:
        content_of_line = info.readline()
        while content_of_line:
            list = content_of_line.split()
            for item in list:
                if item.endswith("," or "."):
                    item = item[:-1]
            for char in list:
                count[char] = count.get(char, 0) + 1
            content_of_line = info.readline()
        return count


input_file = input("file path : ")
if not input_file:
    input_file = r'C:\Users\Administrator\Desktop\bbc.txt'
print(count_chars(input_file))