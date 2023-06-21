from flask import Flask, render_template, request, redirect
import Cryptibrary as my

app = Flask(__name__,template_folder = "templates")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cipher = request.form['cipher']
        if cipher == 'encrypt':
            return redirect("/encrypt")
        else:
            return redirect("/decrypt")
    else:
        return render_template('EnORDe.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt_case():
    if request.method == 'POST':
        cipher = request.form['cipher']
        if cipher == 'caesar':
            return redirect("/encrypt/ceasar")
        elif cipher == 'substitution':
            return redirect("/encrypt/substitution")
        elif cipher == 'vigenere':
            return redirect('/encrypt/vigenere')
    else:
        return render_template('index.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt_case():
    if request.method == 'POST':
        cipher = request.form['cipher']
        if cipher == 'caesar':
            return redirect("/decrypt/ceasar")
        elif cipher == 'substitution':
            return redirect("/decrypt/substitution")
        elif cipher == 'vigenere':
            return redirect('/decrypt/vigenere')
    else:
        return render_template('index.html')

#                       CRIPTAZIONE
@app.route('/encrypt/ceasar', methods=['GET', 'POST'])
def enCeasar():
    if request.method == 'POST':
        words = request.form['words']
        key = int(request.form['shift'])
        encrypted_words = my.caesar_encrypt(words, key)
        return render_template("ceasar_encrypt.html",encrypted_words=encrypted_words)
    else:
        return render_template("ceasar_encrypt.html")

@app.route('/encrypt/substitution', methods=['GET','POST'])
def enSubstitution():
    if request.method == 'POST':
        words = request.form['words']
        key = request.form['key']
        key = my.remove(key)
        key = my.alphabet_complete(key)
        encrypted_words = my.substitution_encrypt(words, key)
        return render_template("substitution_encrypt.html",encrypted_words=encrypted_words)
    else:
        return render_template("substitution_encrypt.html")

@app.route('/encrypt/vigenere', methods=['GET', 'POST'])
def enVigenere():
    if request.method == 'POST':
        words = request.form['words']
        key = request.form['key']
        encrypted_words = my.vigenere_encrypt(words,key)
        return render_template("vigenere_encrypt.html",encrypted_words=encrypted_words)
    else:
        encrypted_words=""
        return render_template("vigenere_encrypt.html")

    

#                       DECRIPTAZIONE

@app.route('/decrypt/ceasar', methods=['GET', 'POST'])
def deCeasar():
    if request.method == 'POST':
        words = request.form['words']
        key = int(request.form['shift'])
        encrypted_words = my.ceasar_decrypt(words, key)    
        return render_template("ceasar_decrypt.html",encrypted_words=encrypted_words)
    else:
        return render_template("ceasar_decrypt.html")

@app.route('/decrypt/substitution', methods=['GET', 'POST'])
def deSubstitution():
    if request.method == 'POST':
        words = request.form['words']
        key = request.form['key']
        key = my.remove(key)
        key = my.alphabet_complete(key)
        encrypted_words = my.substitution_decrypt(words, key)
        return render_template("substitution_decrypt.html",encrypted_words=encrypted_words)
    else:
        return render_template("substitution_decrypt.html")

@app.route('/decrypt/vigenere', methods=['GET', 'POST'])
def deVigenere():
    if request.method == 'POST':
        words = request.form['words']
        key = request.form['key']
        encrypted_words = my.vigenere_decrypt(words,key)
        return render_template("vigenere_decrypt.html",encrypted_words=encrypted_words)
    else:
        encrypted_words=""
        return render_template("vigenere_decrypt.html")

if __name__ == '__main__':
    app.run(debug=True)
