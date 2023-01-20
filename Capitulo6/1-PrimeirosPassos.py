from pygeocoder import Geocoder

endereco = "12222, Lins de Vasconcelos, Sao Paulo, SP"

print(Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWkw2yPMM').geocode(endereco).coordinates)
