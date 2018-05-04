from flask import Flask, render_template, request
import pymorphy2

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/getWords')
def getWords():
    a = request.args.get('a')

    s = "["
    i = 0
    wordArray = []
    morph = pymorphy2.MorphAnalyzer()
    allWords = a.split()

    for word in allWords:
        words = morph.parse(word)
        for x in words:
            for z in x.lexeme:
                if not(z.word in wordArray):
                    wordArray.append(z.word)
                    s = s + ('{"%s":"%s"}, \n\r' %(i, z.word))
                    i = i + 1
    s = s[0:-4] + "]"
    return (s)

if __name__ == "__main__":
    app.run()
