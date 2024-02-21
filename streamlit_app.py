import streamlit as st
# Importing Streamlit library
import streamlit as st

# Add custom CSS for background
st.markdown(
    """
    <style>
        body {
            background-color: #f0f0f0; /* Change to your preferred background color */
            /* Uncomment the line below and replace 'url' with your image path to set a background image */
            /* background-image: url('background.jpg'); */
            /* Optional: You can add more CSS properties to customize the background, such as background-size, background-position, etc. */
        }

        .title {
            font-size: 36px;
            color: #4CAF50;
            padding: 20px;
            text-align: center;
        }

        .description {
            font-size: 18px;
            padding: 10px;
            text-align: center;
        }

        .sidebar {
            font-size: 18px;
            padding: 10px;
            background-color: #f0f0f0;
        }

        .genres {
            font-size: 24px;
            padding: 20px;
        }

        .home {
            font-size: 24px;
            padding: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown('<p class="title">Sanjana\'s Book Cafe</p>', unsafe_allow_html=True)

# Add a short description
st.markdown('<p class="description">Welcome to Sanjana\'s Book Cafe! Sit back, relax, and dive into the world of books.</p>', unsafe_allow_html=True)

# Add a sidebar for navigation
navigation = st.sidebar.radio('Navigation', ['Home', 'Genres and Books'])

# Home page
if navigation == 'Home':
    st.markdown('<p class="home">This is the home page. Check out our book recommendations by genre!</p>', unsafe_allow_html=True)

# Genres and Books page
elif navigation == 'Genres and Books':
    st.markdown('<p class="genres">Explore our collection by genre:</p>', unsafe_allow_html=True)

    # Displaying genres and recommended books with images
    genres_books = {
        'Fantasy': ['The Night Circus', 'The Name of the Wind', 'Harry Potter'],
        'Mystery': ['The Girl with the Dragon Tattoo', 'Gone Girl', 'The Da Vinci Code'],
        'Science Fiction': ['Dune', 'The Martian', 'Neuromancer'],
        'Romantic Comedy': ['Bridget Jones\'s Diary', 'The Rosie Project', 'Crazy Rich Asians']
    }
    
    for genre, books in genres_books.items():
        st.subheader(genre)
        for book in books:
            st.image(f"https://via.placeholder.com/150?text=Cover+of+{book}", use_column_width=True)
            st.write(book)
