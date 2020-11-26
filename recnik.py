dictionary = {
    "1": "Star Wars",
    "2": "Avengers",
    "3": "Joker",
}


def meny():
    print("***************Meny***************")
    print("1: Insert new element in dictionary")
    print("2: Write all elements in dictionary.")
    print("3: Edit existing element in dictionary.")
    print("4: Delete existing element in dictionary.")
    print("5: End.")
    print("**********************************")


def insetr(film=None):
    key = input("Enter a new key ")
    film = input("Enter a new element")
    dictionary.update({key: film})


def write():
    print(dictionary)


def delete():
    while True:
        d = input("Insetr a key of element that you want to delete: ")
        if d in dictionary.keys():
            del dictionary[d]
            break
        else:
            print("The key you inserted does not exist!")


def edit():
    while True:
        a = input("Enter a key of the film you would like to edit: ")
        if a in dictionary.keys():
            film = input("Enter a new tittle: ")
            dictionary[a] = film
            break
        else:
            print("The key you inserted does not exist!")


while True:
    meny()
    c = input("Choose one: ")
    if c == "1":
        instet()
    elif c == "2":
        i = write()
    elif c == "3":
        edit()
    elif c == "4":
        delete()
    elif c == "5":
        break
