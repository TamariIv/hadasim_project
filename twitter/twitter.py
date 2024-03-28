import math


def rectangle():
    """Calculate and print either the area or perimeter of a rectangle based on user input."""
    height = int(input("Enter the height of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))

    if height == width or abs(height - width) > 5:
        print("The area of the rectangle is:", height * width)
    else:
        print("The perimeter of the rectangle is:", 2 * (height + width))


def triangle():
    """Calculate and print either the perimeter or print a triangle based on user input."""
    height = int(input("Enter the height of the triangle: "))
    width = int(input("Enter the width of the triangle: "))

    print("\nChoose triangle operation:")
    print("1. Calculate triangle perimeter")
    print("2. Print triangle")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        perimeter = 2 * height + width
        print("The perimeter of the triangle is:", perimeter)
    elif choice == "2":
        print_triangle(height, width)
    else:
        print("Invalid option.")


def print_triangle(height, width):
    """
    Print a triangle pattern based on the given height and width.

    Args:
        height (int): Height of the triangle.
        width (int): Width of the triangle.
    """
    if width % 2 == 0 or width > height * 2:
        print("Cannot print the triangle.")
        return

    middle_lines = (height - 2)  # the number rof kines between to top and bottom lines
    odd_numbers_in_range = ((width - 1) // 2) - 1  # how many option for * we have
    in_each_group = (middle_lines // odd_numbers_in_range)  # the number of lines printed with each amount of *
    carry_lines = (middle_lines % odd_numbers_in_range)  # additional lines to be printed with the top group

    # print top line
    for i in range((width // 2)):
        print(" ", end="")
    print("*")

    # print middle lines
    amount = 3
    extra_lines_in_top = carry_lines != 0
    while amount < width:
        for times in range(in_each_group):
            for i in range(((width - amount) // 2)):
                print(" ", end="")
            for i in range(amount):
                print("*", end="")
            print("\n", end="")
        if extra_lines_in_top:
            for times in range(carry_lines):
                for i in range(((width - amount) // 2)):
                    print(" ", end="")
                for i in range(amount):
                    print("*", end="")
                print("\n", end="")
            extra_lines_in_top = False
        amount += 2

    # print bottom line
    for i in range(width):
        print("*", end="")


while True:
    print("\nMenu:")
    print("1. Choose rectangle")
    print("2. Choose triangle")
    print("3. Exit")

    option = input("Please choose an option (1, 2, or 3): ")

    if option == "1":
        rectangle()
    elif option == "2":
        triangle()
    elif option == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose again.")
