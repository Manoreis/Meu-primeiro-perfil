'''DICIONÁRIO
Exercício nº10
Armazenar uma contagem de palavras em um texto usando um dicionário, onde as palavras são os atributos e as contagens são os valores.'''



wordstring = 'foi o exercício mais difícil da lista, o pior dos tempos '
wordstring += 'a idade da sabedoria contra a idade da ignorância'
wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("Lista\n" + str(wordlist) + "\n")
print("Frequências\n" + str(wordfreq) + "\n")
print("Pares\n" + str(list(zip(wordlist, wordfreq))))