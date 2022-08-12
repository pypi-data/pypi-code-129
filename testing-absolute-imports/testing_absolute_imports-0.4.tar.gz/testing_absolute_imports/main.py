#!/usr/bin/python

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import testing_absolute_imports.printing
# import testing_absolute_imports.secondprint


def main():
    module_name = testing_absolute_imports.printing.Print()
    module_name.print_name()

    # module_2 = secondprint.PrintNew()
    # module_2.second_print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

