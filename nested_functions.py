# ALDWIN REYES
# ITELEC2
# Laboratory #18 – Guided Coding Exercise: Nested Functions and Reusing User-Defined Functions

def main():

    def square(num):
        """Returns the square of the given number."""
        return num * num 

    def sum_of_squares(numbers):
        """Returns the sum of the squares of the numbers in the list."""
        total = 0
        for n in numbers:
            total += square(n)  # Call the square function and add to total
        return total

    numbers_list = [2, 3, 4]
    result = sum_of_squares(numbers_list)

    print(f"The sum of squares is: {result}")

if __name__ == "__main__":
    main()
