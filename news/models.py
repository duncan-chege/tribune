from django.db import models
import datetime as dt   #returns a specific day

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank= True)       #blank =True allows us to add NULL values to our database.

    #add an __str__ that will return a string representation of our model, useful when we want to view our returned queries.
    def __str__(self):
        return self.first_name
  
    def save_editor(self):
        self.save()

    class Meta:     #Meta subclass specifies model-specific options. This helps in ordering data
        ordering = ['first_name']
        

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    class Meta:     #Meta subclass specifies model-specific options. This helps in ordering data
        verbose_name_plural = 'Tags'

class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)      #create a foreign key column that will store the ID of the Editor from the Editor table.
    tags = models.ManyToManyField(tags)     #a many to many relationship telling django to create a separate join table.
    pub_date = models.DateTimeField(auto_now_add = True)     #stores the exact date and time our article was posted
    article_image = models.ImageField(upload_to = 'articles/')

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):    #this method filters the model data according to the given date and returns it
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):       #method will allow us to filter the all the Articles in our database and return ones matching to our search query
        news = cls.objects.filter(title__icontains=search_term)     #filter the model data using the __icontains query filter. This filter will check if any word in the titlefield of our articles matches the search_term.
                                            #the same search_term in views.py
        return news

    class NewsLetterRecepients(models.Model):
        name = models.CharField(max_length= 30)
        email = models.EmailField()

        