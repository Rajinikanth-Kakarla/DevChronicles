class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] >= rec2[2] or rec2[0] >= rec1[2]:
            return False
        # If one rectangle is above other
        if rec1[1] >= rec2[3] or rec2[1] >= rec1[3]:
            return False
        return True
    
    def isRectangleOverlap2(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or # left
                    rec1[3] <= rec2[1] or # bottom
                    rec1[0] >= rec2[2] or # right
                    rec1[1] >= rec2[3])