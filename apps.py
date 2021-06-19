#playsound and save the conversion into txt file format and audio

from playsound import playsound
import time
import pyttsx3 as pyttsx
from pydub import AudioSegment

sound1 = AudioSegment.from_file("dah.wav", format="wav")
sound2 = AudioSegment.from_file("dit.wav", format="wav")

combine = AudioSegment.empty()

def morse(text):
    code = {' ': '|', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}

    morse_code = ""

    for x in text:
        morse_code += code[x.upper()]

    return morse_code

text = input ("Masukan teks yang ingin di koversikan: ")
print(morse(text))

#playsound
for m in morse(text):
	if m=='.':
		playsound('dit.wav')
		combine += sound1
	elif m=='-':
		playsound('dah.wav')
		combine += sound2
	else:
		time.sleep(0.5)

#input the convertion into txt file format
with open('outputfile.txt', 'w') as outfile:
    outfile.write(morse(text))

#convert sound into mp3 file format (percobaan)
#export playsound into .mp3 file format
file_handle = combine.export("output.mp3", format="wav")