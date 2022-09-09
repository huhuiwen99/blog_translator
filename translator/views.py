from django.shortcuts import render
from . import translate
# Create your views here.
def translator_view(request):
    if request.method == 'POST':
        input_text = request.POST['my_textarea']
        output_text = translate.translator(input_text)
        return render(request, 'translator.html', {'input_text':input_text, 'output_text': output_text})
    else:    
        return render(request, 'translator.html')