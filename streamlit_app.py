import streamlit as st
# Importing Streamlit library
import streamlit as st

# Title of the app with custom CSS
st.markdown(
    """
    <style>
        .title {
            font-size: 36px;
            color: #4CAF50;
            padding: 20px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<p class="title">Sanjana\'s Book Cafe</p>', unsafe_allow_html=True)

# Add a short description with custom CSS
st.markdown(
    """
    <style>
        .description {
            font-size: 18px;
            padding: 10px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<p class="description">Welcome to Sanjana\'s Book Cafe! Sit back, relax, and dive into the world of books.</p>', unsafe_allow_html=True)

# Add a sidebar for navigation with custom CSS
st.sidebar.markdown(
    """
    <style>
        .sidebar {
            font-size: 18px;
            padding: 10px;
            background-color: #f0f0f0;
        }
    </style>
    """,
    unsafe_allow_html=True
)
navigation = st.sidebar.radio('Navigation', ['Home', 'Genres and Books'])

# Home page with custom CSS
if navigation == 'Home':
    st.markdown(
        """
        <style>
            .home {
                font-size: 24px;
                padding: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<p class="home">This is the home page. Check out our book recommendations by genre!</p>', unsafe_allow_html=True)

# Genres and Books page with custom CSS
elif navigation == 'Genres and Books':
    st.markdown(
        """
        <style>
            .genres {
                font-size: 24px;
                padding: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
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

