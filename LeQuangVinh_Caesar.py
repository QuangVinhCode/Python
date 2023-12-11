def encrypt(key,message):
    message=message.upper()
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""
    for letter in message:
        if letter in alpha:
            letter_index=(alpha.find(letter)+key)%len(alpha)
            result=result+alpha[letter_index]
        else:
            result=result+letter
    return result
def decrypt(key,message):
    message =message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result

def main():
    flag = True;
    while flag:
        key = input("nhap k:")
        key = int(key)
        message = input("nhap thong diep:")
        print("------------------------")
        print("1.Encryption")
        print("2.Decryption")
        mode = input("Vui long chon mode:")
        mode = mode.upper();
        match( mode ):
            case "1":
                print(encrypt(key, message))
            case "2":
                print(decrypt(key, message))
        print("ban co muon tiep tuc (y/n):")
        choice = input()
        if choice == "n":
            flag = False;

if __name__=='__main__':
    main()