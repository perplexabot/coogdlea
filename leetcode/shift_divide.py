"""divide without dividing function"""

# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
# Return the quotient after dividing dividend by divisor.
# The integer division should truncate toward zero.
def divide(dividend, divisor):
    """Divide two integers without using divide or modulo operators
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    def shift_divide(numerator, denominator, acc_sum=0):
        """recurse shift divide function for positive ints"""
        if numerator < denominator:
            return acc_sum

        cnt = 0
        old_denominator = denominator
        while denominator <= numerator:
            cnt += 1
            denominator <<= 1
        cnt -= 1
        denominator >>= 1
        return shift_divide(numerator-denominator, old_denominator, acc_sum+2**cnt)

    positive = (-1, 1)[dividend > 0] == (-1, 1)[divisor > 0]
    absolute_value_numerator, absolute_value_denominator = abs(dividend), abs(divisor)

    total = shift_divide(absolute_value_numerator, absolute_value_denominator)
    total = total if positive else -total

    return (2**31) - 1 if (total < - 2**31 or total > (2**31) - 1) else total
