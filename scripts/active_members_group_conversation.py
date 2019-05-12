from urllib.request import urlopen
from collections import Counter


def get_name_from_line(line):
    """

    :param line: Message line from group conversation
    :return: Name of sender
    """

    if '<' not in line and '>' not in line:
        return None

    return line[line.find('<')+1:line.find('>')]


def group_activity():
    group_members = []

    data = urlopen('https://s3.ap-south-1.amazonaws.com/haptikinterview/chats.txt')
    for line in data:
        name = get_name_from_line(str(line))
        if not name:
            continue
        group_members.append(name)

    most_active_members = Counter(group_members).most_common(3)

    print("Most active members in the group in descending order:")
    [print("{0} - {1} messages".format(member[0], member[1])) for member in most_active_members]


def test_get_name_from_line():
    if get_name_from_line('<John>: Okay, sounds like everyone is on the same page here') == 'John':
        print('pass')
    else:
        print('fail')

    if get_name_from_line('<Ram>: Great, lets get started') == 'Ram':
        print('pass')
    else:
        print('fail')

    if get_name_from_line('<Adam>: yea, and the backend building for chatbots is super exicting') == 'Adam':
        print('pass')
    else:
        print('fail')

    if get_name_from_line('<Ryan>: Haptik is cool ðŸ˜„') == 'Ryan':
        print('pass')
    else:
        print('fail')

    if get_name_from_line('<Bush>: Great meeting <all>') == 'Bush':
        print('pass')
    else:
        print('fail')


def test():
    test_get_name_from_line()


group_activity()
test()
