from django.shortcuts import render
from .models import Allitem, Review, Store, Store_set, Today_lineup
from django.http import HttpResponse

# Create your views here.
def index(request):
    allreview = Review.objects.all()
    jcaron_review = Review.objects.filter(id="1")
    context = {
        'allreview' : allreview,
        'jcaron_review' : jcaron_review
    }
    return render(request, 'manager/index.html', context)

def allmenu(request):
    store = Store.objects.get(biz_name="제이카롱")
    macaronjcaron = Allitem.objects.filter(item_category="마카롱", store=store)
    macaron = Allitem.objects.filter(item_category="마카롱")
    package = Allitem.objects.filter(item_category="포장방법")
    
    store_setup = Store_set.objects.all()

    review_all = Review.objects.all()

    lineups = Today_lineup.objects.all()

    context={
        'macaron':macaron,
        'store' : store,
        'macaronjcaron' :macaronjcaron,
        'package':package,
        'store_setup' : store_setup,
        'review_all' : review_all,
        'lineups' : lineups,
    }
    return render(request, 'manager/allmenu.html', context)


def test(request, biz_url):
    sample = Store.objects.all()
    context = {
        'sample' : sample, 
    }
    
    return render(request, 'manager/test.html', context)
   