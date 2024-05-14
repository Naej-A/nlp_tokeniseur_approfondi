import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Assurez-vous de télécharger les ressources nécessaires
nltk.download('punkt')

# Texte en entrée
text = "Bonjour! J'apprends le NLP. C'est très intéressant."

# Tokenisation par phrases
sentences = sent_tokenize(text, language='french')

# Tokenisation par mots dans chaque phrase
words_in_sentences = [word_tokenize(sentence, language='french') for sentence in sentences]

# Affichage des résultats
for i, sentence in enumerate(sentences):
    print(f"Phrase {i+1}: {sentence}")
    print(f"Mots: {words_in_sentences[i]}")
