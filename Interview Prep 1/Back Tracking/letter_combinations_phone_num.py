"""Given a digit string, return all possible letter combinations
that the number could represent"""


def letter_combinations(digits):
    """
    :param digits: str
    """

    mapping = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}

    def combine(rst, remain_digits):

        # end condition
        if len(remain_digits) == 0:
            return rst

        if len(rst) == 0:
            rst = ['']

        nxt_rst = []

        digit = remain_digits.pop(0)
        for r in rst:
            print(r)
            for c in mapping[digit]:
                nxt_rst.append(r+c)
                print(nxt_rst)

        # nxt_rst = r+c
        return combine(nxt_rst, remain_digits)

    # first is current result
    return combine([], list(digits))


print(letter_combinations("46"))
