import unittest

from generic_request_signer.exceptions import WebException, HttpMethodNotAllowed


class ExceptionsTests(unittest.TestCase):

    def test_web_exception_is_subclass_of_exception(self):
        self.assertTrue(issubclass(WebException, Exception))

    def test_web_exception_has_message(self):
        e = WebException('x')
        with self.assertRaises(AssertionError):
            with self.assertRaises(AttributeError):
                e.message

    def test_http_method_not_allowed_is_subclass_of_exception(self):
        self.assertTrue(issubclass(HttpMethodNotAllowed, Exception))
