class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        x , y , z = target

        got_x = False
        got_y = False
        got_z = False

        for a,b,c in triplets:
            if a > x or b > y or c > z:
                continue
            
            if x == a:
                got_x = True
            if y == b:
                got_y = True
            if z == c:
                got_z = True
        
        return got_x and got_y and got_z