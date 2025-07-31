
# Pattern 22

## Problem Statement

You are required to generate a pattern based on the given integer `n`. The pattern will be a square matrix of size `(2n - 1) x (2n - 1)` where the border consists of `n`, the next inner layer is `n-1`, and so on, decreasing until the center is reached. The center will always be `1`.

## Pattern Structure

- The outermost layer of the square matrix will have the value `n`.
- The next inner layer will have the value `n-1`, followed by `n-2`, and so on until the center.
- The center will always have the value `1`.

### Example Output

For `n = 5`, the output will look like:

```

5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5

````

### Explanation of the Pattern

1. The pattern is a `(2n - 1) x (2n - 1)` square grid.
2. The value at each cell is determined by the minimum of the distance from the top, bottom, left, and right edges, and this value is subtracted from `n`.
3. As you move inward from the edges, the value decreases by `1` in each layer.

## Approach

1. **Outer Loop**: Loop through rows (`i`) from `0` to `2n - 2`.
2. **Inner Loop**: Loop through columns (`j`) from `0` to `2n - 2`.
3. **Calculate the Layer**:
   - For each cell, calculate the distance from the top, bottom, left, and right edges.
   - The value at each cell is determined by `n - min(min(top, bottom), min(left, right))`.
4. **Print the Pattern**: Print each value without a newline, then print a newline after each row.

## Code

```python
class Solution:
    # Function to print pattern22
    def pattern22(self, n):
        # Outer loop for the rows
        for i in range(2 * n - 1):
            # Inner loop for the columns
            for j in range(2 * n - 1):
                # Initializing the top, down, left, and right indices of a cell
                top = i
                left = j
                right = (2 * n - 2) - j
                bottom = (2 * n - 2) - i
                
                # Print the minimum of the 4 directions, and subtract from n to create the pattern
                print((n - min(min(top, bottom), min(left, right))), end=" ")
                
            # Move to the next row
            print()

# Main function
if __name__ == "__main__":
    N = 5
    # Create an instance of Solution class
    sol = Solution()
    sol.pattern22(N)
````

## Input

* **n**: A positive integer that defines the size of the pattern. `n` determines the number of layers in the pattern.

## Output

* A square matrix with size `(2n - 1) x (2n - 1)` where the pattern follows the above-described rules.

## Time Complexity

* **Time Complexity**: `O(n^2)` because there are `2n-1` rows and `2n-1` columns, and the minimum operation for each cell is done in constant time.
* **Space Complexity**: `O(1)` because no additional space is used apart from the output.

## Example Usage

```bash
python Pattern22.py
```

For `n = 5`, the pattern will be generated as shown in the example above.

---

**Note**: This solution assumes the value of `n` is always a positive integer and works efficiently for moderate values of `n`.

