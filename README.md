# CipherSculptor
Artful Encryption with the Caesar Cipher

CipherSculptor is a Python-based encryption and decryption tool utilizing the classic Caesar Cipher technique. 
This repository showcases an artful implementation that allows users to effortlessly encrypt and decrypt text with a customizable shift value.
Unleash the power of historical cryptography in a user-friendly manner, ideal for educational exploration and understanding the foundations of substitution ciphers.
Dive into the world of CipherSculptor and sculpt your messages with a touch of encryption artistry.

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down or up the alphabet. Here's how the Caesar Cipher encryption and decryption tool in the provided Python script works:

1. **User Input:**
   - The user is prompted to enter the text they want to encrypt or decrypt.

2. **Shift Value Input:**
   - The user is prompted to enter the shift value, which determines how much each letter in the text will be shifted during encryption or decryption.

3. **Encryption:**
   - The `encrypt` function takes the user-provided text and shift value.
   - For each letter in the text (ignoring non-alphabetic characters), the function shifts the letter to the right in the alphabet by the specified shift value.
   - The encrypted text is formed, maintaining the positions of non-alphabetic characters.

4. **Decryption:**
   - The `decrypt` function takes the encrypted text and the same shift value.
   - It reverses the process, shifting each letter in the encrypted text back to the left in the alphabet by the specified shift value.
   - The decrypted text is formed, preserving the positions of non-alphabetic characters.

5. **Output:**
   - The script then outputs both the encrypted and decrypted texts.

Here's a simple example:
![image](https://github.com/tamzzay/CipherSculptor/assets/130298353/9cb5a0f6-a333-4b33-acc6-fc3e5fa06748)


In this example, with a shift value of 3, each letter in the plaintext is shifted three positions 
to the right in the alphabet during encryption and back to the left during decryption. 
Non-alphabetic characters, such as commas and spaces, remain unchanged. 
The result is an encrypted and decrypted version of the original text.
