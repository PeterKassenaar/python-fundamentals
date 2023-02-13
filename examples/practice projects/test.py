#  Lijst met woorden, je wilt de gemiddelde lengte van elk woord weten.
from statistics import mean

woorden = "Het was een koude, donkere winteravond en Jochem vroeg zich af of hij naar huis zou gaan".split()
# print(words)
# print ('aantal woorden: ', len(words))
lengtes = []
for word in woorden:
    lengtes.append(len(word))
    # With comprehension
# print(lengths)
# lengtes = [len(woord) for woord in woorden ]
gemiddelde = mean(lengtes)
print("Jouw zin: ", woorden)
print("Gemiddelde woordlengte: ", round(gemiddelde, 1))
