from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import string

app = FastAPI()

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_random_string(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(length))

@app.get("/data")
def get_data():
    categories = [generate_random_string(3) for _ in range(100)]
    values = []
    for _ in range(100):
        x = random.randint(10, 200)
        y = random.randint(20, 300)
        z = random.randint(5, 50)
        values.append({"x": x, "y": y, "z": z})
    data = {
        "categories": categories,
        "values": values
    }
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
