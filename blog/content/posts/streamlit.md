+++
title = 'Brief Detour Into UI Development'
date = 2024-07-22T17:02:11-07:00
draft = false
+++

As a software engineer with a background in large-scale distributed systems, I've consistently struggled to create user-friendly interfaces for my projects. In fact, I've found myself relying more heavily on Linux command-line tools rather than their desktop alternative.

However, I clearly understand the importance of providing users with a simple and straightforward way to use my scripts, apps, or models. It's important to present my work to friends, hackathon judges, or strangers online with a nice user experience. Dozens of pages of documentation can't replace a few intuitive forms and buttons, even though I've tried to convince myself otherwise. While some things are inherently complex, as a single engineer looking to share my pet project with the world, I sometimes can create a simple, user-friendly way to interact with my work.

## Why not HTML/CSS/JavaScript?

While a native app or a web app built with advanced HTML/CSS and modern frameworks like React would be significantly better, there are three major issues to consider.

- Firstly, my knowledge of HTML, CSS, JavaScript, and modern frameworks like React and Vue is extremely limited. Mastering these tools requires a huge time commitment, similar to what I've invested in ML systems design and development. I wouldn't be able to create an app that's even remotely decent.
- Secondly, I'm not interested in learning web development technologies, as they don't align with my engineering specialty. My area of expertise is vastly different and far removed from client-side web development.
- Thirdly, even if I could create an app by copying and pasting code and seeking help from ChatGPT, deploying and maintaining both the client and server sides would likely require too much time and effort, particularly when it comes to ensuring reliable connectivity between the server API and client side.

These reasons are highly subjective and based on my personal preferences, so they may not apply to everyone.

## Streamlit

In my daily practice, I work with two programming languages: Python and C++. Since I wanted to leverage my existing knowledge, I only needed to choose a framework. It's likely that Python would have a solution for building frontends, and that's exactly what I found. Between the two most popular tools, [Gradio](https://www.gradio.app/) and [Streamlit](https://streamlit.io/), I opted for Streamlit. Although it takes a bit more effort to learn, it offers more flexibility in the long run.

Streamlit enables me to build and deploy attractive data-driven and ML-powered web apps. There are several ways to get started. For instance, you can explore numerous YouTube videos created by data scientists who showcase their portfolios through Streamlit apps. Alternatively, you can read the ["Getting Started" documentation](https://docs.streamlit.io/get-started/fundamentals) and experiment with the framework to create something impressive. I opted for the ["30 Days of Streamlit" challenge](https://blog.streamlit.io/30-days-of-streamlit), a fun way to learn and practice using Streamlit. All my scripts from the challenge are stored here: <https://github.com/CuriousDima/30days-streamlit>.

To practice my Streamlit skills after the challenge, I built a few small apps that I use occasionally.

- The first one is quite straightforward: a [percentage calculator](https://percent.streamlit.app/) that runs solely on Python logic without relying on external code. Occasionally, I use it when managing resource consumption and provisioning for the systems I work on: <https://github.com/CuriousDima/30days-streamlit/blob/main/percentage_calculator.py> ![Percentage calculator on Streamlit](/ai/images/streamlit_percentage_calculator.png)
- The second app is more intriguing. It serves as a [frontend for my trusty Telegram bot](https://pardonmyenglish.streamlit.app/), which helps me write like a native English speaker. This app makes external calls to various APIs, including OpenAI, Groq, and Perplexity, making the code a bit more interesting. Notably, it shares an LLM client library with the Telegram bot: <https://github.com/CuriousDima/pardon-my-english/blob/main/frontend.py> ![Pardon My English tool on Streamlit](/ai/images/streamlit_pardon_my_english.png)
- The third app is the most interesting one. It showcases [the deployment of a CV model](https://thedima-dog-breed-recognition.hf.space/). I was thrilled with the simplicity of the resulting app and really wanted to share it with the internet in a separate article: <https://curiousdima.medium.com/deploying-a-computer-vision-model-as-a-streamlit-app-on-huggingface-spaces-243c02ec2081> ![Breed Recognition CV App on Streamlit](/ai/images/streamlit_cv_dogs.jpg)

## Conclusion

My brief foray into frontend development didn't take long. I quickly learned Streamlit, which provided me with a simple, user-friendly framework for building interfaces. Although I realize it can't replace a full-fledged, polished web application, it's still a valuable tool for me to showcase my work in an accessible way.
