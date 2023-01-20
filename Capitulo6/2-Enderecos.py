from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 Sao Paulo'
resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWkw2yPMM').geocode(endereco)

#resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWkw2yPMM').geocode(endereco).state
#resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWkw2yPMM').geocode(endereco).postal)code
#resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWkw2yPMM').geocode(endereco).country
#resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWkw2yPMM').geocode(endereco).coordinates

#resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWkw2yPMM').reverse_geocode(-23.5703022, -46.64512676)

print(resultado)