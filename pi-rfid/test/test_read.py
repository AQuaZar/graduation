import unittest
from rfid.tRead import Reader


class TestReadCycle(unittest.TestCase):
    def setUp(self):
        self.func = Reader()

    def test_readTag(self):
        self.assertEqual(self.func.readTag(),(219473183670, 'c9d639271761723567ba36172354c0c7ac542831        '))
    def test_requestAccess_1(self):
        self.assertEqual(self.func.requestAccess('c9d639271761723567ba36172354c0c7ac542831'),
        (b'{"message":"Access granted to Yulia Cactusova"}',200))
    def test_requestAccess_2(self):
        self.assertEqual(self.func.requestAccess('d86ccdfaaa112d91a63eb843738fa97507e64e23'),
        (b'{"message":"Access granted to Anton Poznyakov"}',200))
    def test_requestAccess_3(self):
        self.assertEqual(self.func.requestAccess(''),
        (b'{"detail":"Invalid token header. No credentials provided."}',401))
    def test_requestAccess_4(self):
        self.assertEqual(self.func.requestAccess('qwerty123'),
        (b'{"detail":"Invalid token."}',401))
    def test_authorization_success(self):
        self.assertEqual(self.func.authorization(200),"Authorized")
    def test_authorization_fail(self):
        self.assertEqual(self.func.authorization(400),"Access denied")

if __name__ == "__main__":
    unittest.main()
