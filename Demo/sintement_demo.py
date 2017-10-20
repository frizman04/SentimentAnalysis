from sentiment_classifier import SentimentClassifier

from flask import Flask, render_template, request,  redirect, url_for

app = Flask(__name__)


print("Preparing classifier")
classifier = SentimentClassifier()
print("Classifier is ready")



@app.route('/',methods=['GET','POST'])
def index(text="",clf_response=None):
    print('start')

    if request.method == "POST":
        text = request.form["text"]

        if (text != None and text != '') :
            clf_response = classifier.predict(text)
        else :
            clf_response = None

    print(text)
    return render_template('index.html',text = text, clasifer_response=clf_response)


# @app.route('/rundemo')
# def rundemo() :
#     random_text = 'Прекрасная задняя панель'
#
#     return redirect(url_for('index', text=random_text))
#

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)