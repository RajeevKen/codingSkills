'''
Write a Python program to find the longest consecutive sequence in an unsorted list
Input = [100, 4, 200, 1, 50, 3, 32, 2]
Output = 4, [1, 2, 3, 4]
'''
 

def longest_consecutive_sequence(nums):
    '''
    By set method
    '''
    if not nums:
        return 0, []

    # Convert the list to a set to allow for O(1) lookups
    num_set = set(nums)
    longest_seq = 0
    longest_start = None

    for num in num_set:
        # If 'num - 1' is not in the set, then it is the start of a new sequence
        if num - 1 not in num_set:
            current_num = num
            current_seq = []

            # Find the longest consecutive sequence starting from 'num'
            while current_num in num_set:
                current_seq.append(current_num)
                current_num += 1

            # Update the longest sequence if this one is longer
            if len(current_seq) > longest_seq:
                longest_seq = len(current_seq)
                longest_start = current_seq[0]

    # Return the length of the longest sequence and the sequence itself
    return longest_seq, list(range(longest_start, longest_start + longest_seq))

# Test the function
input_list = [100, 4, 200, 1, 50, 3, 32, 2]
length, sequence = longest_consecutive_sequence(input_list)
print(length, sequence)


def longest_consecutive_sequence(nums):

    '''
    without set class
    '''
    if not nums:
        return 0, []

    # Step 1: Sort the list
    nums.sort()

    longest_seq = 1
    longest_start = nums[0]
    current_seq = 1
    current_start = nums[0]

    # Step 2: Find the longest consecutive sequence
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:  # Consecutive numbers
            current_seq += 1
        elif nums[i] != nums[i - 1]:  # Not a duplicate number
            if current_seq > longest_seq:
                longest_seq = current_seq
                longest_start = current_start
            # Start a new sequence
            current_start = nums[i]
            current_seq = 1

    # Final check after the loop
    if current_seq > longest_seq:
        longest_seq = current_seq
        longest_start = current_start

    # Step 3: Return the longest sequence and its length
    return longest_seq, list(range(longest_start, longest_start + longest_seq))

# Test the function
input_list = [100, 4, 200, 1, 50, 3, 32, 2]
length, sequence = longest_consecutive_sequence(input_list)
print(length, sequence)