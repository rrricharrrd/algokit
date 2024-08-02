from data_structures import LinkedList


def test_list():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.delete(2)
    print(lst)
