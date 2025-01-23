from django.shortcuts import render
from .utils import generate_summary



# View to display the form and generate the summary

def summary_view(request):
    summary = None
    text = ""
    if request.method == 'POST':
        # Retrieve the text from the form
        text = request.POST.get('text')
        if text:
            # Generate the summary
            summary = generate_summary(text)
    context = {
            'summary': summary, 
            'text': text,
        }
    
    return render(request, 'summary/summary.html', context=context)
