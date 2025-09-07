# Dictonary Concept

acr = {'LOL': 'Laugh out Loud',
        'TBH': 'To Be Honest',
        'IDK': 'I dont Care'}

sentence = 'IDK '+ 'What you Think '+ 'TBH'
Translation = acr.get('IDK') + ' What you Think '+ acr.get('TBH')

print('sentence:', sentence)
print('Translation:',Translation)
