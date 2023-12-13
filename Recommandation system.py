books_data = [
    {'Title': 'Wings of Fire', 'Category': 'Biography', 'Rating': 4.8},
    {'Title': 'Wise and Otherwise', 'Category': 'Biography', 'Rating': 4.7},
    {'Title': 'The Alchemist', 'Category': 'Fiction', 'Rating': 4.7},
    {'Title': 'The Kite Runner', 'Category': 'Fiction', 'Rating': 4.8},
    {'Title': 'Think and Grow Rich', 'Category': 'Success', 'Rating': 4.7},
    {'Title': 'Atomic Habits', 'Category': 'Success', 'Rating': 4.9},
    {'Title': 'It Ends with Us', 'Category': 'Romantic', 'Rating': 4.6},
    {'Title': 'The Notebook', 'Category': 'Romantic', 'Rating': 4.5},
    {'Title': 'The Girl on the Train', 'Category': 'Mystry', 'Rating': 4.4},
    {'Title': 'Gone Girl', 'Category': 'Mystry', 'Rating': 4.2}
]

def recommend_books_by_Category(user_Category):
    matching_books = [book for book in books_data if user_Category.lower()in book['Category'].lower()]

    if not matching_books:
        return " No books found of the specified Category"
    sorted_books = sorted(matching_books, key = lambda x:x['Rating'], reverse = True)

    recommended_books = [(book['Title'], book['Rating']) for book in sorted_books]
    return recommended_books

user_input_Category = input("Enter the Category of book you'd like to read: ")
recommendations = recommend_books_by_Category(user_input_Category)

if isinstance(recommendations, str):
    print(recommendations)
else:
    print("Recommended books in {user_input_Category} Category.")
    for title, rating in recommendations:
        print(f"{title} - Rating: {rating}")