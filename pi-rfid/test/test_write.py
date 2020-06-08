import unittest
from rfid.tWrite import Writer


class TestWriteCycle(unittest.TestCase):
    def setUp(self):
        self.func = Writer()

    def test_requestToken(self):
        self.assertEqual(self.func.requestToken("c3ded5dce6c2ce089b271f974482647d645ad17e",
        "318367038610"),
        (200,b'{"token":"c9d639271761723567ba36172354c0c7ac542831","user_id":5,"email":""}'))
    # def test_requestToken_wrong_token(self):
    #     self.assertEqual(self.func.requestToken("c3ded5dce6c2fadsfae","318367038610"),
    #     (401,b'{"detail":"Invalid token."}'))
    # def test_requestToken_wrong_username(self):
    #     self.assertEqual(self.func.requestToken("c3ded5dce6c2ce089b271f974482647d645ad17e"
    #     ,"fagdsadga"),
    #     (400,b'{"non_field_errors":["Unable to log in with provided credentials."]}'))
    def test_writeToken(self):
        self.assertEqual(self.func.writeTokenOnTag(200,
        b'{"token":"c9d639271761723567ba36172354c0c7ac542831","user_id":5,"email":""}'),
        "Success! Data has been written. \n")
    # def test_writeToken_400(self):
    #     self.assertEqual(self.func.writeTokenOnTag(400,b'{"token":"c9dsaf","user_id":5,"email":""}'),
    #     "Bad request, make sure that user exists or check correctness of credentials. \n")
    # def test_writeToken_401(self):
    #     self.assertEqual(self.func.writeTokenOnTag(401,b'{"token":"c9dsaf","user_id":5,"email":""}'),
    #     "Access to server denied, check correctness of token. \n")

if __name__ == "__main__":
    unittest.main()
