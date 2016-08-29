import pickle
import pyLDAvis
data = pickle.load(open("Pickles/LDAvis.data", "rb"))
pyLDAvis.show(data, ip = '0.0.0.0', use_http = True)
