"""Robot Return to Origin"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for move in moves:
            if move == "U":
                y += 1
            elif move == "R":
                x += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
        return x == 0 and y == 0


if __name__ == "__main__":
    print(Solution().judgeCircle("URDL"))
    print(Solution().judgeCircle("URRDLL"))
    print(Solution().judgeCircle("URRDL"))
    print(Solution().judgeCircle("URDLL"))
