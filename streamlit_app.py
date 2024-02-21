import streamlit as st
# Importing Streamlit library
import streamlit as st

# Add custom CSS for background
st.markdown(
    """
    <style>
        * {
            background-color: black !important; /* Change to your preferred background color */
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
            text-align:center;
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
        'Popular Fantasies': ['The Night Circus', 'The Name of the Wind', 'Harry Potter'],
        'Popular Romantic Comedy': ['Bridget Jones\'s Diary', 'The Rosie Project', 'Crazy Rich Asians']
    }
    book_img=['https://s.hdnux.com/photos/06/13/40/1619968/3/1200x0.jpg',
              'https://m.media-amazon.com/images/S/aplus-media/vc/972d3fab-4906-452c-8e9a-5771fb23a3b6.jpg',
              'https://images.thenile.io/r1000/9780747554561.jpg',
              'https://images.gr-assets.com/books/1292060045l/227443.jpg',
              'https://prodimage.images-bn.com/pimages/9781982172930_p0_v3_s550x406.jpg',
              'https://the-bibliofile.com/wp-content/uploads/2014/12/crazyrichasians.png']
              
    i=0
    for genre, books in genres_books.items():
        st.subheader(genre)
        for book in books:
            st.write(book)
            st.image(book_img[i], use_column_width=True)
            
            i+=1
