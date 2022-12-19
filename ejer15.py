text = 'zip da mucha pereza pero hay que usar zip'

buscar = text.find('zip') + 1
buscar_sig = text.find('zip', buscar)
print(buscar_sig)