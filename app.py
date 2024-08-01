class BookRecommendationSystem:
    def __init__(self):
        self.books = {
            "fiction": ["The Great Gatsby", "1984", "To Kill a Mockingbird"],
            "non-fiction": ["Sapiens", "Educated", "Becoming"],
            "mystery": [
                "Gone Girl",
                "Big Little Lies",
                "The Girl with the Dragon Tattoo",
            ],
        }
        self.ratings = {
            category: {book: [] for book in books}
            for category, books in self.books.items()
        }

    def recommend_books(self, category):
        if category in self.books:
            return self.books[category]
        else:
            return "Category not found"

    def rate_book(self, category, book, rating):
        if category in self.ratings and book in self.ratings[category]:
            self.ratings[category][book].append(rating)
        else:
            print("Book not found in the specified category")

    def get_personalized_recommendations(self, category):
        if category in self.ratings:
            rated_books = {
                book: sum(ratings) / len(ratings)
                for book, ratings in self.ratings[category].items()
                if ratings
            }
            recommended_books = sorted(rated_books, key=rated_books.get, reverse=True)
            return recommended_books
        else:
            return "Category not found"


if __name__ == "__main__":
    system = BookRecommendationSystem()
    while True:
        action = (
            input("Choose an action (recommend, rate, personalized, exit): ")
            .strip()
            .lower()
        )
        if action == "recommend":
            category = (
                input("Enter a book category (fiction, non-fiction, mystery): ")
                .strip()
                .lower()
            )
            recommendations = system.recommend_books(category)
            print(f"Recommended books: {recommendations}")
        elif action == "rate":
            category = (
                input("Enter a book category (fiction, non-fiction, mystery): ")
                .strip()
                .lower()
            )
            book = input("Enter the book title: ").strip()
            rating = float(input("Enter your rating (0-5): "))
            system.rate_book(category, book, rating)
        elif action == "personalized":
            category = (
                input("Enter a book category (fiction, non-fiction, mystery): ")
                .strip()
                .lower()
            )
            recommendations = system.get_personalized_recommendations(category)
            print(f"Personalized recommendations: {recommendations}")
        elif action == "exit":
            break
        else:
            print("Invalid action, please try again")
