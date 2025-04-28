import streamlit as st

# Mock product data
products = [
    {"id": 1, "name": "T-shirt", "price": 20, "image": "images/tshirt.png"},
    {"id": 2, "name": "Shoes", "price": 50, "image": "images/shoes.png"},
    {"id": 3, "name": "Watch", "price": 100, "image": "images/watch.png"},
]

# Initialize cart in session
if "cart" not in st.session_state:
    st.session_state.cart = []

# Display products
st.title("🛒 My Shop")

for product in products:
    st.image(product["image"], width=150)
    st.write(f"**{product['name']}**")
    st.write(f"Price: ${product['price']}")

    if st.button(f"Add {product['name']} to Cart"):
        st.session_state.cart.append(product)
        st.success(f"Added {product['name']} to cart!")

# View cart
st.header("🛍️ Your Cart")

total = 0
for item in st.session_state.cart:
    st.write(f"- {item['name']} (${item['price']})")
    total += item['price']

st.write(f"### Total: ${total}")

if st.button("Checkout"):
    st.success("Thank you for your purchase!")
    st.session_state.cart = []
