def func_read(path):
    f = open(path)
    content = f.readlines()
    result = {}

    last_title = None
    for line_content in content:
        if line_content.strip() == "":
            continue
        if line_content.startswith("["):
            last_title = line_content[1:-2]
            result[last_title] = {}
        else:
            first_equal = line_content.find("=")
            key = line_content[:first_equal]
            value = line_content[first_equal + 1:-1]
            result[last_title][key] = value
    return result
print(func_read(r'C:\Users\Administrator\Desktop\install.ini'))


def simulate(path):
    configuration = func_read(path)
    configuration['Setup']['RebootMode'] = "1\n"
    string = []
    for title in configuration.keys():
        string.append('\n[%s]' % title)
        current_section = configuration[title]

        for key in current_section.keys():
            value = current_section[key]
            string.append('%s=%s' % (key, value))
    f = open(path, 'w')
    f.write('\n'.join(string))
    f.close()


simulate(r'C:\Users\Administrator\Desktop\install.ini')


