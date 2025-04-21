def find_min(nums: list=None) -> int:
    minimum = nums[0]
    for i in range(0, len(nums)):
        minimum = nums[i] if nums[i] < minimum else minimum
    return minimum

def find_max(nums: list=None) -> int:
    maximum = nums[0]
    for i in range(0, len(nums)):
        maximum = nums[i] if nums[i] > maximum else maximum
    return maximum



def longest_consecutive(nums: list = None) -> int:
    num_set = set(nums)  # Convert list to set for O(1) lookups
    print (num_set)
    longest = 0

    for num in num_set:
        print (num)
        if num - 1 not in num_set:  # Start of a new sequence
            #print ("{} not in num_set".format(str(num - 1)))
            length = 1              # length is reset
            while num + length in num_set:
                #print ("Check for " + str(num+length))
                length += 1
            longest = max(longest, length)
            print ("For num = {}, longest = {}".format(num, longest))

    return longest

if __name__ == "__main__":
    numbers = [100, 4, 200, 1, 3, 2,  4, 5, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    print (longest_consecutive(numbers))
