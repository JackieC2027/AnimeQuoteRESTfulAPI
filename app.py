from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

# Dictionary containing the quotes
quotes = {
    "quote1": {
        "content": "People died when they are killed",
        "character": "Shirou",
        "origin": "Fate/Stay Night"
    },
    "quote2": {
        "content": "Believe it!",
        "character": "Naruto",
        "origin": "Naruto Series"
    },
    "quote3": {
        "content": "I'll take a potato chip... and eat it!",
        "character": "Light Yagami",
        "origin": "Death Note"
    },
    "quote4": {
        "content": "I'm not a nerd. I'm a specialist.",
        "character": "Shiroe",
        "origin": "Log Horizon"
    },
    "quote5": {
        "content": "I won't run away anymore... I won't go back on my word!",
        "character": "Naruto Uzumaki",
        "origin": "Naruto Series"
    },
    "quote6": {
        "content": "It's a terrible day for rain.",
        "character": "Roy Mustang",
        "origin": "Fullmetal Alchemist: Brotherhood"
    },
    "quote7": {
        "content": "I won't scatter your sorrow to the heartless sea. I will always be with you.",
        "character": "Big Boss",
        "origin": "Metal Gear Solid V: The Phantom Pain"
    },
    "quote8": {
        "content": "No matter how deep the night, it always turns to day, eventually.",
        "character": "Sora",
        "origin": "No Game No Life"
    },
    "quote9": {
        "content": "I'm the one who's going to surpass the Hokage!",
        "character": "Naruto Uzumaki",
        "origin": "Naruto Series"
    },
    "quote10": {
        "content": "There is only one thing that matters: to set a person's heart ablaze!",
        "character": "Roronoa Zoro",
        "origin": "One Piece"
    },
    "quote11": {
        "content": "I'm not a pervert... I'm a super pervert!",
        "character": "Jiraiya",
        "origin": "Naruto Series"
    },
    "quote12": {
        "content": "I want to be a potato!",
        "character": "Hachiman Hikigaya",
        "origin": "My Teen Romantic Comedy SNAFU"
    },
    "quote13": {
        "content": "I don't want to conquer anything. I just think that the guy with the most freedom in this ocean is the Pirate King!",
        "character": "Monkey D. Luffy",
        "origin": "One Piece"
    },
    "quote14": {
        "content": "The only ones who should kill are those who are prepared to be killed.",
        "character": "Lelouch vi Britannia",
        "origin": "Code Geass"
    },
    "quote15": {
        "content": "Courage is not the absence of fear, but rather the judgment that something else is more important than fear.",
        "character": "Rin Tohsaka",
        "origin": "Fate/stay night"
    },
    "quote16": {
        "content": "Even if the world ends, as long as I'm with you, I'll be happy.",
        "character": "Yato",
        "origin": "Noragami"
    },
    "quote17": {
        "content": "There are no regrets. If one can be proud of one's life, one should not wish for another chance.",
        "character": "Saber",
        "origin": "Fate/stay night"
    },
    "quote18": {
        "content": "Fear is not evil. It tells you what your weakness is. And once you know your weakness, you can become stronger.",
        "character": "Gildarts Clive",
        "origin": "Fairy Tail"
    },
    "quote19": {
        "content": "It's not the world that's messed up; it's those of us in it.",
        "character": "Light Yagami",
        "origin": "Death Note"
    },
    "quote20": {
        "content": "The world's not perfect, but it's there for us trying the best it can.",
        "character": "Makoto Shinkai",
        "origin": "Your Name"
    },
}


# Custom abort function to handle errors
def abort(quote_id):
    if quote_id not in quotes:
        abort(404, message=f"Todo {quote_id} doesn't exist")

# Request parser for parsing request arguments
parser = reqparse.RequestParser()
parser.add_argument('quote')

@app.route('/')
def index():
    return render_template('index.html')

# Resource for handling individual quotes
class Quote(Resource):
    # Retrieve a specific quote by ID
    def get(self, quote_id):
        abort(quote_id)
        return quotes[quote_id]

    # Delete a specific quote by ID
    def delete(self, quote_id):
        abort(quote_id)
        del quotes[quote_id]
        return "", 204

    # Update a specific quote by ID
    def put(self, quote_id):
        args = parser.parse_args()
        quote = {'quote': args['quote']}
        quotes[quote_id] = quote
        return quote, 201
    
# Resource for handling a list of quotes
class QuoteList(Resource):
    # Retrieve all quotes
    def get(self):
        return quotes

    # Create a new quote
    def post(self):
        args = parser.parse_args()
        quote_id = int(max(quotes.keys()).lstrip('quote')) + 1
        quote_id = 'quote%i' %quote_id
        quotes[quote_id] = {'quote': args['quote']}
        return quotes[quote_id], 201

# Add resources to the API
api.add_resource(Quote, '/quotes/<quote_id>')
api.add_resource(QuoteList, '/quotes')

if __name__ == "__main__":
    app.run(debug=True)
