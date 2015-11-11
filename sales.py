import math
import settings


class Item(object):
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty


ORDERS = {
    'Order 1': [
        Item('book', 12.49, 1),
        Item('music cd', 14.99, 1),
        Item('chocolate bar', 0.85, 1)],
    'Order 2': [
        Item('imported box of chocolates', 10.00, 1),
        Item('imported bottle of perfume', 47.50, 1)],
    'Order 3': [
        Item('imported bottle of perfume', 27.99, 1),
        Item('bottle of perfume', 18.99, 1),
        Item('box of imported chocolates', 11.25, 1),
        Item('packet of headache pills', 9.75, 1)]
    }


def sales_tax(price):
    sales_tax = settings.SALES_TAX * price
    return round_tax(sales_tax)


def import_tax(price):
    import_tax = settings.IMPORT_TAX * price
    return round_tax(import_tax)


def round_tax(tax):
    return math.ceil(tax * settings.ROUND_UP_CEIL) / settings.ROUND_UP_CEIL


def total_price(price, quantity, tax):
    total_price = quantity * (price + tax)
    return round(total_price, 2)


def calculate_tax(item, price):
    total_tax = 0
    if item in settings.IMPORTED:
        tax = import_tax(price)
        total_tax += tax
    if item not in settings.EXCEPTIONS:
        tax = sales_tax(price)
        total_tax += tax
    return total_tax


def parse_order(order_list):
    output = []
    sales_taxes = 0
    total = 0
    for item in order_list:
        tax = calculate_tax(item.name, item.price)
        price_final = total_price(item.price, item.qty, tax)
        output.append([item.qty, item.name, price_final])
        sales_taxes += tax
        total += total_price(item.price, item.qty, tax)
    summary = {
        'tax': sales_taxes,
        'total': total
    }
    return output, summary


def print_receipt():
    output, summary = parse_order(ORDERS['Order 3'])
    for item in output:
        print "%s %s: %s" % tuple(item)
    print "Sales Taxes: %s" % summary['tax']
    print "Total: %s" % summary['total']


def main():
    print_receipt()


if __name__ == '__main__':
    main()
