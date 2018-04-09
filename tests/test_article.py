import unittest
from app.models import Article

class ArticleTest(object):
    """test to confirm the behaviour of the article class."""
    def setUp(self):
        self.new_article = Article('the-next-web','PlayStation\'s $30 PS4 gamepad for kids is totally adorable', 'https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2017/10/PS4-Mini-gamepad-social.jpg', 'Sony\'s teamed up with Hori on its new $30 Mini Wired Gamepad, which is designed for younger PS4 players with smaller hands.', 'https://thenextweb.com/gaming/2017/10/19/playstations-30-ps4-gamepad-for-kids-is-totally-adorable/', '2017-10-19T13:00:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

    def test_init(self):
        self.assertEqual( self.new_article.source, 'the-next-web')
        self.assertEqual( self.new_article.title, 'PlayStation\'s $30 PS4 gamepad for kids is totally adorable')
        self.assertEqual( self.new_article.urlToImage, 'https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2017/10/PS4-Mini-gamepad-social.jpg')
        self.assertEqual( self.new_article.description, 'Sony\'s teamed up with Hori on its new $30 Mini Wired Gamepad, which is designed for younger PS4 players with smaller hands.')
        self.assertEqual( self.new_article.urlToArticle, 'https://thenextweb.com/gaming/2017/10/19/playstations-30-ps4-gamepad-for-kids-is-totally-adorable/')
        self.assertEqual( self.new_article.publishedAt, '2017-10-19T13:00:00Z')
