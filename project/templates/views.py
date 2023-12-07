from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    info_me = {'phone': '+7-953-412-88-90', 'telegram': 'Vladis_lav', 'github': 'https://github.com/olimech'}
    return render(request, 'contacts.html', context={'info_me': info_me})


def form(request):
    # info_user = {'user': name, 'email_user': email, 'pol_user': pol }
    return render(request, 'form.html')


# class Person:
#     def __init__(self, name, email, pol):
#         self.name = name
#         self.email = email
#         self.pol = pol


