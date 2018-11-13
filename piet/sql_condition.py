class SQLCondition:

    def __init__(self, condition, logical_operator='AND'):
        self.condition = condition
        self.logical_operator = logical_operator

    def get_c_snippet(self, first_condition=True):
        c_snippet = self.condition
        if first_condition is False:
            c_snippet = ' {l} {c}'.format(
                l=self.logical_operator, c=c_snippet)
        return c_snippet


class SQLConditionsHandler:

    def __init__(self, logical_operator='AND'):
        self.c_list = []
        self.logical_operator = logical_operator

    def add_condition(self, condition, logical_operator='AND'):
        condition.logical_operator = logical_operator
        self.c_list.append(condition)

    def get_c_snippet(self, first_condition=True):
        for ind, c in enumerate(self.c_list):
            if ind == 0:
                c_snippet = c.get_c_snippet()
            else:
                c_snippet += c.get_c_snippet(first_condition=False)

        c_snippet = '({})'.format(c_snippet)

        if first_condition is False:
            c_snippet = ' {l} {c}'.format(
                l=self.logical_operator, c=c_snippet)

        return c_snippet


if __name__ == '__main__':
    a = SQLCondition('os=\'ios\'')
    b = SQLCondition('os=\'android\'', 'OR')
    c = SQLCondition('event_name=\'Intake\'')
    d = SQLCondition('event_name=\'NotIntake\'', 'OR')
    A = SQLConditionsHandler()
    B = SQLConditionsHandler()
    C = SQLConditionsHandler()

    A.add_condition(a)
    A.add_condition(b)

    print(A.get_c_snippet())

    B.add_condition(c)
    B.add_condition(d)

    C.add_condition(A)
    C.add_condition(B)

    print(C.get_c_snippet())
