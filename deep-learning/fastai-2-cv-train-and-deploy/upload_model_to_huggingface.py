import os

from dotenv import load_dotenv

from huggingface_hub import login, push_to_hub_fastai
from fastai.vision.all import *

load_dotenv()
login(token=os.getenv("HUGGINGFACE_TOKEN"))

learn = load_learner("dog-breed-identification-export_error-rate-0_118.pkl")
push_to_hub_fastai(learner=learn, repo_id="TheDima/resnet50-dog-breed-identification")
