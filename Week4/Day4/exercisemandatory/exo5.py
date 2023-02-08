# def make_shirt(size, text):
#     sentence = f'The size of the shirt is {size} and the text is {text}'
#     return sentence

# a = make_shirt('S', ' je taime')

# print(a)

def make_shirt(size = 'large', text = 'I love Python'):
    sentence = f'The size of the shirt is {size} and the text is {text}'
    return sentence


a = make_shirt()

print(a)

b = make_shirt(text= 'Je suis un developper' )
print(b)

c = make_shirt(size= 'medium', text= 'I am a developper')
print(c)

d = make_shirt(size= 'any size', text= 'I am a developper')

