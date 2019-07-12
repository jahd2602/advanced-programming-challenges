from compression_and_decompression import decompress_string
from unittest import TestCase


class DecompressTest(TestCase):

    def test_example(self):
        test_input = "3[abc]4[ab]c"
        expected_output = "abcabcabcababababc"
        result = decompress_string(test_input)
        self.assertEqual(expected_output, result)

