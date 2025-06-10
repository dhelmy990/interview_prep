# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
    For this problem, i am lucky enough to know about the linked list reversal algo
    I wrap the smaller algo into the larger one

    Refer to drawing. I intentionally created a sub linked list of the form good
    for the algo, and return the first and last node

    I get the head [A NODE NOT PART OF THE SEQUENCE I ATTEMPT TO REVERSE] to point to
    first node
    and get the last node to point to [FIRST NODE OF NEXT SEQUENCE]

    Based on the given role to ensure the completeness of the algo, the last node
    of this sequence is set to the "head" role

    To allow the correctness of the algo (always have an outside watcher) I need
    to instantiate a dummy node. To finish the algo off I can return this dummy
    node's next as the final value

    I guess I'll re-attempt this some other time, but otherwise i feel pretty satisfied for now
    
"""

class Solution:

    """
        def print(self, head):
            want = []
            while head:
                want.append(head.val)
                head = head.next
            print(want)
    """

    def reverse(self, head):
        self.print(head)

        prev, cur = None, head
        while cur:
            placeholder = cur.next
            cur.next = prev
            prev = cur
            cur = placeholder
        return prev, head




    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #the...fuck...wait why is this considered hard
        #find out if i have k nodes
        #if its the first time i do this...set head to the last of this
        #else, simply perform reversal

        #i know what im trying to do in my head...but i cant express this in code
        dummy = head
        dummy_node = ListNode(0, head)
        lp = dummy_node


        try:
            while(True):
                for i in range(k - 1):
                    dummy = dummy.next
                
                rp = dummy.next

                dummy.next = None
                new_start, new_end = self.reverse(lp.next)
                lp.next, new_end.next = new_start, rp
                lp = new_end
                dummy = rp
        except:
            return dummy_node.next