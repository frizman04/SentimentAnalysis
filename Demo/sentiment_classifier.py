import pickle



class SentimentClassifier(object) :

    def __init__(self):

        with open('sentiment_clf.pkl', 'rb') as f:
            self.clf = pickle.load(f)

    def predict(self,text) -> int :
        try :
            return self.clf.predict([text])
        except :
            return -1
