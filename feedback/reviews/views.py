from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .models import Review
# from .models import Review

# Create your views here.

class ReviewView(CreateView):
    model = Review
    template_name = 'reviews/review.html'
    form_class = ReviewForm
    success_url = '/thank-you'

    # template_name = 'reviews/review.html'
    # form_class = ReviewForm
    # success_url = '/thank-you'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def get(self, request):
    #     form=ReviewForm()
    #     return render(request, 'reviews/review.html',{
    #         'form': form
    #     })   

    # def post(self, request):
    #     form=ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/thank-you')
    #     return render(request, 'reviews/review.html',{
    #         'form': form
    #     })
     
# def review(request):
#     if request.method == 'POST':
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating']
#             # )
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#     else:
#         form=ReviewForm()

#     return render(request, 'reviews/review.html',{
#         'form': form
#     })   

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['message'] = "Thank you for your feedback!"
        return context
    
# class ReviewListView(TemplateView):
#     template_name = 'reviews/review-list.html'

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         reviews=Review.objects.all()
#         context['reviews']=reviews
#         return context

class ReviewListView(ListView):
    template_name = 'reviews/review-list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query=super().get_queryset()
        data=base_query.filter(rating__gte=4)
        return data
    
# class SingleReviewView(TemplateView):
#     template_name = 'reviews/single_review.html'

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         review_id=kwargs['id']
#         selected_review=Review.objects.get(pk=review_id)
#         context['review']=selected_review
#         return context

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        loaded_review=self.object
        request=self.request
        favorite_id=request.session.get('favorite_review')
        context['is_favorite']=str(loaded_review.id)==favorite_id
        return context

class AddFavoriteView(View):
    def post(self, request):
        review_id=request.POST['review_id']
        request.session['favorite_review']=review_id
        return HttpResponseRedirect('/reviews/'+review_id)