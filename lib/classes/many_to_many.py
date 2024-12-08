class Article:
    all = []
    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("author must be an instance of Author")
        
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError("magazine must be an instace of Magazine")    

        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string and 5-50 characters.")

        Article.all.append(self)
        self._author._articles.append(self)
        self._magazine._articles.append(self)    

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed")
        
        if isinstance(value,str) and 5 <= len(value) <=50:
            self._title = value
        else:
            raise ValueError("Title must be a string and 5-50 characters")

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
   
       if isinstance(value, Author):
            self._author = value
       else:
            raise TypeError("author must be an instance of Author")        
       
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
    
                    
       if isinstance(value, Magazine):
            self._magazine = value
       else:
            raise TypeError("magazine must be an instance of Magazine")               

        
    
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0 :
            self._name = name
            self._articles = []
        else:
            raise ValueError("Name must be a String")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):

        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed")
        
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a string")    

    
    def articles(self):
        return list(set(self._articles))
    

    def magazines(self):
        unique_magazines = list(set(article.magazine for article in self._articles))
        return unique_magazines
    
    def add_article(self, magazine, title):
        latest_article = Article(self, magazine, title)
        self._articles.append(latest_article)
        return latest_article

    def topic_areas(self):
        if not self._articles:
            return None
        topics =[]
        for article in self._articles:
            topics.append(article.magazine.category)
        return list(set(topics))        

class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str) and  2 <= len(name) <= 16:
            self._name = name
            self._articles = []
        else:
            raise ValueError("Name must be a String")
            
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a string")
         
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(value, '_name'):
            raise AttributeError("Name cannot be changed")        
        if isinstance(value, str) and  2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a String")        

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if hasattr(value, '_category'):
            raise AttributeError("Category cannot be changed")               
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a string")        

    def articles(self):
        return self._articles

    def contributors(self):
        unique_contributors = list(set(article.author for article in self._articles))
        return unique_contributors       

    def article_titles(self):
        if not self._articles:
            return None
        titles =[]
        for article in self._articles:
            titles.append(article.title)
        return titles    

    def contributing_authors(self):
        pass


# creating Authors 
author1 = Author("David Parsley")
author2 = Author("Joy Mwende")

# creating Magazines 
magazine1 = Magazine("National Geo", "Nature")
magazine2 = Magazine("Rolling Stone", "Music")

# adding articles to authors and link them to magazines
article1 = author1.add_article(magazine1, "The African Savannah")
article2 = author2.add_article(magazine2, "Hottest Realeases of the Week")


# check articles of David & Joy
print(f"Articles by {author1.name}:")
for article in author1.articles():
    print(f"{article.title}\nMagazine: {article.magazine.name}\n")

print(f"Articles by {author2.name}:")
for article in author2.articles():
    print(f"{article.title}\nMagazine: {article.magazine.name}")    

# check articles of magazine 1 & 2
print(f"\nArticles in {magazine1.name}:")
for article in magazine1.articles():
    print(f"{article.title}\nAuthor: {article.author.name}\n")

print(f"\nArticles in {magazine2.name}:")
for article in magazine2.articles():
    print(f"{article.title}\nAuthor: {article.author.name}\n")

# Get unique topics of author 1 & 2
print(f"\nUnique topic areas for {author1.name}: {author1.topic_areas()}")

print(f"\nUnique topic areas for {author2.name}: {author2.topic_areas()}")


# Get the contributors of magazine 1 & 2
print(f"\nContributors to {magazine1.name}:")
for contributor in magazine1.contributors():
    print(f"{contributor.name}")

print(f"\nContributors to {magazine2.name}:")
for contributor in magazine2.contributors():
    print(f"{contributor.name}")


# Get the article titles in magazine 1 & 2
print(f"\nArticle titles in {magazine1.name}:")
for title in magazine1.article_titles():
    print(f"{title}")

print(f"\nArticle titles in {magazine2.name}:")
for title in magazine2.article_titles():
    print(f"{title}")