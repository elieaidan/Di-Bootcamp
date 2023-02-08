magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for i in magician_names:
       print(i)
     

show_magicians()

def make_great():
    global magician_names
    for i in magician_names:
        magician_names = 'The Great' + ' ' + i
        print(magician_names)
    

make_great()


    

 





