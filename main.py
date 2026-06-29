from fastapi import FastAPI

app = FastAPI()

book = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Data Science with Python",
        "author": "Le Van C",
        "category": "data science",
        "year": 2023,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Machine Learning Basics",
        "author": "Pham Van D",
        "category": "machine learning",
        "year": 2022,
        "is_available": False
    }
]

@app.get("/books/statistics")
def get_book_statistics():
    available_books = 0
    borrowed_books = 0
    for i in book:
        if i["is_available"]:
            available_books += 1
        else:
            borrowed_books += 1
            
    return {
        "total_books": len(book),
        "available_books": available_books,
        "borrowed_books": borrowed_books
    }
    
@app.get("/books/categories")
def get_book_categories():
    categories = []
    for i in book:
        if i["category"] not in categories:    
            categories.append(i["category"])
    return {"categories": categories}

@app.get("/books/latest")
def get_latest_books():
    if not book:
        return {
            "message": "No books available"
        }
    
    max = book[0]
    for i in book:
        if i["year"] > max["year"]:
            max = i
    return {"latest_book": max}