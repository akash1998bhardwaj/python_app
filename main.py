import streamlit as st

st.title("Responsive Website with Streamlit")

col1, col2, col3 = st.columns([2, 1, 1])  # 2:1:1 column ratio
with col1:
    st.header("Main Content")
    st.write("This section occupies a larger space.")
with col2:
    st.header("Sidebar")
    st.write("This is a smaller column.")
with col3:
    st.header("Ads")
    st.write("Add widgets here.")

# Responsive containers
with st.container():
    st.subheader("Footer Section")
    st.write("Add responsive elements here.")





st.markdown(
    """
    <style>
    .custom-header {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #4CAF50;
    }
    .responsive-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }
    .card {
        flex: 1;
        margin: 10px;
        padding: 15px;
        border: 1px solid #ddd;
        border-radius: 8px;
        max-width: 300px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    <div class="custom-header">Welcome to My Responsive Website</div>
    <div class="responsive-container">
        <div class="card">Card 1</div>
        <div class="card">Card 2</div>
        <div class="card">Card 3</div>
    </div>
    """,
    unsafe_allow_html=True
)



st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <div class="container">
        <div class="row">
            <div class="col-md-6">Column 1</div>
            <div class="col-md-6">Column 2</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


st.sidebar.title("Left Menu")
page = st.sidebar.radio("Go to", ["Home", "About"])

if page == "Home":
    st.title("Home Page")
    st.write("Welcome to the responsive home page!")
elif page == "About":
    st.title("About Page")
    st.write("This is the about section.")