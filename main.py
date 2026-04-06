import random

quotes = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("You miss 100% of the shots you don't take.", "Wayne Gretzky"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("I have not failed. I've just found 10,000 ways that won't work.", "Thomas Edison"),
    ("The only impossible journey is the one you never begin.", "Tony Robbins"),
    ("In the middle of difficulty lies opportunity.", "Albert Einstein"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("Keep your face always toward the sunshine—and shadows will fall behind you.", "Walt Whitman")
]

def main():
    quote, author = random.choice(quotes)
    print(f'"{quote}" - {author}')

if __name__ == "__main__":
    main()