def word_count(text):
    words = text.split()
    count = len(words)
    return count

def main():
    print("welcome to the word counter tool!!")
    text = input("Enter the text: ")
    count = word_count(text)
    print("The number od words is: ", count)

main()