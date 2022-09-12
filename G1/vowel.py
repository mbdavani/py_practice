def main():
    word = str(input("What word would you like to analyze? "))

    x = len(word[:])
    vowels = ["a", "e", "i", "o", "u"]
    y=0

    for i in range(x):
         if (any(item in vowels for item in word)) == True:
            y+=1
    
    print("The amount of vowels in your entry is= ", end="\n")
    print(y)
          
    
main()
