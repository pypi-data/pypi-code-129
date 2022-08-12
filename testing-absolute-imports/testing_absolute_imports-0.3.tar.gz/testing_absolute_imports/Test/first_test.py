import unittest

import testing_absolute_imports.printing
import testing_absolute_imports.main


class TestRepetitionTime(unittest.TestCase):

    def test_repetition_time_bold(self):
        name_variable = testing_absolute_imports.printing.Print()
        print(name_variable.print_name())

    def test_main(self):
        main = testing_absolute_imports.main.main()
