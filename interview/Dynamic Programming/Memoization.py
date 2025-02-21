def climbStairs(n: int) -> int:
    memo = {}
    
    def climb_helper(i: int) -> int:
        if i <= 1:
            return 1
        
        # check if value is already in cache
        # before making recursive calls
        # corresponds to the green nodes in the diagram
        if i in memo:
            return memo[i]
        
        # store result in cache before returning
        memo[i] = climb_helper(i - 1) + climb_helper(i - 2)
        return memo[i]
    
    return climb_helper(n)