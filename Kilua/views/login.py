from django.shortcuts import RequestContext, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required



def logar(request):

    context = RequestContext(request)



    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/kilua/controle/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Sua conta foi desabilitada.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Login invalido: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:

        return render_to_response('login.html', {}, context)


@login_required
def user_logout(request):

    logout(request)


    return HttpResponseRedirect('/kilua/login/')