from django.shortcuts import redirect

def redirect_to_chat(request):
    return redirect("room")