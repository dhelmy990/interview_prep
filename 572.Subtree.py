
class Solution:
    def transcribes(self, root) -> list:
        """
            Return string version of trees to leverage sliding window
        """

        ans = []
        working = [root]
        while working:
            focus = working.pop(-1)
            if focus is not None:
                working.append(focus.right)
                working.append(focus.left)
                ans.append(focus.val)
            else:
                ans.append(None)
        return ans



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #my idea is i memorise the length of subroot once
        #after that, i should only need only to iterate through root tree once
        #my job would also
        
        #im thinking that if you would like to reduce the number of
        #computations, you should kind of use a "sliding window" approach
        #hm...yeah that would actually work. neat.
        root = self.transcribes(root)
        subRoot = self.transcribes(subRoot)

        point_root = len(subRoot) - 1
        point_sub_root = point_root


        while(point_root < len(root)):
            print(subRoot[point_sub_root])
            print(root[point_root])

            if point_sub_root < 0:
                return True
            elif subRoot[point_sub_root] == root[point_root]:
                point_sub_root -= 1
                point_root -= 1
            else:
                point_root += (len(subRoot) - point_sub_root)
                point_sub_root = len(subRoot) - 1
                print("here")

        return False