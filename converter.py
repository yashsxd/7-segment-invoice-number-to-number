from metadata import data

# for storing set of numbers
num_set = []

def print_output(num_set):
    with open('output.txt','a') as f:
        f.write(num_set)
        f.write('\n')

def word_reader(char):
    if char is '\n':
        print_output(''.join(num_set))
        # print(''.join(num_set))
        num_set.clear()
    else:
        number = [key for (key, value) in data.items() if value == char]
        if number:
            num_set.append(str(number[0]))

def extract_numbers(input_lines):
    length = len(input_lines)

    for w in range(0, length - 3, 4):
        length_line = len(input_lines[w])
        for x in range(0, length_line - 2, 3):
            char = []
            for y in range(3):
                for z in range(3):
                    if input_lines[w + y][x + z] is not '\n':
                        char.append(input_lines[w + y][x + z])
                    else:
                        char.append(' ')
            word_reader(char)
        word_reader('\n')


def open_file():
    open('output.txt', 'w').close()
    with open('input.txt','r') as f:
        input_lines = f.readlines()
    return input_lines


input_lines = open_file()
extract_numbers(input_lines)