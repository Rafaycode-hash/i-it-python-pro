import streamlit as st

# Page Configuration
st.set_page_config(page_title="My Portfolio", page_icon="📘", layout="wide")

# Sidebar Navigation
st.sidebar.title("📂 Navigation")
section = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Contact"])

# Home Section
if section == "Home":
    st.title("👋 Welcome to My Website")
    st.subheader("I’m Abdul Rafay Sheikh — a Frontend Developer & Student 👨‍💻")
    st.write("This is a simple website built using Python and Streamlit.")

# About Me Section
elif section == "About Me":
    st.header("🙋 About Me")
    st.write("""
    I'm currently learning Python, HTML, CSS, Bootstrap and Streamlit.
    I also study Computer Science and Space Science.
    
    I love building small projects that improve my skills and help others.
    """)
    st.image("https://via.placeholder.com/300x200.png?text=My+Photo", caption="That’s me!", use_column_width=False)

# Projects Section
elif section == "Projects":
    st.header("🛠 My Projects")
    st.write("- ✅ Unit Converter Web App (Streamlit)")
    st.write("- ✅ Password Strength Meter")
    st.write("- ✅ Personal Library Manager")
    st.write("- ✅ BMI Calculator")
    st.write("- ✅ Rock, Paper, Scissors Game")
    st.write("...and many more in progress!")

# Contact Section
elif section == "Contact":
    st.header("📬 Contact Me")
    st.write("Email: abdulrafaysheikh5656@gmail.com")
    st.write("Phone: +92 332 3920344")
    st.write("[LinkedIn Profile](https://www.linkedin.com/in/abdul-rafay-sheikh-169238260)")

st.markdown("---")
st.caption("Made with ❤️ by Abdul Rafay using Python & Streamlit")
