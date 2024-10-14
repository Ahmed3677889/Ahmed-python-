def print_even_numbers():
    print("الأعداد الزوجية من ١ إلى ١١ هي:")
    for num in range(1, 12):
        if num % 2 != 0:
            print(num)

# Call the function
print_even_numbers()
