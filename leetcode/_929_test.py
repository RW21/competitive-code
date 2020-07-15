from unittest import TestCase
from _929 import *


class _929_test(TestCase):
    def test_numUniqueEmails(self):
        assert Solution().numUniqueEmails(
            ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
        ) == 2
