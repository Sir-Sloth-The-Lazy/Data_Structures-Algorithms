
# Pattern 21

## Problem Statement

You are asked to generate a rectangular pattern with asterisks (`*`) on the borders and spaces in the middle. The size of the pattern is determined by the input `n`, which defines the number of rows and columns. The pattern will have `*` in the first and last rows, and `*` in the first and last columns of the middle rows.

### Example Output for `n = 5`:

For `n = 5`, the output will be:

```

*****
*   *
*   *
*   *
*****

````

### Explanation:
- The first and last rows (`i == 0` or `i == n-1`) contain only `*`.
- The middle rows (`1 <= i <= n-2`) contain `*` at the start and end positions, with spaces in between.

## Approach

1. **`pattern_start_end(self, n)`**:
   - Prints a row of `*` characters of length `n`. This is used for the first and last rows of the pattern.

2. **`pattern_mid(self, n)`**:
   - Prints `*` at the first and last positions, and spaces in between for the middle rows of the pattern.

3. **`pattern21(self, n)`**:
   - Iterates through the rows of the pattern:
     - For the first and last rows, it calls `pattern_start_end(n)` to print the full row of `*`.
     - For the middle rows, it calls `pattern_mid(n)` to print `*` on the edges and spaces in the middle.

## Code Implementation

```python
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
````

## Input

* **n**: A positive integer that defines the number of rows and columns in the pattern.

## Output

* A rectangular pattern with dimensions `n x n` where:

  * The first and last rows contain only `*`.
  * The first and last columns of the middle rows contain `*` with spaces in between.

## Time Complexity

* **Time Complexity**: `O(n^2)` because the pattern is generated using two nested loops: one for iterating over rows and another for iterating over columns.

* **Space Complexity**: `O(1)` because the pattern is directly printed and no additional space is used apart from the console output.

## Example Usage

```bash
python pattern_generator.py
```

For `n = 5`, the output will be:

```
*****
*   *
*   *
*   *
*****
```

---

**Note**: This solution assumes that the value of `n` is always a positive integer.

