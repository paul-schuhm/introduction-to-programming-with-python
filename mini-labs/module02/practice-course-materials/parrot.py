# A parrot (and silly?) program that repeat everything you type
# You can exit this program by typing different keywords

while(True):
    answer = input("")
    if(answer == "stop" or answer == "quit" or answer == "exit"):
        break;
    print(answer)
