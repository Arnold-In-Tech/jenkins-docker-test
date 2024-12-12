import unittest
from unittest.mock import patch

# Mock for redis
import mockredis
import hitcount

class HitCountTest(unittest.TestCase):

    @patch('hitcount.r', mockredis.mock_strict_redis_client(host='0.0.0.0', port=6379, db=0))
    def testOneHit(self):
        # increase the hit count for user1
        hitcount.hit("user1")
        # ensure that the hit count for user1 is just 1
        self.assertEqual(b'1', hitcount.getHit("user1"))


if __name__ == '__main__':
    unittest.main()
        

# In the first line, we are importing the unittest Python module that provides the necessary framework and functionality to run the unit test and generate a detailed report on the test execution process. 
# In the second line, we are importing the hitcount Python module, where we are soon going to implement the hit count functionality. 
# We then continue to add the test code that would test the hitcount module's functionality.   

# What the test is doing is “making a hit” or visiting the redis server using the patch method, which effectively registers the visit/hit by increasing the count by one as indicated by the comments (in #). Finally, the term ‘assertion’  in the function self.assertEqual(), compares the hit-count that we expect (1) to the one that is there at the current time. If they match, the test will pass, if not it will fail and report what caused the failure. Otherwise it will run successfully and give us the “OK”. 
