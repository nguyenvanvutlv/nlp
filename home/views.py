from django.shortcuts import render
from django.conf import settings
from home.text import preprocess, bert


def home(request):
    result = "NONE"
    text = ""
    if request.method == "POST":
        text = request.POST.get('user_text')
        result = bert(settings.MODEL,
                      settings.TOKENIZER,
                      preprocess(text,
                                 settings.POS,
                                 settings.NEG,
                                 settings.REPLACE_LIST))
        print(text, result)
    return render(request, 'base.html', {"processed_text": result, "text" : text})