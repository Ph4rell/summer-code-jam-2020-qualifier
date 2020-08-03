"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import collections
import re
import itertools


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""
    id = itertools.count()
    last_edited = None
    

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str, last_edited = None):
      self.id = next(Article.id)
      self.title = title
      self.author = author
      self.publication_date = publication_date
      self.content = content
      self.last_edited = last_edited

    @property
    def content(self):
      return self._content

    @content.setter 
    def content(self, value):
      self.last_edited = datetime.datetime.now()
      self._content = value

    def __lt__(self, other):
      return self.publication_date < other.publication_date
  
    def __repr__(self):
      return f"<Article title=\"{self.title}\" author='{self.author}' publication_date='{self.publication_date.isoformat()}'>"

    def __len__(self):
      return len(self.content)

    def short_introduction(self, n_characters:int):
      count = 0
      result = ''
      partial_list = list()
      for i, element in enumerate(self.content.replace('\n', ' ')):
        for char in element:
          if count < n_characters:
            count+=1
            partial_list.append(char)
          else:
            break
      total_list = self.content.replace('\n', ' ').split(' ')
      partial_list = "".join(partial_list).split(' ')
      final_list = [i for i, j in zip(total_list, partial_list) if i == j]
      return " ".join(final_list)

      
    def most_common_words(self, n_words:int):
      total_list = re.split("[\W']",self.content.lower())
      new_list = list()
      for i in total_list:
        if i:
          new_list.append(i)
      counter = collections.Counter(new_list).most_common(n_words)
      return dict(counter)

        
