import unittest
from logicky_bits.Expression import *


E2a_3 = Expression(Term(2, Variable("a", 3)))
Eneg_2a_3 = Expression(Term(-2, Variable("a", 3)))
E2a_neg_3 = Expression(Term(2, Variable("a", -3)))
E4a_3 = Expression(Term(4, Variable("a", 3)))

T4y_8 = Term(4, Variable("y", 8))
T2a_3 = Term(2, Variable("a", 3))
Tneg_2a_3 = Term(-2, Variable("a", 3))

E1_minus_4a_3 = Expression(Term(1), Term(-4, Variable("a", 3)))
E1_minus_2a_3 = Expression(Term(1), Term(-2, Variable("a", 3)))
E2a_3_plus_2a_neg_3 = Expression(Term(2, Variable("a", 3)), Term(2, Variable("a", -3)))
E2a_3_plus_1 = Expression(Term(2, Variable("a", 3)), Term(1))
E2a_3_minus_1 = Expression(Term(2, Variable("a", 3)), Term(-1))
E2a_neg_3_plus_4y_8 = Expression(Term(2, Variable("a", -3)), Term(4, Variable("y", 8)))
E4a_3_minus_1 = Expression(Term(4, Variable("a", 3)), Term(-1))
E4a_3_plus_1 = Expression(Term(4, Variable("a", 3)), Term(1))
Ex_plus_y = Expression(Term(1, Variable("x")), Term(1, Variable("y")))
Ex_minus_y = Expression(Term(1, Variable("x")), Term(-1, Variable("y")))
Ex_2_minus_y_2 = Expression(Term(1, Variable("x", 2)), Term(-1, Variable("y", 2)))
Ex_2_plus_2xy_plus_y_2 = Expression(
    Term(1, Variable("x", 2)),
    Term(2, Variable("x"), Variable("y")),
    Term(1, Variable("y", 2)),
)
E4y_8_minus_8a_3_y_8 = Expression(
    Term(4, Variable("y", 8)), Term(-8, Variable("a", 3), Variable("y", 8))
)


class Test_Expressions(unittest.TestCase):
    def test_add(self):
        # Expression + int
        self.assertEqual(E2a_3 + 0, E2a_3)
        self.assertEqual(E2a_3 + 1, E2a_3_plus_1)

        # Expression + Term
        self.assertEqual(E2a_neg_3 + T4y_8, E2a_neg_3_plus_4y_8)
        self.assertEqual(E2a_3 + T2a_3, E4a_3)

        # Expression + Expression
        self.assertEqual(E2a_3 + E2a_3, E4a_3)
        self.assertEqual(E2a_3 + E2a_neg_3, E2a_3_plus_2a_neg_3)
        self.assertEqual(E2a_neg_3 + E2a_3, E2a_3_plus_2a_neg_3)

    def test_sub(self):
        # Expression - int / int - Expression
        self.assertEqual(E2a_3 - 0, E2a_3)
        self.assertEqual(0 - E2a_3, Eneg_2a_3)
        self.assertEqual(E2a_3 - 1, E2a_3_minus_1)
        self.assertEqual(1 - E2a_3, E1_minus_2a_3)

        # Expression - Expression
        self.assertEqual(E2a_3 - E2a_3, 0)
        self.assertEqual(E2a_3 - E1_minus_2a_3, E4a_3_minus_1)
        self.assertEqual(E1_minus_2a_3 - E2a_3, E1_minus_4a_3)

        # Expression - Term
        self.assertEqual(E4a_3_minus_1 - T2a_3, E2a_3_minus_1)
        self.assertEqual(T2a_3 - E4a_3_minus_1, E1_minus_2a_3)
        self.assertEqual(E2a_3 - T2a_3, 0)
        self.assertEqual(T2a_3 - E2a_3, 0)

    def test_mul(self):
        # Expression * int
        self.assertEqual(E1_minus_2a_3 * 0, 0)
        self.assertEqual(E1_minus_2a_3 * 1, E1_minus_2a_3)

        # Expression * Term
        self.assertEqual(E1_minus_2a_3 * T4y_8, E4y_8_minus_8a_3_y_8)

        # Expression * Expresssion
        self.assertEqual(Ex_plus_y * Ex_plus_y, Ex_2_plus_2xy_plus_y_2)
        self.assertEqual(Ex_minus_y * Ex_plus_y, Ex_2_minus_y_2)

    def test_pow(self):
        self.assertEqual(E1_minus_2a_3**2, E1_minus_2a_3 * E1_minus_2a_3)
        self.assertEqual(
            E1_minus_2a_3**3, E1_minus_2a_3 * E1_minus_2a_3 * E1_minus_2a_3
        )
        self.assertEqual(
            E1_minus_2a_3**4,
            E1_minus_2a_3 * E1_minus_2a_3 * E1_minus_2a_3 * E1_minus_2a_3,
        )

    def test_str(self):
        self.assertEqual(str(E2a_3), "2a³")
        self.assertEqual(str(Eneg_2a_3), "-2a³")
        self.assertEqual(str(E2a_neg_3), "2a⁻³")
        self.assertEqual(str(E4a_3), "4a³")
        self.assertEqual(str(E1_minus_4a_3), "1 - 4a³")
        self.assertEqual(str(E1_minus_2a_3), "1 - 2a³")
        self.assertEqual(str(E2a_3_plus_2a_neg_3), "2a³ + 2a⁻³")
        self.assertEqual(str(E2a_3_plus_1), "2a³ + 1")
        self.assertEqual(str(E2a_3_minus_1), "2a³ - 1")
        self.assertEqual(str(E2a_neg_3_plus_4y_8), "2a⁻³ + 4y⁸")
        self.assertEqual(str(E4a_3_minus_1), "4a³ - 1")
        self.assertEqual(str(E4a_3_plus_1), "4a³ + 1")
        self.assertEqual(str(Ex_plus_y), "x + y")
        self.assertEqual(str(Ex_minus_y), "x - y")
        self.assertEqual(str(Ex_2_minus_y_2), "x² - y²")
        self.assertEqual(str(Ex_2_plus_2xy_plus_y_2), "x² + 2xy + y²")
        self.assertEqual(str(E4y_8_minus_8a_3_y_8), "4y⁸ - 8a³y⁸")

    def test_in_place(self):
        anchor = Term(2, Variable("x")) #2x
        my_term = Term(2, Variable("x")) #2x
        x = Term(1, Variable("x"))

        self.assertEqual(anchor, my_term)
        my_term *= x #2x^2
        self.assertEqual(my_term, anchor*x)

        my_term = Term(2, Variable("x")) #2x
        self.assertEqual(anchor, my_term)
        my_term += x #3x
        self.assertEqual(my_term, anchor+x)

        my_term = Term(2, Variable("x")) #2x
        self.assertEqual(anchor, my_term)
        my_term -= x #x
        self.assertEqual(my_term, anchor-x)

        my_term = Term(2, Variable("x")) #2x
        self.assertEqual(anchor, my_term)
        my_term **= 2 #4x^2
        self.assertEqual(my_term, anchor**2)

print(__name__)
if __name__ == "__main__":
    
    unittest.main()
