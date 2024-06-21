from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .forms import ReviewForm
# Create your views here.


def index(request):

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, "reviews/review.html", {
        "form": form
    })


def thankyou(request):
    return render(request, "reviews/thankyou.html")
