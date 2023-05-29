from flask import Blueprint,render_template,request
from flask_login import login_required,current_user
from . import ciphers
import numpy as np
from flask import jsonify


views=Blueprint('views',__name__)

@views.route("/")
@login_required
def home():
    return render_template("home.html",user=current_user)

@views.route("/learn")
@login_required
def learn():   
    return render_template("learn.html",user=current_user)

@views.route("/lab",methods=["POST","GET"])
@login_required
def lab():
   return render_template("lab.html",user=current_user)

@views.route("/puzzles",methods=["POST","GET"])
@login_required
def puzzles():
     return render_template("puzzles.html",user=current_user)


@views.route('/encrypt', methods=['POST'])

def encrypt():
    selected_cipher = request.json['selectedCipher']
    shift = request.json['shift']
    message = request.json['message']
    # keyword = request.json['shift']  # Add this line to get the keyword
    # matrix = request.json['shift']  # Add this line to get the matrix

    encrypted_message = ''

    if selected_cipher == 'Caesar Cipher':
        encrypted_message = ciphers.caesar_encrypt_python(message, int(shift))
    elif selected_cipher == 'Atbash Cipher':
        encrypted_message = ciphers.atbash_encrypt_python(message)
    elif selected_cipher == 'Vigenère Cipher':
        encrypted_message = ciphers.vigenere_encrypt_python(message, shift)
    elif selected_cipher == 'Playfair Cipher':
        encrypted_message = ciphers.playfair_encrypt_python(message, shift)


    return jsonify({'encryptedMessage': encrypted_message})


@views.route('/decrypt', methods=['POST'])
def decrypt():
    selected_cipher = request.json['selectedCipher']
    shift = request.json['shift']
    message = request.json['message']

    decrypted_message = ''

    if selected_cipher == 'Caesar Cipher':
        decrypted_message = ciphers.caesar_decrypt_python(message, int(shift))
    elif selected_cipher == 'Atbash Cipher':
        decrypted_message = ciphers.atbash_decrypt_python(message)
    elif selected_cipher == 'Vigenère Cipher':
        decrypted_message = ciphers.vigenere_decrypt_python(message, shift)
    elif selected_cipher == 'Playfair Cipher':
        decrypted_message = ciphers.playfair_decrypt_python(message, shift)

    return jsonify({'decryptedMessage': decrypted_message})


@views.route('/decryptCaesar', methods=['POST'])
def decrypt_caesar():
    ciphertext = request.json['ciphertext']

    decrypted_message = ciphers.caesar_decrypt(ciphertext)

    return jsonify({'decryptedMessage': decrypted_message})


@views.route('/atbash',methods=["POST","GET"])
@login_required
def atbash():
    return render_template("atbash.html",user=current_user)


@views.route('/atbash/encrypt', methods=['POST'])
def atbash_encrypt():
    data = request.get_json()
    text = data['text']
    encrypted_text = ciphers.atbash_encrypt_python(text)
    return jsonify({'encryptedText': encrypted_text})

@views.route('/atbash/decrypt', methods=['POST'])
def atbash_decrypt():
    data = request.get_json()
    text = data['text']
    decrypted_text = ciphers.atbash_decrypt_python(text)
    return jsonify({'decryptedText': decrypted_text})

@views.route('/hill',methods=["POST","GET"])
@login_required
def hill():
    return render_template("hill.html",user=current_user)

@views.route('/hill/encrypt', methods=['POST'])
def hill_encrypt_route():
    data = request.get_json()
    plaintext = data['plaintext']
    key = np.array(data['key'])
    encrypted_text = ciphers.hill_encrypt(plaintext, key)
    return jsonify({'encryptedText': encrypted_text})

@views.route('/hill/decrypt', methods=['POST'])
def hill_decrypt_route():
    data = request.get_json()
    ciphertext = data['ciphertext']
    key = np.array(data['key'])
    decrypted_text = ciphers.hill_decrypt(ciphertext, key)
    return jsonify({'decryptedText': decrypted_text})
