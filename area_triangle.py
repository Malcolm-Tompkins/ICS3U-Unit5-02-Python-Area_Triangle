#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 26, 2021
# Calculates the area of a triangle with functions


def area_of_triangle(user_base, user_height):
    area = user_base * user_height / 2
    print("The area of your triangle is: {:.0f}mm²".format(area))


def main():
    user_input1 = (input("Enter the base of your triangle (mm): "))
    user_input2 = (input("Enter the height of your triangle (mm): "))
    try:
        user_base = int(user_input1)
        try:
            user_height = int(user_input2)
            area_of_triangle(user_base, user_height)

        except Exception:
            print("{} is not a positive integer".format(user_input2))
    except Exception:
        print("{} is not a positive integer".format(user_input1))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
