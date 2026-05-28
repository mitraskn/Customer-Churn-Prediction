# def main():
#     print("Hello from uvsample01!")


# if __name__ == "__main__":
#     main()
from fastapi import FastAPI
import emoji
import pyjokes

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Hello 😊"}

# Emoji route
@app.get("/emoji")
def get_emoji():
    text = emoji.emojize("I love Python :rocket:")
    return {"emoji": text}

# Joke route
@app.get("/joke")
def get_joke():
    joke = pyjokes.get_joke()
    return {"joke": joke}