from copy import deepcopy

from fastai.vision.all import *

# from huggingface_hub import from_pretrained_fastai
from PIL import Image

# from streamlit_js_eval import get_page_location
import pandas as pd
import streamlit as st
import pathlib


_LABELS = (
    "affenpinscher",
    "afghan_hound",
    "african_hunting_dog",
    "airedale",
    "american_staffordshire_terrier",
    "appenzeller",
    "australian_terrier",
    "basenji",
    "basset",
    "beagle",
    "bedlington_terrier",
    "bernese_mountain_dog",
    "black-and-tan_coonhound",
    "blenheim_spaniel",
    "bloodhound",
    "bluetick",
    "border_collie",
    "border_terrier",
    "borzoi",
    "boston_bull",
    "bouvier_des_flandres",
    "boxer",
    "brabancon_griffon",
    "briard",
    "brittany_spaniel",
    "bull_mastiff",
    "cairn",
    "cardigan",
    "chesapeake_bay_retriever",
    "chihuahua",
    "chow",
    "clumber",
    "cocker_spaniel",
    "collie",
    "curly-coated_retriever",
    "dandie_dinmont",
    "dhole",
    "dingo",
    "doberman",
    "english_foxhound",
    "english_setter",
    "english_springer",
    "entlebucher",
    "eskimo_dog",
    "flat-coated_retriever",
    "french_bulldog",
    "german_shepherd",
    "german_short-haired_pointer",
    "giant_schnauzer",
    "golden_retriever",
    "gordon_setter",
    "great_dane",
    "great_pyrenees",
    "greater_swiss_mountain_dog",
    "groenendael",
    "ibizan_hound",
    "irish_setter",
    "irish_terrier",
    "irish_water_spaniel",
    "irish_wolfhound",
    "italian_greyhound",
    "japanese_spaniel",
    "keeshond",
    "kelpie",
    "kerry_blue_terrier",
    "komondor",
    "kuvasz",
    "labrador_retriever",
    "lakeland_terrier",
    "leonberg",
    "lhasa",
    "malamute",
    "malinois",
    "maltese_dog",
    "mexican_hairless",
    "miniature_pinscher",
    "miniature_poodle",
    "miniature_schnauzer",
    "newfoundland",
    "norfolk_terrier",
    "norwegian_elkhound",
    "norwich_terrier",
    "old_english_sheepdog",
    "otterhound",
    "papillon",
    "pekinese",
    "pembroke",
    "pomeranian",
    "pug",
    "redbone",
    "rhodesian_ridgeback",
    "rottweiler",
    "saint_bernard",
    "saluki",
    "samoyed",
    "schipperke",
    "scotch_terrier",
    "scottish_deerhound",
    "sealyham_terrier",
    "shetland_sheepdog",
    "shih-tzu",
    "siberian_husky",
    "silky_terrier",
    "soft-coated_wheaten_terrier",
    "staffordshire_bullterrier",
    "standard_poodle",
    "standard_schnauzer",
    "sussex_spaniel",
    "tibetan_mastiff",
    "tibetan_terrier",
    "toy_poodle",
    "toy_terrier",
    "vizsla",
    "walker_hound",
    "weimaraner",
    "welsh_springer_spaniel",
    "west_highland_white_terrier",
    "whippet",
    "wire-haired_fox_terrier",
    "yorkshire_terrier",
)


def get_breed(path):
    pass


@st.cache_resource
def get_predictor():
    # return from_pretrained_fastai("TheDima/resnet50-dog-breed-identification")
    path = pathlib.Path("dog-breed-identification-export_error-rate-0_118.pkl")
    return load_learner(path)


def predict(image):
    # Get predictions
    predictor = get_predictor()
    pred, pred_idx, probs = predictor.predict(image)
    return pred, probs[pred_idx].item(), probs


def print_probabilities(probs, labels, top_n=10):
    df = pd.DataFrame({"Label": labels, "Probability": probs})
    df = df.sort_values(by="Probability", ascending=False).head(top_n)
    st.dataframe(df, column_order=["Label", "Probability"], hide_index=True)


st.title("Dog Breed Recognition")

# url = get_page_location()
# image_prefix = url["protocol"] + "//" + url["host"]

# st.write("Some doggies for your inspiration")
# d1, d2, d3, d4 = st.columns(4)
# with d1:
#     st.image("static/0a54ce47525781f2caa66f65291dddf8.jpg")
# with d2:
#     st.image("static/0a59d3205cff15e31ee30213b9988e7e.jpg")
# with d3:
#     st.image("static/0ab808aa3571846e50ed74a204662c52.jpg")
# with d4:
#     st.image("static/0c0b3758c1b177b2a2961c1483159898.jpg")


uploaded_file = st.file_uploader("Upload a doggy...", type=["jpg", "jpeg"])
if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    image_copy = deepcopy(image)

    # Make a prediction
    with st.spinner("Checking..."):
        pred, prob, probs = predict(image)

    centered_html = f"""
        <div style="text-align: center;">
            <h3>It is {pred.replace("_", " ").title()}! (I am {100*prob:.1f}% sure 😉)</h3> <br>
        </div>
    """
    st.markdown(centered_html, unsafe_allow_html=True)
    st.image(image_copy, caption="Uploaded doggy", use_column_width=True)

    st.markdown("---")
    st.markdown("Nerdy Top-10 Probabilities: ")
    print_probabilities(probs, _LABELS)

st.markdown("---")
st.write(f"We know only 120 breeds: {', '.join(_LABELS).replace('_', ' ').title()}.")
