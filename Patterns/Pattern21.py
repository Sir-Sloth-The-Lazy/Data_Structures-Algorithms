class Solution:
    def pattern_start_end(self, n):
        print("*" * n, end="")

    def pattern_mid(self, n):
        for j in range(n):
            if j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")

    def pattern21(self, n):
        for i in range(n):
            if i == 0 or i == n - 1:
                self.pattern_start_end(n)
            else:
                self.pattern_mid(n)
            print()

# Main function
if __name__ == "__main__":
    N = 5
    sol = Solution()
    sol.pattern21(N)