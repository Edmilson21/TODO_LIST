from asyncio.windows_events import NULL
from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContacForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages



# Búsqueda
 
  

def index(request, letter = NULL):
        if letter != NULL:
             contacts = Contact.objects.filter(name__istartswith=letter)
        else:
            contacts = Contact.objects.filter(name__icontains=request.GET.get('search', '')) 

        context = {
            'contacts':contacts
            }
        return render(request, 'contact/index.html', context)


# Vista Detalles

def view(request, id):
    contact = Contact.objects.get(id=id)
    contexto = {
        'contact':contact
    }
    return render(request, 'contact/detail.html', contexto)


# Vista Editar

def edit(request, id):
    contact = Contact.objects.get(id=id)

    if (request.method == 'GET'):
        form = ContacForm(instance=contact) # Aqui se está forzando la instancia para saber exactamente en que formulario estamos
        context = {
            'form':form,
            'id': id
        }
        return render(request, 'contact/edit.html',context)

    if (request.method == 'POST'):
        form = ContacForm(request.POST, instance = contact)
        if form.is_valid():
            form.save()
        
        context = {
            form:'form',
            'id': id
        }
        messages.success(request,'Contacto Actualizado!')
        return render(request, 'contact/edit.html',context)
 


# Vista Crear

def create(request):
     if request.method == 'GET':
          form = ContacForm()
          context = {
                'form':form
          }
          return render(request, 'contact/create.html', context)
     
     if request.method == 'POST':
                form = ContacForm(request.POST)
                if form.is_valid():
                     form.save()
                return redirect('contact')
     

# Vista Borrar

def delete(request,id):
     contact = Contact.objects.get(id=id)
     contact.delete()
     return redirect('contact')                
               

     