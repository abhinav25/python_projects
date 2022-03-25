import re
with open('/.../test_file.txt') as f:
    lines = f.readlines()
    print(lines)
    f1 = open('/.../new_file.txt', 'w')
    for line in lines:
        new_string = re.sub('[^A-Za-z0-9]+', '', line)
        print(new_string)
        f1.write(new_string+'\n')
    f1.close()
