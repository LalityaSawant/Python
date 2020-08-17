balls_arr = ['G', 'B', 'G', 'G', 'R', 'B', 'R', 'G']
# Output: [R, R, G, G, G, G, B, B]


def dutch_flag_sort(balls):
    i = l_ptr = 0
    r_ptr = len(balls)-1
    pivot = 'G'

    while i <= r_ptr:
        if balls[i] < pivot:
            balls[i], balls[r_ptr] = balls[r_ptr], balls[i]
            r_ptr -= 1
        elif balls[i] > pivot:
            balls[i], balls[l_ptr] = balls[l_ptr], balls[i]
            l_ptr += 1
            i += 1
        else:
            i += 1

    return balls


print(dutch_flag_sort(balls_arr))

"""
Dutch National Flag
Given some balls of three colors arranged in a line, rearrange them such that all the red balls go first, then green and then blue ones.
Do rearrange the balls in place. A solution that simply counts colors and overwrites the array is not the one we are looking for.
This is an important problem in search algorithms theory proposed by Dutch computer scientist Edsger Dijkstra. Dutch national flag has three colors (albeit different from ones used in this problem).
Example

Input: [G, B, G, G, R, B, R, G]

Output: [R, R, G, G, G, G, B, B]
There are a total of 2 red, 4 green and 2 blue balls. In this order they appear in the correct output.
Notes
Input Parameters: An array of characters named balls, consisting of letters from {‘R’, ‘G’, ‘B’}.
Output: Return type is void. Modify the input character array by rearranging the characters in-place.
Constraints:
1 <= n <= 100000
Do this in ONE pass over the array - NOT TWO passes, just one pass.
Solution is only allowed to use constant extra memory.

Custom Input

Input Format: The first line of input should contain an integer n, denoting the number of balls. In the next n lines, i-th line should contain one letter from {'R', 'G', 'B'}, balls[i], denoting the color of the i-th ball. If balls = [G, B, G, G, R, B, R, G], then input should be:
8
G
B
G
G
R
B
R
G

Output Format: There will be n lines of output. i-th line contains a character balls[i], denoting character at index i of balls. Here, balls is the character array after the function that you are going to complete is called. For input balls = [G, B, G, G, R, B, R, G], output will be:
R
R
G
G
G
G
B
B
"""