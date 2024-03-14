import os
from flask import Flask, render_template
import random

app = Flask(__name__)

tech_quotes = [
    "Talk is cheap. Show me the code. - Linus Torvalds",
    "The best thing about a boolean is even if you are wrong, you are only off by a bit. - Unknown",
    "Programming isn't about what you know; it's about what you can figure out. - Chris Pine",
    "Code is like humor. When you have to explain it, it's bad. - Cory House",
    "There are only two hard things in computer science: cache invalidation and naming things. - Phil Karlton",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler",
    "Debugging is like trying to find a needle in a haystack. Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it. - Brian Kernighan",
    "Programming is not about typing, it's about thinking. - Rich Hickey",
    "The most important skill for a programmer is to learn how to learn. - John Sonmez",
    "Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the universe trying to produce bigger and better idiots. So far, the universe is winning. - Rick Cook"
]

@app.route("/")
def index():
    quote = random.choice(tech_quotes)
    # print(quote)
    return render_template("index.html", quote=quote)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))