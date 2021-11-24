# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node

# ggggg


class Solution:
    @staticmethod
    def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
        """
        Merge two sorted linked list
        :param l1: first sorted linked list
        :param l2: second sorted linked list
        :return:
        """
        test_list = []
        merged_node = ListNode()
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                merged_node = add(merged_node, l1.val)
                test_list.append(l1.val)
                l1 = l1.next_node
            else:
                merged_node = add(merged_node, l2.val)
                test_list.append(l2.val)
                l2 = l2.next_node

        while l1 is not None:
            merged_node = add(merged_node, l1.val)
            test_list.append(l1.val)
            l1 = l1.next_node

        while l2 is not None:
            merged_node = add(merged_node, l2.val)
            test_list.append(l2.val)
            l2 = l2.next_node
        print(test_list)
        print(size(merged_node))
        return merged_node


def add(n: ListNode, data: int) -> ListNode:
    new_node = ListNode(val=data)
    if n.val is None:
        return new_node
    new_node.next_node = n
    return new_node


def size(n: ListNode) -> int:
    i = 0
    while n is not None:
        n = n.next_node
        i += 1
    return i


def values(n: ListNode) -> list[int]:
    li = []
    while n is not None:
        li.append(n.val)
        n = n.next_node
        if n is None:
            break
    return li


def test_linked_list():
    linked_list = ListNode(val=4)
    for x in [3, 2, 1]:
        linked_list = add(linked_list, x)

    # print(size(linked_list))
    s = Solution()
    n = s.merge_two_lists(linked_list, linked_list)
    print(values(linked_list))
    print(values(n))


test_linked_list()
