import os


class TextLoader:
    def __init__(self, encoding: str = 'utf-8'):
        self.encoding = encoding
        self.articles = {}
        self.summaries = {}

    def load_data(self, path: str) -> dict:
        """
        Read all files from the path and return a dict such that the key is the filename and the value is the content.
        :return: dict
        """
        text_dict = {}
        for filename in os.listdir(path):
            with open(os.path.join(path, filename), 'r', encoding=self.encoding) as f:
                content = f.read()
                text_dict[filename] = content

        return text_dict

    def load_articles_and_summaries(self, articles_path: str, summaries_path: str):
        """
        Load articles and summaries from the given path.
        :return: None
        """
        self.articles = self.load_data(articles_path)
        self.summaries = self.load_data(summaries_path)


if __name__ == '__main__':
    loader = TextLoader()
    loader.load_articles_and_summaries('../Dataset/BBC News Summary/News Articles/business',
                                       '../Dataset/BBC News Summary/Summaries/business')
    keys = list(loader.articles.keys())
    print(loader.summaries[keys[0]])