from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Choice, Settings

# Create your views here.
def raw_index(request):
  lates_question_list = Question.objects.order_by('-pub_date')[:5]
  output = ''

  for a in lates_question_list:
    output += f"{a.question_text}<br>"
    # option list
    option_list = Choice.objects.filter(question=a)
    for b in option_list:
      output += f"{b.choice_text}<br>"
    output += "<br>"
  return HttpResponse(output)

def html_version(request):
  question_list = Question.objects.all()
  answer_list = Choice.objects.all()
  context = {
    'questions_option': question_list,
    'answer': answer_list
  }
  return render(request, 'form.html', context)

def index_other(request):
  latest_question = Question.objects.order_by('-pub_date')[:5]
  output = ''
  
  for q in latest_question:
    output += f"{q.question_text}<br>"
    # answer list
    answer_list = Choice.objects.filter(question=q)
    list_answer = ", ".join([a.choice_text for a in answer_list])
    output += f"Pilihan: {list_answer}"
    output += "<br><br>"
  return HttpResponse(output)

def html_index(request):
  lates_question_list = Question.objects.order_by('-pub_date')[:5]
  # answer list
  answer_list = Choice.objects.all()
  context = {
    "latest_question_list": lates_question_list,
    "answer_list": answer_list
  }
  return render(request, "index.html", context)

def submit_vote(request, question_id):
    # TODO: Implement vote submission logic
    return HttpResponse("Vote submitted for question id: {}".format(question_id))

def profile(request):
  return HttpResponse('Hello world, you are at the profile page')

def contact(request):
  return HttpResponse('Hello world, you are at the contact page')

def address(request):
  return HttpResponse('My address is Jl. Pramuka No. 180, Kec. Gegerbitung, Kab. Sukabumi, Jawa Barat, Indonesia')

def phone(request):
  return HttpResponse('My phone number is +62 812-3456-7890')