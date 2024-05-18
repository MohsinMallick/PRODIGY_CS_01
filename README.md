Task-01
Implement Caesar Cipher:
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

The Caesar Cipher is one of the oldest and simplest encryption techniques. It involves replacing each letter in a text with another letter a fixed number of positions down the alphabet. For example, with a shift of 1, A becomes B, B becomes C, and so on.

Here's an example of encrypting the message "GOODBYE" with a shift of 4:

1. Start with the plaintext message: GOODBYE.
2. Choose a shift value; in this case, we'll use 4.
3. Substitute each letter in the plaintext with the letter four positions to the right in the alphabet:
   - G becomes K (shifted 4 positions from G)
   - O becomes S (shifted 4 positions from O)
   - O becomes S (shifted 4 positions from O)
   - D becomes H (shifted 4 positions from D)
   - B becomes F (shifted 4 positions from B)
   - Y becomes C (shifted 4 positions from Y)
   - E becomes I (shifted 4 positions from E)
4. The encrypted message is “KSSHFCI”.

To decrypt the message, shift each letter back by the same number of positions. For “KSSHFCI”, shifting each letter back by 4 positions gives you the original message, “GOODBYE”.
