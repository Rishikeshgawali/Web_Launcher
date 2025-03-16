from sys import *
import webbrowser
import re
import urllib.request

def is_connected():
    try:
        urllib.request.urlopen("https://www.google.co.in",timeout = 1)
        return True
    except urllib.request.URLError as err:
        return False

def Find(string):
    url = re.findall('^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$',string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            url = Find(line)                    #url = ['https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'] ...it is in []
            print(url)
            for str in url :
                webbrowser.open(str,new = 2)

def main():
    print("----Program by Rishikesh Gawali----")
    print("Applicatio name is : "+argv[0])

    if(len(argv) !=2):
        print("Error : Invalid Number of Argument")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used to open URL which are writte in one file.")
        exit()

    if ((argv[1] == "-u") or (argv[1] == "-U")):
        print("usage : ApplicationName Name_Of_File")
        exit()

    try:
        connected = is_connected()

        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable to connect to Internet...")

    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input ",E)

if __name__ == "__main__":
    main()
