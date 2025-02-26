import random
import os

# Lakers Associate People Quotes 
LA_QU = [
    "Once a Laker, always a Laker - George Mikan",
    "These young guys are playing checkers. I'm out there playing chess. - Kobe Bryant",
    "People just don't understand how obsessed I am with winning - Kobe Bryant",
    "The Lakers have figured out how to win in every era - Jeanie Buss",
    "Any time you win a championship with a team, it's really special coming back and doing it in L.A. with the Lakers - Alex Caruso",
    "I mean, the Lakers are pretty damn Hollywood - Jerry Buss",
    "The only person who can really motivate you is you - Shaquille O'Neal",
    "In life, winning and losing will both happen. What is never acceptable is quitting - Magic Johnson",
    "You can't win unless you learn how to lose - Kareem Abdul-Jabbar",
    "Heros come and go, but legends are forever - Kobe Bryant"
]

def LA_NUM(): # uses as keys for various encryption steps
    return [8, 2, 4, 2, 3] # Laker player numbers that were important: Kobe 8,24 and Lebron 23

def buzzerBeatercheck(txt): # creates a two num checksum based on text 
    total = 0
    for char in txt:
        total = (total + (ord(char) % 24)) % 24
    return str(total).zfill(2)

def dribbling(txt, jerseyNum, enc=True): # applies a shfiting encryption based on jerseyNum list
    shift_txt = ""
    for i, char in enumerate(txt):
        num_val = jerseyNum[i % len(jerseyNum)]
        if not enc:
            num_val = -num_val # will reverse the shift for decryption
        shift_txt += chr(ord(char) + num_val)
    return shift_txt

def passing(txt, enc=True): # letter sub encryption on text 
    vowels = "AEIOUaeiou" # vowel shifting
    consMapEnc = str.maketrans("FLCPGflcpg", "CPGFLcpgfl")
    consMapDec = str.maketrans("CPGFLcpgfl", "FLCPGflcpg") # Will do reverse mapping
    
    if enc:
        txt = txt.translate(consMapEnc)
        txt = ''.join(vowels[(vowels.index(c) + 1) % len(vowels)] if c in vowels else c for c in txt) # first translate consonant then shifts vowels
    else:
        txt = ''.join(vowels[(vowels.index(c) - 1) % len(vowels)] if c in vowels else c for c in txt) # will reverse steps above
        txt = txt.translate(consMapDec) 
    
    return txt

def fastbreak(txt, jerseyNum, enc=True): # two chunks determined by jerseyNum lis
    chunks = [] 
    jerseyIndex = 0
    start = 0
    while start < len(txt): # Will reverse each chunk for encryption and decryption
        curChunkSize = jerseyNum[jerseyIndex % len(jerseyNum)]
        end = min(start + curChunkSize, len(txt)) # will reverse chunk and print list
        chunks.append(txt[start:end][::-1])
        start += curChunkSize
        jerseyIndex += 1
    return ''.join(chunks)

def lakerEnc(input, output): # encrypts file that is inputted
    if not os.path.exists(input):
        print("ERROR: NOT A VALID FILE")
        return                      

    with open(input, 'r', encoding='utf-8') as f:
        plaintxt = f.read().rstrip('\n')
        
    jerseyNum = LA_NUM() 
    step1 = dribbling(plaintxt, jerseyNum, enc=True) # shift base on jerseyNum
    step2 = passing(step1, enc=True) # Sub letter passing
    ciptxt = fastbreak(step2, jerseyNum, enc=True) # reverse chunk text based on jerseyNum
    checkSum = buzzerBeatercheck(ciptxt) # creates text
    
    encData = ciptxt + checkSum
    quote = random.choice(LA_QU)
    
    with open(output, 'wb') as f:
        f.write(f"{quote}\n###ENCRYPTED###\n{encData}".encode('utf-8'))
    
    print("ENCRYPTION SUCCESSFUL,", output, "created") # gives encrypted file
    print("NEW MESSAGE:", quote) # gives quote

def laker_Dec(input, output): # decrypts file that was encrypted
    if not os.path.exists(input):
        print("ERROR NOT VALID FILE")
        return
    
    with open(input, 'rb') as f:
        content = f.read().decode('utf-8')
    
    parts = content.split("###ENCRYPTED###\n", 1) # separatees header from encrypted data
    if len(parts) < 2:
        print("ERROR NOT ENOUGH LINES")
        return
    
    encData = parts[1].rstrip('\n')
    
    if len(encData) < 2:
        print("ERROR NOT ENCRYPTED DATA")
        return
    
    checkSum = encData[-2:] 
    ciptxt = encData[:-2]
    calCheckSum = buzzerBeatercheck(ciptxt) # recalculates checkSum with encrypted data
    
    if calCheckSum == checkSum: # make sure checkSum match to decrypt data
        jerseyNum = LA_NUM()
        step1 = fastbreak(ciptxt, jerseyNum, enc=False) # reverse fastbreak(chunk reverse)
        step2 = passing(step1, enc=False) # reverse passing(sub)
        plaintxt = dribbling(step2, jerseyNum, enc=False) # reverse dribbling(shift)

        with open(output, 'wb') as f:
            f.write(plaintxt.encode('utf-8')) 
        print("DECRYPTION SUCCESSFUL, OUTPUT TO:", output, "created") # gives decrypt data 

    else:
        print("Decryption FAILED")

def main(): # simple main that allows for encrypt, decrypt, and exciting 
    while True:
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        
        choice = input("Pick 1-3: ")
        if choice == "1":
            inputName = input("Enter input file: ")
            outputName = input("Enter output file: ")
            lakerEnc(inputName, outputName)
        elif choice == "2":
            inputName = input("Enter input file: ")
            outputName = input("Enter output file: ")
            laker_Dec(inputName, outputName)
        elif choice == "3":
            break
        else:
            print("BEE FRRRR NOT A VALID CHOICE")

if __name__ == "__main__":
    main()