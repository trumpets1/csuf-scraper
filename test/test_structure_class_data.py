import unittest
import structure_class_data


# 494128 -- math 534
math_534 = 'data/494128.html'
# 494129 -- math 535
math_535 = 'data/494120.html'
# 494141 -- math 599 research
math_599 = 'data/494141.html'
# 493151 -- econ 440
econ_440 = 'data/493151.html'



class TestHello(unittest.TestCase):
    def test_hello(self):
        """
        Test that it can say hello
        """
        result = structure_class_data.hello(3)
        self.assertEqual(result, 5)

class TestGettingComponentsFromTile(unittest.TestCase):
    def test_department(self):
        """
        department
        """
        title_components = structure_class_data.get_title_data(math_534)
        self.assertEqual(title_components['department'], 'MATH')
    def test_class_number(self):
        """
        class number
        """
        title_components = structure_class_data.get_title_data(math_534)
        self.assertEqual(title_components['class_number'], '534')

    def test_class_name(self):
        """
        class name
        """
        title_components = structure_class_data.get_title_data(math_534)
        self.assertEqual(title_components['class_name'], 'Statistical Computing')
    def test_unit_count(self):
        """
        department
        """
        title_components = structure_class_data.get_title_data(math_534)
        self.assertEqual(title_components['units'], [3])
if __name__ == '__main__':
    unittest.main()