import random


def getQuote(fileName):
    f = open(fileName, "r")

    quotes = f.read().split("-")

    quote = random.choice(quotes)
    f.close()
    return quote

if __name__ == "__main__":
    quoteFile = "quotes.txt"

    print(getQuote(quoteFile))