import nltk

# Faça os downloads dos pacotes comentados abaixo na primeira execução
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

texto = 'Mr. Green killed Coronel Mostard in the study with the candlestick. Mr. Green is not a very nice fellow'

frases = nltk.tokenize.sent_tokenize(texto)
print(frases)

tokens = nltk.word_tokenize(texto)
print(tokens)

classe = nltk.pos_tag(tokens)
print(classe)

entidades = nltk.chunk.ne_chunk(classe)
print(entidades)