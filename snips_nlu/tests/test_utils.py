import unittest

from snips_nlu.utils import LimitedSizeDict


class TestLimitedSizeDict(unittest.TestCase):
    def test_should_raise_when_no_size_limit(self):
        # Given/When/Then
        with self.assertRaises(ValueError) as ctx:
            LimitedSizeDict()
        self.assertEqual(ctx.exception.message,
                         "'size_limit' must be passed as a keyword argument")

    def test_should_initialize_with_argument(self):
        # Given
        sequence = [("a", 1), ("b", 2)]
        size_limit = 3
        # When
        d = LimitedSizeDict(sequence, size_limit=size_limit)
        # Then
        self.assertItemsEqual(d.items(), sequence)

    def test_should_initialize_without_argument(self):
        # Given
        size_limit = 10
        # When
        d = LimitedSizeDict(size_limit=size_limit)
        # Then
        self.assertItemsEqual(d.items(), [])

    def test_should_wrong_when_initialization_should_raise_error(self):
        # Given
        sequence = [("a", 1), ("b", 2), ("c", 3)]
        size_limit = len(sequence) - 1
        # When/Then
        with self.assertRaises(ValueError) as ctx:
            LimitedSizeDict(sequence, size_limit=size_limit)
        self.assertEqual(ctx.exception.message,
                         "Tried to initialize LimitedSizedDict with more "
                         "value than permitted with 'limit_size'")

    def test_should_erase_items_when_updating(self):
        # Given
        sequence = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
        size_limit = len(sequence) - 2
        # When
        my_dict = LimitedSizeDict(sequence[:size_limit], size_limit=size_limit)
        for k, v in sequence[size_limit:]:
            my_dict[k] = v
        # Then
        self.assertItemsEqual(my_dict.items(), sequence[size_limit:])


if __name__ == '__main__':
    unittest.main()