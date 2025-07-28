class Solution:
    def Pattern19(self, n):

        for i in range(n):
            # this loop decides the number of lines
            # print the stars
            for j in range(n - i):
                print("*", end="")

            # print the spaces
            for spaces in range(2 * i):
                print(" ", end="")

            # print the remaining stars

            for stars in range(n - i):
                print("*", end="")
            print()
        for i in range(n):
            for j in range(0, i + 1):
                print("*", end="")
            for spaces in range(2 * n - 2 * (i + 1)):
                ''' since i = 0  here but we need 8 spaces between the two stars after the first part is over
                hence we will use 2 * (i + 1) 
                so i = 0 -> spaces = 2 * n - 2 * i - 2 = 10 - 0 - 2 = 8 just what we needed
                   i = 1 -> spaces = 2 * n - 2 * i - 2 = 10 - 2 - 2 = 6
                '''
                print(" ", end="")
            for stars in range(0, i + 1):
                print("*", end="")
            print()


if __name__ == "__main__":
    solution = Solution()
    solution.Pattern19(5)
