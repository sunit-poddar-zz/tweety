def can_create(list_of_strings, input_string):
    """
    Divide the word into two parts:
        - the prefix will have a length of 'counter' and check if it is present in 'list_of_strings':
            - if yes, check for suffix of length "input_string_len - counter" recursively. Return True if both prefix &
            suffix are present the 'input_string'.

    :param list_of_strings:
    :param input_string:
    :return:
    """

    input_string_len = len(input_string)

    if input_string_len == 0:
        return True

    for counter in range(1, input_string_len + 1):
        sub_string = input_string[:counter]

        if sub_string not in list_of_strings:
            continue

        if can_create(list_of_strings, input_string[counter:]):
            return True

    return False


def initiate():
    list_of_strings = input("Enter substrings separated by blank space: ").split(' ')
    input_string = input("Enter parent string: ")

    print(can_create(list_of_strings, input_string))


def test():
    print('\n\nTEST CASES')
    if can_create(["back", "end", "front", "tree"], 'backend') == True:
        print('pass')
    else:
        print('fail')

    if can_create(["back", "end", "front", "tree"], 'endfront') == True:
        print('pass')
    else:
        print('fail')

    if can_create(["back", "end", "front", "tree"], 'frontyard') == False:
        print('pass')
    else:
        print('fail')

    if can_create(["back", "end", "front", "tree"], 'backfront') == True:
        print('pass')
    else:
        print('fail')

    if can_create(["back", "end", "front", "tree"], 'notree') == False:
        print('pass')
    else:
        print('fail')


initiate()
test()
