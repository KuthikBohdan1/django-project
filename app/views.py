from django.shortcuts import render
# from app.models import 
# Create your views here.
# from app.models import TypeRoom, Room

def site(request):
    text = "hi from vives"

    context = {
        "all_text": text
    }

    return render(
        request,
        template_name="page.html",
        context=context,
        
    )
