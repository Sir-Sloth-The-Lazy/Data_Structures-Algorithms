class Solution:
    def pattern20(self, n):

        initial_spaces = 2 * n - 2
        for i in range(1, n + 1):
            print("*" * i, end="")

            # print the spaces
            print(" " * initial_spaces, end="")

            # print the stars again
            print("*" * i, end="")

            print()

            initial_spaces -= 2

        initial_spaces = 2
        for i in range(1, n):
            print("*" * (n - i), end="")

            # print the spaces
            print(" " * initial_spaces, end="")

            # print the stars
            print("*" * (n - i), end="")

            initial_spaces += 2
            print()

