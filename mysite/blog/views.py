from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'name': 'Malika',
               'age': 35,
               'job': 'programmist',
               }
    return render(request, template_name='blog/index.html', context=context)


def index1(request):
    context = {'name1': 'Alim',
               'age1': 11,
               'job1': 'templates'}
    return render(request, template_name='blog/index1.html', context=context)


# def index2(request):
#     context = {'name': 'Malika',
#                'age': 35,
#                'job': 'programmist'}
#     return render(request, template_name='blog/index.html', context=context)
#
#
# def index3(request):
#     context = {'name': 'Malika',
#                'age': 35,
#                'job': 'programmist'}
#     return render(request, template_name='blog/index.html', context=context)
#
#
# def index4(request):
#     context = {'name': 'Malika',
#                'age': 35,
#                'job': 'programmist'}
#     return render(request, template_name='blog/index.html', context=context)
#
#
# def index5(request):
#     context = {'name': 'Malika',
#                'age': 35,
#                'job': 'programmist'}
#     return render(request, template_name='blog/index.html', context=context)
