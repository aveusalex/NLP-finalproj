import re


def unique_chars(text: str) -> list:
    """
    Return a set of unique chars in the text.
    :param text: str
    :return: list
    """

    return list(set(text))


def whitespace_tokenization(text: str) -> list:
    """
    Split the text into tokens considering whitespaces.
    :param text: str
    :return: list
    """
    return text.split()


def regex_tokenization(text: str) -> list:
    """
    Remove punctuation from the text using regex.
    :param text: str
    :return: list
    """
    return re.split('\W+', text)


if __name__ == '__main__':
    from LoadData import TextLoader

    loader = TextLoader()
    loader.load_articles_and_summaries('../Dataset/BBC News Summary/News Articles/business',
                                       '../Dataset/BBC News Summary/Summaries/business')
    keys = list(loader.articles.keys())
    print(whitespace_tokenization(loader.articles[keys[0]]))
    print(regex_tokenization(loader.articles[keys[0]]))
    # print(unique_chars(loader.articles[keys[0]]))
