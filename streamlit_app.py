import streamlit as st
import streamlit as st

# Add custom CSS for background and text styles
st.markdown(
    """
    <style>
        *{
            background:#8da29f !important;
        }

        .title {
            font-size: 50px;
            color: Black; /* Green title color */
            padding: 20px;
            text-align: center;
            font-style:italic;
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

        .genre-header {
            background-color: #FFD700; /* Gold background color for genre headers */
            color: #800080; /* Purple text color for genre headers */
            padding: 10px;
            margin-top: 20px;
            border-radius: 10px;
        }

        .book-name {
            font-style: italic; /* Italicize book names */
            text-align: center; /* Center-align book names */
            color: #FF4500; /* Orange book name color */
        }

        .book-image {
            border-radius: 40%; /* Rounded corners for book images */
            display: block; /* Make image a block element */
            margin-left: auto; /* Center-align image horizontally */
            margin-right: auto; /* Center-align image horizontally */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown('<p class="title">Sanjana\'s Colorful Book Cafe 🌈📚</p>', unsafe_allow_html=True)

# Add a short description
st.markdown('<p class="description">Welcome to Sanjana\'s Book Cafe! Sit back, relax, and dive into the world of books.</p>', unsafe_allow_html=True)

# Add a sidebar for navigation
navigation = st.sidebar.radio('Navigation', ['Home', 'Genres and Books'])

# Home page
if navigation == 'Home':
    st.markdown('<p class="description">This is the home page. Check out our book recommendations by genre!</p>', unsafe_allow_html=True)

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
        st.markdown(f'<p class="genre-header">{genre}</p>', unsafe_allow_html=True)
        for book in books:
            st.markdown(f'<p class="book-name">{book}</p>', unsafe_allow_html=True)
            st.image(book_img[i], width=500, caption=book, use_column_width=False)
            i+=1
