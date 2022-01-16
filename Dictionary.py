
def add_element(Dict):
    word= input("\nEnter a word you want to add : ")
    meaning = input("Enter its meaning : ")
    Dict[word] = meaning
    print("\nUpdated dictionary : ",Dict)

def delete_element(Dict):
    word = input("\nEnter the word you want to delete : ")
    if word in Dict.keys():
        del Dict[word]
        print("\nUpdated dictionary : ",Dict)
    else:
        print("Word not found")

def search_element(Dict):
    search = input("\nEnter the word you want to search from dictionary : ")
    if search in Dict.keys():
        word = Dict.get(search)
        print("Meaning of entered word : ",word)
    else:
        print("word not found")

def sort(Dict):
    print("\nSorted list : ",sorted(Dict))

def search_same(Dict):
    word = input("\nEnter value to be searched : ")
    list = []
    if word in Dict.values():
        for i in Dict.keys():
            if Dict[i]==word:
                list.append(i)
                print (list)
    else:
        print("Word not found")

def display(Dict):
    print("\nDictionary : ",Dict)


Dict = {"annual":"yearly","chief":"head","emotion":"feelings","guarantee":"ensure","big":"huge","leader":"head"}
c=1
while [c==1]:
    n = int(input("\n*****MENU*****\n1.Add new word \n2.Delete a word\n3.Search a word\n4.Display words in alphabetical order \n5.Find word with same meaning\n6.Displaydictionary content\n7.Exit\nEnter the operation you want to perform : \n"))
    if n==1:
        add_element(Dict)
    elif n==2:
        delete_element(Dict)
    elif n==3:
        search_element(Dict)
    elif n==4:
        sort(Dict)
    elif n==5:
        search_same(Dict)
    elif n==6:
        display(Dict)
    elif n==7:
        break
    else :
        print("Invalid choice!!")

"""
Output :

*****MENU*****
1.Add new word
2.Delete a word
3.Search a word
4.Display words in alphabetical order
5.Find word with same meaning
6.Display dictionary content
7.Exit
Enter the operation you want to perform :
1
Enter a word you want to add : kind
Enter its meaning : generous
Updated dictionary : {'annual': 'yearly', 'chief': 'head', 'emotion': 'feelings', 'guarantee':
'ensure', 'big': 'huge', 'leader': 'head', 'kind': 'generous'}

*****MENU*****
1.Add new word
2.Delete a word
3.Search a word
4.Display words in alphabetical order

5.Find word with same meaning
6.Display dictionary content
7.Exit
Enter the operation you want to perform :
2
Enter the word you want to delete : big
Updated dictionary : {'annual': 'yearly', 'chief': 'head', 'emotion': 'feelings', 'guarantee':
'ensure', 'leader': 'head', 'kind': 'generous'}

*****MENU*****
1.Add new word
2.Delete a word
3.Search a word
4.Display words in alphabetical order
5.Find word with same meaning
6.Display dictionary content
7.Exit
Enter the operation you want to perform :
3
Enter the word you want to search from dictionary : gaurantee
word not found

*****MENU*****
1.Add new word
2.Delete a word
3.Search a word
4.Display words in alphabetical order
5.Find word with same meaning
6.Display dictionary content
7.Exit
Enter the operation you want to perform :
3
Enter the word you want to search from dictionary : guarantee
Meaning of entered word : ensure

*****MENU*****

1.Add new word
2.Delete a word
3.Search a word
4.Display words in alphabetical order
5.Find word with same meaning
6.Display dictionary content
7.Exit
Enter the operation you want to perform :
4
Sorted list : ['annual', 'chief', 'emotion', 'guarantee', 'kind', 'leader']
*****MENU*****
1.Add new word
2.Delete a word
3.Search a word
4.Display words in alphabetical order
5.Find word with same meaning
6.Display dictionary content
7.Exit
Enter the operation you want to perform :
5
Enter value to be searched : head
['chief', 'leader']
*****MENU*****
1.Add new word
2.Delete a word
3.Search a word
4.Display words in alphabetical order
5.Find word with same meaning
6.Display dictionary content
7.Exit
Enter the operation you want to perform :
6
Dictionary : {'annual': 'yearly', 'chief': 'head', 'emotion': 'feelings', 'guarantee': 'ensure',
'leader': 'head', 'kind': 'generous'}

*****MENU*****
1.Add new word
2.Delete a word
3.Search a word
4.Display words in alphabetical order
5.Find word with same meaning
6.Display dictionary content
7.Exit
Enter the operation you want to perform :
7

...Program finished with exit code 0
Press ENTER to exit console.

"""