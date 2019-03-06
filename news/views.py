# from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
from .models import Article,NewsLetterRecipients
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

#create your views here    
def news_today(request):
    date=dt.date.today()
    news = Article.todays_news()
    if request.method == 'POST':        # form will be submitting sensitive data to the database we are going to use a POST request. 
        form = NewsLetterForm(request.POST)     #pass in the POST request values as an argument.
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name, email = email)
            recipient.save()
            send_welcome_email(name,email)
            form = NewsLetterForm()     #instead of showing post request argument show empty form no need to give HttpResponseRedirect()
            
            HttpResponseRedirect('news_today')      #redirect the user back to the news_today view function.
    else:
        form = NewsLetterForm()     #If it is not a POST request we just create an empty form instance and then we pass it to our template.
        
    return render(request, 'all-news/today-news.html', {"date": date, "news":news, "letterForm": form})     #the last argument is a dictionary of values that we pass into the template
                                                                #referred to as the Context in Django
    return HttpResponse(html)

# View Function to present news from past days
def past_days_news(request,past_date):
    #error handling to make sure the user inserts a proper date and our date conversion doesn't break
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)
    
    news = Article.days_news(date)      #we pass in the date got from the url.
    return render(request, 'all-news/past-news.html', {"date": date,"news":news})

def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")        #article is the query itself for the name of the actual input in the search form
        searched_articles = Article.search_by_title(search_term)
        
        return render(request, 'all-news/search.html',{"articles": searched_articles})

@login_required(login_url='/accounts')
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)      #query the database for a single object using the get function. and pass in the article_id.
    except ObjectDoesNotExist:
        raise Http404
    return render(request,"all-news/article.html", {"article": article})
    
