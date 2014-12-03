import unittest

import json

from endpoints import reverse

class ReverseTestCase(unittest.TestCase):
    def runTest(self):
        r = reverse.Reverse()
        result = json.loads(r.index("your mom"))

        assert result['result'] == 'mom ruoy'
