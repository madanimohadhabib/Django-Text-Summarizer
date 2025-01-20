from django.shortcuts import render
from .utils import generate_summary

# Vue pour afficher le formulaire et générer le résumé
def summary_view(request):
    summary = None
    text = ""
    if request.method == 'POST':
        # Récupérer le texte du formulaire
        text = request.POST.get('text')
        if text:
            # Générer le résumé
            summary = generate_summary(text)
    context = {
            'summary': summary, 
            'text': text,
        }
    
    return render(request, 'summary/summary.html', context=context)
