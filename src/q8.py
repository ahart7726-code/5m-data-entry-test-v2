"""
Question 8 — Python: Find and Fix the Bug  [Short Answer — Write Code]

The function below is SUPPOSED to count how many even numbers are in a list.
It runs without crashing, but it returns the wrong answer.

    def count_evens(numbers):
        count = 0
        for n in numbers:
            if n % 2 == 1:      # <-- something here is wrong
                count = count + 1
        return count

    # Expected: 4  (the evens are 2, 4, 6, 8)
    print(count_evens([1, 2, 3, 4, 5, 6, 8]))

------------------------------------------------------------------
Task
------------------------------------------------------------------

(a) What does the buggy version actually return for [1, 2, 3, 4, 5, 6, 8], and why?

    Answer: It will return 3 and count odd number in the list, because the formula is like n mod 2 = 1 which formula to get odd number

(b) Fix the bug. Write the corrected function below.
    (A one-character change is enough, but you must understand why.)
"""

def count_evens(numbers):
    count = 0
        for n in numbers:
            if n % 2 == 0:      # <-- something here is wrong
                count = count + 1
        return count
    


"""
(c) In one sentence, explain in plain English what `n % 2 == 0` checks.

    Answer: this formula will check whether the reminder of n divided by 2 is 0, if yes then it is even number, if reminder is 1 then it is odd number
"""
