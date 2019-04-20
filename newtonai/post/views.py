from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from post.models import Post
import json
import random

class HomePageView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['post'] = Post.objects.all()
		return context

	def post(request):
		if request.method == 'POST':
			obj = json.loads(request.body.decode('utf8').replace("'", '"'))

			ran = random.randint(0, len(obj['ids'])-1)
			
			result = Post.objects.get(pk=obj['ids'][ran])
			data = {
		        'title': result.title,
		        'content': result.content,
		        'date_add': result.date_add,
		        'user_add': result.user_add.username,
		        'image': str(result.image),
		        'active': result.active 
    		}
			return JsonResponse(data)

