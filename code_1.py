import pandas as pd
import random 

df = pd.read_csv("tech.csv")

def generate_quote():
    """Generate and display a random quote from the CSV file."""
    random_index = random.randint(0, len(df) - 1)
    random_quote = df.loc[random_index, "Quote"]
    print(random_quote)

if __name__ == "__main__":
    generate_quote()
