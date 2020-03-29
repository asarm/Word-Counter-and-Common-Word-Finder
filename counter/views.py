from django.shortcuts import render
from collections import Counter

# Create your views here.
text=""


def index(request):
    context = {'text':text}
    return render(request, 'counter/index.html', context)


def counter(request):
    posted_text = request.POST['posted_text']

    #prevents to deleting old text, while going previous page
    global text
    text = posted_text
    
    words = posted_text.split()
    word_count = len(words)
    used_words = Counter(words)
    common_words = used_words.most_common(2)
    context = {'word_count': word_count,
               'common_word': common_words[0][0],
               'count': common_words[0][1]}
    return render(request, 'counter/result.html', context)
