alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
directions=input("Type 'encode' to encrypt, type decode to 'decrypt' \n")
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))
shift=shift%26
should_resume=True
while should_resume:
    def caesar(text_value,shift_amount,direction):
        Result=""
        if direction=="decode":
            shift_amount*=-1
        for char in text_value:
            if char in alphabets:
                position=alphabets.index(char)
                new_position=position+shift_amount
                caesar_text=alphabets[new_position]
                Result+=caesar_text
            else:
                Result+=text_value
        print(f"The {direction}d value is {Result}")
    caesar(text_value=text,shift_amount=shift,direction=directions)
    restart=input("Type yes to restart, or 'no to end : ")
    if restart=='no':
        should_resume=False
        print("Goodbye")
        




