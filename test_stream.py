import unittest
from stream import Stream


class Stream_test(unittest.TestCase):
    """
    Test class.
    """
    list_1 = [4, 12, 3, 8, 17, 12, 1, 8, 7]
    list_1_str = [str(d) for d in list_1]
    names = ['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez',
        'Howe', 'Ray', 'Navarro', 'Talley', 'Bernard', 'Gomez', 'Hamilton',
        'Case', 'Petty', 'Lott', 'Casey', 'Hall', 'Pena', 'Witt', 'Joyner',
        'Raymond', 'Crane', 'Hendricks', 'Vance', 'Cleveland', 'Duncan', 'Soto',
        'Brock', 'Graham', 'Nielsen', 'Rutledge', 'Strong', 'Cox']

    # tests for stream generation function
    def test_stream_generation(self):
        #
        result = Stream(self.list_1).source() \
            .get()
        self.assertEqual(self.list_1, result)


    # tests for filter() function
    def test_filter_1(self):
        #
        # test Challenge 1
        result = Stream(self.list_1).source() \
            .filter(lambda n : n % 2 == 1) \
            .get()
        self.assertEqual([3, 17, 1, 7], result)

    def test_filter_11(self):
        result = Stream(self.list_1).source() \
            .filter(lambda d : False) \
            .get()
        self.assertEqual([], result)

    def test_filter_12(self):
        result = Stream(self.list_1).source() \
            .filter(lambda d : True) \
            .get()
        self.assertEqual(self.list_1, result)

    def test_filter_13(self):
        result = Stream(self.names).source() \
            .filter(lambda n : len(n) == 4) \
            .get()
        self.assertEqual(['Gill', 'Howe', 'Case', 'Lott', 'Hall', 'Pena', 'Witt', 'Soto'], result)


    # tests for map() function
    def test_map_2(self):
        #
        # test Challenge 2
        result = Stream(self.names).source() \
            .slice(8) \
            .map(lambda n : len(n)) \
            .get()
        self.assertEqual([8, 4, 6, 10, 7, 7, 4, 3], result)

    def test_map_21(self):
        result = Stream(self.names).source() \
            .filter(lambda n : len(n) == 3) \
            .map(lambda n : (n, len(n))) \
            .get()
        self.assertEqual([('Ray', 3), ('Cox', 3)], result)


    # tests for reduce() function
    def test_reduce_3(self):
        #
        # test Challenge 3
        result = Stream(self.names).source() \
            .slice(8) \
            .map(lambda n : len(n)) \
            .reduce(lambda x, y : x + y)
        self.assertEqual(49, result)

    def test_reduce_31(self):
        # test Challenge 3.1
        n = 3
        result = Stream(self.names).source() \
            .filter(lambda name : len(name) == n) \
            .map(lambda n : n.upper()) \
            .reduce(lambda x, y : str(x) + str(y), '')
        self.assertEqual('RAYCOX', result)
        #
        n = 5
        result = Stream(self.names).source() \
            .filter(lambda name : len(name) == n) \
            .map(lambda n : n.upper()) \
            .reduce(lambda x, y : str(x) + str(y), '')
        self.assertEqual('GOMEZPETTYCASEYCRANEVANCEBROCK', result)


    # tests for sort() function
    def test_sort_4(self):
        # test Challenge 4
        result = Stream(self.names).source() \
            .slice(8) \
            .sort() \
            .get()
        expected = ['Buckner', 'Gill', 'Gonzalez', 'Hardin', 'Howe', 'Marquez', 'Ray', 'Richardson']
        self.assertEqual(expected, result)

    def alpha_comperator(self, n1, n2):
        return -1 if n1 < n2 else 1

    def len_alpha_comperator(self, n1, n2):
        return -1 if len(n1) < len(n2) else 1 if len(n1) > len(n2) else self.alpha_comperator(n1, n2)

    def test_sort_41(self):
        # test Challenge 4.1
        result = Stream(self.names).source() \
            .sort(self.len_alpha_comperator) \
            .get()
        #
        expected = ['Cox', 'Ray', 'Case', 'Gill', 'Hall', 'Howe', 'Lott', 'Pena', 'Soto', 'Witt',
            'Brock', 'Casey', 'Crane', 'Gomez', 'Petty', 'Vance', 'Duncan', 'Graham', 'Hardin',
            'Joyner', 'Strong', 'Talley', 'Bernard', 'Buckner', 'Marquez', 'Navarro', 'Nielsen',
            'Raymond', 'Gonzalez', 'Hamilton', 'Rutledge', 'Cleveland', 'Hendricks', 'Richardson'
        ]
        self.assertEqual(expected, result)

    def test_sort_42(self):
        # test Challenge 4.2
        result = Stream(self.names).source() \
            .sort(self.len_alpha_comperator) \
            .map(lambda n : (n, n[::-1].capitalize(), len(n))) \
            .filter(lambda n1 : n1[2] % 2 == 1) \
            .get()
        #
        expected = [('Cox', 'Xoc', 3), ('Ray', 'Yar', 3), ('Brock', 'Kcorb', 5), ('Casey', 'Yesac', 5),
            ('Crane', 'Enarc', 5), ('Gomez', 'Zemog', 5), ('Petty', 'Yttep', 5), ('Vance', 'Ecnav', 5),
            ('Bernard', 'Dranreb', 7), ('Buckner', 'Renkcub', 7), ('Marquez', 'Zeuqram', 7),
            ('Navarro', 'Orravan', 7), ('Nielsen', 'Neslein', 7), ('Raymond', 'Dnomyar', 7),
            ('Cleveland', 'Dnalevelc', 9), ('Hendricks', 'Skcirdneh', 9)
        ]
        self.assertEqual(expected, result)
        #
        result = Stream(self.names).source() \
            .sort(self.len_alpha_comperator) \
            .map(lambda n : (n, n[::-1].capitalize(), len(n))) \
            .filter(lambda n1 : n1[2] % 2 == 1) \
            .count()
        self.assertEqual(16, result)


    # report results,
    # see https://stackoverflow.com/questions/28500267/python-unittest-count-tests
    # currentResult = None

    # @classmethod
    # def setResult(cls, amount, errors, failures, skipped):
    #     cls.amount, cls.errors, cls.failures, cls.skipped = \
    #         amount, errors, failures, skipped

    # def tearDown(self):
    #     amount = self.currentResult.testsRun
    #     errors = self.currentResult.errors
    #     failures = self.currentResult.failures
    #     skipped = self.currentResult.skipped
    #     self.setResult(amount, errors, failures, skipped)

    # @classmethod
    # def tearDownClass(cls):
    #     print("\ntests run: " + str(cls.amount))
    #     print("errors: " + str(len(cls.errors)))
    #     print("failures: " + str(len(cls.failures)))
    #     print("success: " + str(cls.amount - len(cls.errors) - len(cls.failures)))
    #     print("skipped: " + str(len(cls.skipped)))

    # def run(self, result=None):
    #     self.currentResult = result # remember result for use in tearDown
    #     unittest.TestCase.run(self, result) # call superclass run method


if __name__ == '__main__':
    result = unittest.main()

