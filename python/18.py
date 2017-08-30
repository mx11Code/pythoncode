def func(path):
    f = open(path)
    content = f.read().split("\n")
    result = {}

    # todo: move content from ini file to result
    last_title = None
    for line_content in content:

        if line_content.strip() == '':
            continue

        if line_content.startswith("[") and line_content.endswith("]"):
            last_title = line_content[1:-1]
            result[last_title] = {}
        else:
            first_equal = line_content.find("=")
            key = line_content[:first_equal]
            value = line_content[first_equal + 1:]
            result[last_title][key] = value

    return result


print(func(r'C:\Users\Administrator\Desktop\install.ini'))
