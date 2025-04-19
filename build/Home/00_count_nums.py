def count_numbers(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict

def main():
    nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    result = count_numbers(nums)
    print("Frequency of numbers:", result)

if __name__ == "__main__":
    main()
