import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    def setUp(self):
        self.news_source = Source('abc-news-au','ABC News (AU)', 'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.')

    def test_instance(self):
        self.assertTrue(isinstance(self.news_source,Source))

    def test_init(self)
        self.assertEqual( self.news_source.id, 'abc-news-au')
        self.assertEqual( self.news_source.name, 'ABC News (AU)')
        self.assertEqual( self.news_source.description, 'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.')
