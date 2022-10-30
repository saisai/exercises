'''
https://leetcode.com/problems/robot-bounded-in-circle/

https://leetcode.com/problems/robot-bounded-in-circle/solutions/850464/python-3-simulation-explanation/

Explanation
    direc is the direction, pos is current position [x, y]
    Simulate the process and find out where the point is at for every instruction
    If pos return to origin [0, 0] or direction not facing initial state (0), then there is a loop
Implementation

'''
class S:
    def isRobotBounded(self, instructions: str) -> bool:
        direc, pos = 0, [0,0]
        for c in instructions:
            if c == "L": direc = (direc + 1) % 4
            elif c == "R": direc = (direc - 1) % 4
            elif c == "G":
                if direc == 0: pos[1] += 1
                elif direc == 1: pos[0] -= 1
                elif direc == 2: pos[1] -= 1
                else: pos[0] += 1
        return pos == [0, 0] or direc != 0

instructions = "GGLLGG"
print(S().isRobotBounded(instructions))

