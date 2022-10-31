#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Oct 2022
# This program accepts packages for a company
# and decides if the package is acceptable or not.
# This program uses if and else statements.

import math


def main():

    # input
    package_weight = int(input("Enter weight of package (kg): "))
    package_length = int(input("Enter package length (cm): "))
    package_width = int(input("Enter package width (cm): "))
    package_height = int(input("Enter package height (cm): "))

    # process and output
    if (package_weight > 27) or (package_weight < 27):
        print(
            "\n{0:,}kg is an approved weight, the company accepts package.".format(
                package_weight
            )
        )
    else:
        print(
            "\n{0:,}kg is unapproved weight, the company rejects package.".format(
                package_weight
            )
        )
    volume = package_length * package_width * package_height
    if volume <= 10000:
        print(
            "\n{0:,} cubic cm is approved, the company accepts package.".format(volume)
        )
    else:
        print(
            "\n{0:,} cubic cm is unapproved, the company rejects package.".format(
                volume
            )
        )
    if package_weight == 27 or volume > 10000:
        print(
            "\nSorry the company cannot accepted the package because its either equal to 27kg or larger than 10,000 cubic cm."
        )

    print("\n\nDone.")


if __name__ == "__main__":
    main()
