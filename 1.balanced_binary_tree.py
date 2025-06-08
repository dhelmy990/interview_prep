
"""
    Today I learnt that float('inf') - float('inf' evaluates to NaN. 
    Intuitibely speaking, inf - inf  = 0 
    But
    I have now also learnt that NaN in any comparision evaluates to False. 
    Thank you Python, very cool.

    Initally, my code's conditional was swapped around. Now it looks like this to get around NaN shortcircuiting the eval to evaluate negatively where it should evaluate negatively 
    (I want NaN > 1 to go through. But NaN >/< anything becomes False so instead I parked it downstairs and inverted the boolean)

    Anyway, the inspiration here behind this solution is that i know that if a binary tree downstairs is unbalanced, then i shouldn't care about trees upstaris.
    So if i find diff > 1 anywhere, i shortcircuit any future evaluations by trying to provide float('inf')
    In abs(anything - float('inf')) that evaluates immediately to a value > 1.
"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode], first = True) -> bool:
        if root is None:
            return True if first else 0

        l, r = self.isBalanced(root.left, False), self.isBalanced(root.right, False)

        diff = abs(l - r)
        if diff <= 1:
            _ = max(l, r)
            if not first:
                return _ + 1
            else:
                return True
        else:
            return False if first else float('inf')