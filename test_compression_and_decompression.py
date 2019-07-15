from compression_and_decompression import decompress_string
from unittest import TestCase


class DecompressTest(TestCase):

    def test_example(self):
        test_input = "3[abc]4[ab]c"
        expected_output = "abcabcabcababababc"
        result = decompress_string(test_input)
        self.assertEqual(expected_output, result)

    def test_number_with_more_than_one_digit(self):
        test_input = "10[a]"
        expected_output = "aaaaaaaaaa"
        result = decompress_string(test_input)
        self.assertEqual(expected_output, result)

    def test_repetition_inside_another(self):
        test_input = "2[3[a]b]"
        expected_output = "aaabaaab"
        result = decompress_string(test_input)
        self.assertEqual(expected_output, result)

