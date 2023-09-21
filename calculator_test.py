from calc.calcilator import calculator
from unittest import TestCase, main


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'),4)
    def test_minus(self):
        self.assertEqual(calculator('3-1'),2)

    def test_multi(self):
        self.assertEqual(calculator('4*4'),16)
    def test_divide(self):
        self.assertEqual(calculator('10/5'),2)
    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('dhbhbdh')
        self.assertAlmostEqual('Expression should have one sign from (+-/*)', e.exception.args[0])

    def test_two_sign(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertAlmostEqual('Expression should contains two integer number and one sign', e.exception.args[0])

    def test_many_sign(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2*7')
        self.assertAlmostEqual('Expression should contains two integer number and one sign', e.exception.args[0])
    def test_not_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2.9')
        self.assertAlmostEqual('Expression should contains two integer number and one sign', e.exception.args[0])
    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertAlmostEqual('Expression should contains two integer number and one sign', e.exception.args[0])

    
    
    

if __name__=='__main__':
    main()