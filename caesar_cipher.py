alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryption(text, o):
  rotation = ""
  # searching letter number in text
  for letter_number in text:
    # reply the letter number if something wrong
    if (alphabet.find(letter_number) == -1):
      rotation += letter_number
      #schifre
    else:
      rotation += (alphabet[(alphabet.find(letter_number) + o) % len(a)])
  return rotation

def decryption(t, o):
  rotation = ""
  for letter_number in t:
    if (alphabet.find(letter_number) == -1):
      rotation += letter_number
      #
    else:
      rotation += (alphabet[(alphabet.find(letter_number) - o) % len(a)])
  return rotation

word = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(word))
#
if mode == 1:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encryption(text, rotation))
  #
elif mode == 2:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decryption(text, rotation))
  #
elif mode == 3:
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\\_(ツ)_/¯")
