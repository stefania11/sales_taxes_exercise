import unittest
from sales import *


class TestTaxesCalculation(unittest.TestCase):

    def test_tax_calculation(self):
        '''
        Tests sales taxe for all types of items
        '''
        # general
        item1 = Item(name='music CD', price=14.99, qty=1)
        tax = calculate_tax(item1.name, item1.price)
        result_price = total_price(item1.price, item1.qty, tax)
        self.assertEqual(result_price, 16.49)

        # # imported, general
        item2 = Item(name='imported bottle of perfume', price=27.99, qty=1)
        tax = calculate_tax(item2.name, item2.price)
        result_price = total_price(item2.price, item2.qty, tax)
        self.assertEqual(result_price, 32.19)

        # books
        item3 = Item(name='book', price=12.49, qty=1)
        tax = calculate_tax(item3.name, item3.price)
        result_price = total_price(item3.price, item3.qty, tax)
        self.assertEqual(result_price, 12.49)

        # imported, chocolate
        item4 = Item(name='imported box of chocolates', price=10.00, qty=1)
        tax = calculate_tax(item4.name, item4.price)
        result_price = total_price(item4.price, item4.qty, tax)
        self.assertEqual(result_price, 10.50)

        #  medical
        item5 = Item(name='packet of headache pills', price=10.00, qty=1)
        tax = calculate_tax(item5.name, item5.price)
        result_price = total_price(item5.price, item5.qty, tax)
        self.assertEqual(result_price, 10.00)


class TestOrderParsing(unittest.TestCase):
    def test_total_taxes(self):
        '''
        Calculate sum of all taxes in cart
        '''
        item1 = Item(name='book', price=12.49, qty=1)
        item2 = Item(name='music CD', price=14.99, qty=1)
        item3 = Item(name='chocolate bar', price=0.85, qty=1)
        order_list = [item1, item2, item3]
        output, summary = parse_order(order_list)
        total_tax = summary['tax']
        self.assertEqual(total_tax, 1.50)

    def test_total_price(self):
        '''
        Sum of all prices and taxes
        '''
        item1 = Item(name='book', price=12.49, qty=1)
        item2 = Item(name='music CD', price=14.99, qty=1)
        item3 = Item(name='chocolate bar', price=0.85, qty=1)
        order_list = [item1, item2, item3]
        output, summary = parse_order(order_list)
        total_price = summary['total']
        self.assertEqual(total_price, 29.83)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
