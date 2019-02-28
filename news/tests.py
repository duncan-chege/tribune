from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.james = Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        
    #Testing instance to confirm that the object is being instantiated correctly.
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    #Testing save method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()      #query all the objects from the database.
        self.assertTrue(len(editors) >0)

class tagsTestClass(TestCase):
    def setUp(self):
        self.trendy = tags(name = "Trendy")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.trendy,tags))

    def test_save_method(self):
        self.trendy.save_tags()
        tag = tags.objects.all()      #query all the objects from the database.
        self.assertTrue(tags)

class ArticleTestClass(TestCase):
    def setUp(self):
        #Creating a new editor and saving it 
        self.james = Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        #Creating a new tag and saving it
        self.new_tag = tags(name="testing")
        self.new_tag.save()

        #creating a new article and saving it
        self.new_article= Article(title = 'Test Article', post = 'Random test post', editor = self.james)
        self.new_article.save()

        #adding that new tag to the article and saving it
        self.new_article.tags.add(self.new_tag)
        self.new_article.save()

    #method that will allow us to get today's news
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)      #Since we have saved a news article for that test we expect the method to return at least one news article

    #test that confirms getting news according to a given date

   #test to confirm getting news according to a given date.
    def test_get_news_by_date(self):
        test_date = '2019-02-20'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()       #convert test date string to a date object
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

    def tearDown(self):     #delete all instances of our models from the database after each test.
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

 

