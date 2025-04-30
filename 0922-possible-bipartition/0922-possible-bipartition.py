class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        BLUE, GREEN = 1, -1
        
        def draw( person_id, color ):
            color_of[person_id] = color
            
            for the_other in dislike_table[ person_id ]:
                if color_of[the_other] == color:
                    return False

                if (not color_of[the_other]) and (not draw( the_other, -color)):
                    return False
                    
            return True
        
        if N == 1 or not dislikes:
            return True
        
        dislike_table = defaultdict(list)
        color_of = defaultdict(int)
        
        for p1, p2 in dislikes:
            dislike_table[p1].append( p2 )
            dislike_table[p2].append( p1 )
            
        for person_id in range(1, N+1):
            
            if (not color_of[person_id])  and (not draw( person_id, BLUE)):
                return False 
        
        return True