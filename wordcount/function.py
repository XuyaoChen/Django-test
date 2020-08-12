#from django.http import HttpResponse
from django.shortcuts import render

#接收用户的请求，返回指定的网页
def home(request):
    return render(request, 'home.html')

def count(request):
    total_count = len(request.GET['text'])
    user_text = request.GET['text']

    word_dict = {}

    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(), key=lambda w:w[1], reverse=True)

    return render(request, 'count.html', {'count': total_count, 'usertext': user_text, 'worddict': word_dict, 'sorteddict': sorted_dict})
