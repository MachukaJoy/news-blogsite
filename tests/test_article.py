import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("Wildfire’s Rapid Spread Worries New Mexico Officials - The New York Times","https://static01.nyt.com/images/2022/05/01/world/01new-mexico-fire1/01new-mexico-fire1-facebookJumbo.jpg","The fire authorities in the state were bracing for more high winds, more smoke and more evacuees.","2022-05-01T13:47:15Z","https://www.engadget.com/wikipedia-editors-vote-to-block-cryptocurrency-donations-113549175.html")

    def test_instance(self):
        '''
        Test to check creation of new article instance
        '''
        self.assertTrue(isinstance(self.new_article,Article))



if __name__=='__main__':
    unittest.main()  