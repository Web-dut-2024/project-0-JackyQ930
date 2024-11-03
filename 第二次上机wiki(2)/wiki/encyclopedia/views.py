from django.shortcuts import render
from . import util
from django.shortcuts import render, redirect


def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

import markdown2

def entry_page(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    else:
        content = markdown2.markdown(content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })

def search(request):
    query = request.GET.get('q')
    if not query:
        return redirect('index')
    
    # 完全匹配的条目
    if util.get_entry(query):
        return redirect('entry_page', title=query)
    
    # 部分匹配的条目
    results = [entry for entry in util.list_entries() if query.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html", {
        "results": results,
        "query": query
    })

from django.http import HttpResponseRedirect
from django.urls import reverse

def create_new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        # 如果条目已存在，返回错误
        if util.get_entry(title):
            return render(request, "encyclopedia/error.html", {
                "message": "An entry with this title already exists."
            })
        
        # 保存新条目
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry_page", args=[title]))
    
    return render(request, "encyclopedia/new.html")

def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        # 更新条目
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry_page", args=[title]))
    
    # 获取现有内容
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

import random

def random_page(request):
    entries = util.list_entries()
    random_title = random.choice(entries)
    return HttpResponseRedirect(reverse("entry_page", args=[random_title]))
