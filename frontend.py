import streamlit as st
from PIL import Image, ImageDraw
import base64
import backend

def mask_circle_transparent(pil_img, blur_radius=0, offset=0):
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    offset = blur_radius / 2
    width, height = pil_img.size
    draw.ellipse([offset, offset, width - offset, height - offset], fill=255)
    pil_img.putalpha(mask)
    return pil_img


st.set_page_config(page_title="AlgoAssist", layout="wide", initial_sidebar_state="expanded")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_gif_as_page_bg(gif_file):
    bin_str = get_base64_of_bin_file(gif_file)
    page_bg_img = f'''
    <style>
    .stApp {{
      background-image: url("data:image/gif;base64,{bin_str}");
      background-size: cover;
      background-repeat: no-repeat;
      background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

background_image_path = r"bg3.jpg"
set_gif_as_page_bg(background_image_path)
st.markdown("<h1 style='font-size: 50px; color: #F8F8FF;'>AlgoAssist</h1>", unsafe_allow_html=True)

# col1, col2 = st.columns([1,2])
# with col2:
# logo_path = "logo.jpg"
#     logo_image = Image.open(logo_path)
#     logo_image = logo_image.resize((100, 100))
#     st.image(logo_image, use_column_width=False)
col1, col2 = st.columns([1, 2])
def run():
    prompt = st.session_state['question_input']
    st.session_state['solution'] = backend.give_response(prompt)
    st.session_state['tags'] = backend.give_tags(prompt)


with col1:
    st.markdown("<h2 style='font-size: 30px; color: #f5f5f8;'>Question", unsafe_allow_html=True)
    with st.expander("Question", expanded=True):
        question_input = st.text_area("Enter your question...",key="question_input")
    st.markdown('</h2>', unsafe_allow_html=True)
    st.button("Enter",on_click=run)
    st.subheader("Tags")
    if "tags" not in st.session_state:
        st.session_state["tags"] = " "
    with st.container():
        st.markdown(st.session_state["tags"], unsafe_allow_html=True)
#print(st.session_state)
if "question_input" not in st.session_state:
    st.session_state["question_input"] = "Enter your Question..."


with col2:
    st.markdown("<h2 style='font-size: 30px; color: #f8f8ff;'>Solution</h2>", unsafe_allow_html=True)
    if "solution" not in st.session_state:
        st.session_state["solution"] = "Your solution will be displayed here.. "
    with st.container():
        st.markdown(st.session_state["solution"], unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 35px; color: #ffffff;'>Team", unsafe_allow_html=True)
with st.expander(" ",expanded=False):
    team_members = ["Pragya Rathal", "Sparsh Rastogi", "Shlok Matanhelia", "Kaustubh Roy", "Naitik Agrawal"]
    image_paths = ["bg.jpg", "bg2.jpg", "bg3.jpg", "bg5.jpg", "bg4.jpg"]

    team_cols = st.columns(len(team_members))

    for i, col in enumerate(team_cols):
        with col:
            image = Image.open(image_paths[i])
            image = image.resize((75, 75))
            image = mask_circle_transparent(image)
            st.image(image)
            st.markdown(f"<h3 style='font-size: 20px; color: #ffffff;'>{team_members[i]}</h3>", unsafe_allow_html=True)
