#Write a function count_frequency that takes a list of words as an argument, counts how many times each word appears in the list, and then returns this frequency listing as a Python dictionary
from collections import Counter
list=['apple','egg','apple','banana','egg','apple']
count = Counter(list)
print(count)
#%%
#leetcode two sum
def two_sum(nums: list, target: int):
    for i, n in enumerate(nums):
        match = target - n
        if match in (rest := nums[i + 1:]):
            match_at = rest.index(match)
            return i, match_at + i + 1


if __name__ == '__main__':
    if result := two_sum([4, 10, 11, 15], 25):
        print(f'Indices:\n{result}')
    else:
        print('No matches found')
