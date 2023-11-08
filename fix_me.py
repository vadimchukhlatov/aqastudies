def calculate_average(num):
    total = sum(num)
    count = len(num)
    print(total, count)
    return total / count


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
