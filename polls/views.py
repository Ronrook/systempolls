
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import CreatePollForm
from .models import Poll, Choice


def home(request):
    # Solicitamos todos los ojetos de la clase Poll  
    polls = Poll.objects.all()
    choices = Choice.objects.all()
    # Creamos el contexto con los objetos Poll
    
    context = {
        'polls': polls,
        'choices': choices
    }
    #Retornamos la vista Home y le enviamos el contexto
    return render(request, 'poll/home.html', context)



def create(request):
    # Validar si el metodo Http es POST
    if request.method == 'POST':
        # Guardar la peticion
        form = CreatePollForm(request.POST)
        # Validar si es valida
        if form.is_valid():
            form.save()

            return redirect('home')


    else:
        form = CreatePollForm()

    context = {
        'form': form
    }
    return render(request, 'poll/create.html',  context)




def vote(request, poll_id):
    # Solicitamos un ojeto Poll por medio de su ID 
    poll = Poll.objects.get(pk= poll_id)

     # Validar si el metodo Http es POST
    if request.method == 'POST':

         # selecionar el campo del metodo Post
        selected_option = request.POST['poll']

         # Validar el valor del campo selecionado
        if selected_option == 'option1':
            poll.option_one_count += 1

        elif selected_option == 'option2':
             poll.option_two_count += 1


        elif selected_option == 'option3':
             poll.option_three_count += 1

        else:
            return HttpResponse(400, 'Invalid form option' )
        

        poll.save()

        return redirect('results', poll_id)


    
    context = {
        'poll': poll
    }
    
    
    return render(request, 'poll/vote.html',  context)


def results(request,  poll_id ):
    # Solicitamos un ojeto Poll por medio de su ID 
    poll = Poll.objects.get(pk= poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html',  context)