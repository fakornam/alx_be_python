

weather=input("What's the weather like today? (sunny/rainy/cold):").lower()

match weather:
    case "sunny":
        print(f"Wear a t-shirt and sunglasses.")
    case "rainy":
        print(f"Don't forget your umbrella and a raincoat.")
    case "cold":
        print(f"Make sure to wear a warm coat and a scarf.")
    case _:
        print(f"Sorry, I don't have recommendations for this weather.")