from textblob import TextBlob #sentiment analysis
from colorama import Fore, Style,init #colored terminal
#initiliaze coloroma
init(autoreset=True)
#function-analyze the sentiment
def analyze_sentiment(text):
    #initiliaze textblob
    blob=TextBlob(text)
    #get the polarity
    polarity=blob.sentiment.polarity
    if polarity>0:
    #positive sentiment
        return "positive",polarity
    elif polarity<0:
    #-ve sentiment
        return "negative",polarity
    else:
        return "Neutral",polarity
#main function-run the program
def main():
    print(Fore.GREEN+"😊Welcome to the Sentiment Analyzer.")
    print(Fore.YELLOW+"Type 'exit' to close the program")
    while True:
        message=input(Fore.CYAN+"Your text:")
        if message.lower()=='exit':
            print(Fore.RED+"Exiting......")
            break
        sentiment,score=analyze_sentiment(message)
        if sentiment=="positive":
            print(Fore.LIGHTGREEN_EX+"You are happy")
        elif sentiment=="negative":
            print(Fore.RED+"You are sad")
        else:
            print(Fore.YELLOW+"Neutral Sentiment")
#run the main function
main()