class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num]+=1
            else:
                freq_map[num] = 1
        
        freq_list = list(freq_map.items())
        freq_list.sort(key=lambda x:x[1] , reverse=True)
        result = []
        for i in range(k):
            result.append(freq_list[i][0])      
        return result  