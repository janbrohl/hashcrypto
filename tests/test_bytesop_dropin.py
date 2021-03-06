import unittest
import hashcrypto.bytesop_fallback


def ba(*args):
    return bytes(bytearray(*args))


class TestUtilFunctions(unittest.TestCase):

    def test_b_xor(self):
        b = ba(range(32))
        self.assertEqual(ba(32), ba(hashcrypto.bytesop_fallback.op_xor(b, b)))
        self.assertEqual(b, ba(hashcrypto.bytesop_fallback.op_xor(b, ba(32))))

if __name__ == '__main__':
    unittest.main()
