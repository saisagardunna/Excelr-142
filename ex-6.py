import nltk
import spacy
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    tokens
