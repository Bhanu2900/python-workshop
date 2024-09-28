from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
Analyzer = SentimentIntensityAnalyzer()


def analyzer(text):
    try:
        sentiment = Analyzer.polarity_sources(text)

        if sentiment["cimpound"] >=0.05:
            print("positive")
        elif sentiment["compound"] <=-0.05:
            print("negative")
        else:
            print("neutral")
        print(sentiment)
    except exception as e:
        print(e)


Text = input("please enter a text: ")
analyze(Text)