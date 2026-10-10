class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def solution(self):
        head = None
        
        # 1. Create Linked List
        def create_list(arr):
            nonlocal head
            if not arr:
                return None
            head = ListNode(arr[0])
            curr = head
            for val in arr[1:]:
                curr.next = ListNode(val)
                curr = curr.next

        # 2. Traverse and print the node values
        def traverse():
            curr = head
            res = []
            while curr:
                res.append(str(curr.val))
                curr = curr.next
            print(" -> ".join(res))

        # 3. Insert node at a specific position (0-indexed)
        def insert_at(pos, val):
            nonlocal head
            new_node = ListNode(val)
            if pos == 0:
                new_node.next = head
                head = new_node
                return
            curr = head
            for _ in range(pos - 1):
                if not curr:
                    return
                curr = curr.next
            if curr:
                new_node.next = curr.next
                curr.next = new_node

        # 4. Find Middle node and print its value
        def find_middle():
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            if slow:
                print(slow.val)

        # 5. Delete node by value
        def delete_node(val):
            nonlocal head
            if head and head.val == val:
                head = head.next
                return
            curr = head
            prev = None
            while curr and curr.val != val:
                prev = curr
                curr = curr.next
            if curr:
                prev.next = curr.next

        # 6. Reverse list
        def reverse():
            nonlocal head
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            head = prev

        # 7. Calculate the sum of every two consecutive node values
        def sum_consecutive():
            curr = head
            sums = []
            while curr and curr.next:
                sums.append(curr.val + curr.next.val)
                curr = curr.next
            print(sums)