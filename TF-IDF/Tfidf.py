from Preprocessing.LoadData import TextLoader
from Preprocessing.DataCleaning import regex_tokenization
from sklearn.feature_extraction.text import TfidfVectorizer


if __name__ == '__main__':
    loader = TextLoader()
    loader.load_articles_and_summaries('../Dataset/BBC News Summary/News Articles/business',
                                       '../Dataset/BBC News Summary/Summaries/business')
    keys = list(loader.articles.keys())
    tfidf = TfidfVectorizer(tokenizer=regex_tokenization)
    X = tfidf.fit_transform(loader.articles.values())
    # getting the words with highers tf-idf values for each document
    idxs = X[0].toarray().argsort()[0][-100:]
    print(tfidf.get_feature_names_out()[idxs])
