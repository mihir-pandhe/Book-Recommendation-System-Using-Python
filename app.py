class BookRecommendationSystem:
    def __init__(self):
        self.books = {
            'fiction': ['The Great Gatsby', '1984', 'To Kill a Mockingbird'],
            'non-fiction': ['Sapiens', 'Educated', 'Becoming'],
            'mystery': ['Gone Girl', 'Big Little Lies', 'The Girl with the Dragon Tattoo']
        }

    def recommend_books(self, category):
        if category in self.books:
            return self.books[category]
        else:
            return 'Category not found'

if __name__ == '__main__':
    system = BookRecommendationSystem()
    category = input("Enter a book category (fiction, non-fiction, mystery): ").strip().lower()
    recommendations = system.recommend_books(category)
    print(f"Recommended books: {recommendations}")
