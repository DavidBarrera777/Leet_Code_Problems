#657. Robot Return to Origin
#Easy 

#There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its
#moves, judge if this robot ends up at (0, 0) after it completes its moves.
#You are given a string moves that represents the move sequence of the robot where moves[i]
#represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
#Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.
#Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the 
#right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's 
#movement is the same for each move.


#This just checks whether the movments are the same and if they are then they would cancel each other
#out resulting in the robot being at (0,0) thus True would be returned
#Otherwise False would be returned because the robot would have moved positions
def judge_circle(moves):
    if moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D'):
        return True 
    else:
        return False



#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    moves = 'UD'
    print(judge_circle(moves))

    moves2 = 'LL'
    print(judge_circle(moves2))

    moves3 = 'RLUURDDDLU'
    print(judge_circle(moves3))
    return 





if __name__ == '__main__':
    main()