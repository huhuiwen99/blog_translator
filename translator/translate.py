from googletrans import Translator

def translator(text):
    trans = Translator()
    output =  trans.translate(text = text, dest = 'chinese (simplified)')
    return output.text