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


group_activity()
