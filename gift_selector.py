
gifts = [
    "Book", "Toy", "Gadget", "Video Game", "Headphones", 
    "Smartphone", "Laptop", "Watch", "Shoes", "Wallet", 
    "Headset", "Camera", "Drone", "Smart Watch", "Bluetooth Speaker"
]


def calculate_gift_code(indices):
    code = 0
    for idx in indices:
        code |= (1 << idx)
    return code


def display_result(selected_gifts, gift_code):
    html_output = f"""
    <html>
    <head><title>Gift Selection Result</title></head>
    <body>
        <h1>Gift Selection Extravaganza</h1>
        <p>Selected Gifts: {', '.join(selected_gifts)}</p>
        <p>Unique Gift Code: {gift_code}</p>
    </body>
    </html>
    """
    return html_output


if __name__ == "__main__":
    selected_indices = input("Enter gift indices separated by commas (e.g., 0,1): ")
    selected_indices = [int(i.strip()) for i in selected_indices.split(',')]

    selected_gifts = [gifts[i] for i in selected_indices]
    gift_code = calculate_gift_code(selected_indices)

    print(display_result(selected_gifts, gift_code))
