from model import eng, Directors, Movies
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, between, or_

Session = sessionmaker(bind=eng)
session = Session()

# Lists to Commit to DB
directors = [{'name': 'Frank', 'surname': 'Darabont', 'rating': 7}, {'name': 'Francis Ford', 'surname': 'Coppola', 'rating': 8}, {'name': 'Quentin', 'surname': 'Tarantino', 'rating': 10}, {'name': 'Christopher', 'surname': 'Nolan', 'rating': 9}, {'name': 'David', 'surname': 'Fincher', 'rating': 7}]
movies = [{'title': 'The Shawshank Redemption', 'year': 1994, 'category': 'Drama', 'director_id': 1, 'rating': 8}, {'title': 'The Green Mile', 'year': 1999, 'category': 'Drama', 'director_id': 1, 'rating': 6}, {'title': 'The Godfather', 'year': 1972, 'category': 'Crime', 'director_id': 2, 'rating': 7}, {'title': 'The Godfather III', 'year': 1990, 'category': 'Crime', 'director_id': 2, 'rating': 6}, {'title': 'Pulp Fiction', 'year': 1994, 'category': 'Crime', 'director_id': 3, 'rating': 9}, {'title': 'Inglourious Basterds', 'year': 2009, 'category': 'War', 'director_id': 3, 'rating': 8}, {'title': 'The Dark Knight', 'year': 2008, 'category': 'Action', 'director_id': 4, 'rating': 9}, {'title': 'Interstellar', 'year': 2014, 'category': 'Sci-fi', 'director_id': 4, 'rating': 8}, {'title': 'The Prestige', 'year': 2006, 'category': 'Drama', 'director_id': 4, 'rating': 10}, {'title': 'Fight Club', 'year': 1999, 'category': 'Drama', 'director_id': 5, 'rating': 7}, {'title': 'Zodiac', 'year': 2007, 'category': 'Crime', 'director_id': 5, 'rating': 5}, {'title': 'Seven', 'year': 1995, 'category': 'Drama', 'director_id': 5, 'rating': 8}, {'title': 'Alien 3', 'year': 1992, 'category': 'Horror', 'director_id': 5, 'rating': 5}]

# Commit all the Directors to the DB
session.add_all((Directors(**director) for director in directors))
session.commit()
# Commit all the Movies to the DB
session.add_all((Movies(**movie) for movie in movies))
session.commit()

# List all movies for the Drama category
result = session.query(Movies).filter(Movies.category == 'Drama').all()
print(result)

# List the titles of movies from the Crime category that were made after 1994
result2 = session.query(Movies.title).filter(and_(
            Movies.category == 'Crime', Movies.year > 1994)).all()
print(result2)

# List the categories of all movies and their rankings, for the films that were produced between
# 2000 and 2010 and had rankings greater than 7, also, sort them by their ranking
result3 = session.query(Movies.category, Movies.rating).filter(
            and_(Movies.rating > 7, between(Movies.year, 2000, 2010))).order_by(
                Movies.rating.desc()).all()
print(result3)
# List the names of all directors whose ranking is greater than or equal
# to 6 and whose first name starts with 'D' or ends with 'n'.
result4 = session.query(Directors.surname).filter(and_(
            Directors.rating >= 6, or_(
                Directors.name.like('D%'), Directors.name.like('%n')))).all()
print(result4)
