import nltk
import pickle

# Faça os downloads dos pacotes comentados abaixo na primeira execução
# nltk.download('stopwords')
# nltk.download('rslp')

base = [('eu sou admirada por muitos', 'alegria'),
        ('eu amo você', 'alegria'),
        ('me sinto completamente amado', 'alegria'),
        ('amar e maravilhoso', 'alegria'),
        ('estou me sentindo muito animado novamente', 'alegria'),
        ('eu estou muito bem hoje', 'alegria'),
        ('que belo dia para dirigir um carro novo', 'alegria'),
        ('o dia está muito bonito', 'alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem', 'alegria'),
        ('o amor e lindo', 'alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

# Stop Words são palavras que não agregam siginificado para a emoção dos textos

# Stop Words geradas manualmente
stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

# Stop Words geradas pelo nltk
stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
# print(stopwords)


def removeStopWords(texto):
    frases = []
    for (palavras, emocao) in texto:
        semStop = []
        for p in palavras.split():
            if p not in stopwordsnltk:
                semStop.append(p)
        frases.append((semStop, emocao))
    return frases


# print(removeStopWords(base))


# Ao extrair o radical é possível que se perca um pouco da informação, mas de maneira geral
def extraiRadical(texto):
    stemmer = nltk.RSLPStemmer()
    frasesstemming = []
    for (palavras, emocao) in texto:
        comstemming = []
        for p in palavras.split():
            if p not in stopwordsnltk:
                comstemming.append(str(stemmer.stem(p)))
        frasesstemming.append((comstemming, emocao))
    return frasesstemming


frasesRadical = extraiRadical(base)
# print(frasesRadical)


def buscaPalavras(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras


palavras = buscaPalavras(frasesRadical)
# print(palavras)


def buscaFrequencia(palavras):
    return nltk.FreqDist(palavras)


frequencia = buscaFrequencia(palavras)
# print(frequencia.most_common(50))


def buscaPalavrasUnicas(frequencia):
    freq = frequencia.keys()
    return freq


palavrasunicas = buscaPalavrasUnicas(frequencia)
# print(palavrasunicas)


def extraiPalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavra in palavrasunicas:
        caracteristicas['%s' % palavra] = palavra in doc
    return caracteristicas


caracteristicasfrase = extraiPalavras(['am', 'nov', 'dia'])
# print(caracteristicasfrase)

def extraiRadicalFrase(frase):
    resultado = []
    stemmer = nltk.RSLPStemmer()
    for p in frase.split():
        resultado.append(str(stemmer.stem(p)))
    return resultado

def avaliaFrase(frase, classificador):
    processado = extraiRadicalFrase(frase)
    novo = extraiPalavras(processado)

    print(classificador.classify(novo))
    distribuicao = classificador.prob_classify(novo)
    for classe in distribuicao.samples():
        print(classe, distribuicao.prob(classe))

def salvaTreinamento(classificador):
    try:
        salva_classificador = open("naivebayes.pickle", "wb")
        pickle.dump(classificador, salva_classificador)
        salva_classificador.close()
        return True
    except:
        return False

def recuperaClassificador():
    classifier_f = open("naivebayes.pickle", "rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()
    return classifier


# função do nltk que aplica as caracteristicas da função passada como parâmetro a uma variável
basecompleta = nltk.classify.apply_features(extraiPalavras, frasesRadical)
# print(basecompleta[15])

# montando a tabela de probabilidade
classificador = nltk.NaiveBayesClassifier.train(basecompleta)
# print(classificador.labels())
# print(classificador.show_most_informative_features(10))

# salvando o treinamento em um arquivo
salvaTreinamento(classificador)

classe = recuperaClassificador()
avaliaFrase("eu amo o dia", classe)