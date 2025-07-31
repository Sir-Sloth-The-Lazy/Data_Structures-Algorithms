class Solution:
    # Function to print pattern22
    def pattern22(self, n):
        # Outer loop for the rows
        for i in range(2 * n - 1):
            # Inner loop for the columns
            for j in range(2 * n - 1):
                """ Initialising the top, down, left
                and right indices of a cell"""
                top = i
                left = j
                right = (2 * n - 2) - j
                bottom = (2 * n - 2) - i

                """ Minimum of 4 directions and then we 
                subtract from n because previously we 
                would get a pattern whose border has 0's, 
                but we want with border n's and then
                decreasing inside."""
                print((n - min(min(top, bottom), min(left, right))), end=" ")

            # Move to the next row
            print()


# Main function
if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern22(N)