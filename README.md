# Generarive_AI
Step-1 : Create a New folder and open vs code in it and open terminal and write conda create -v venv python==3.10 -y

second-option : create virtual environment using pip python -m venv myenv myenv\Scripts\activate.bat

third-option : Install all the packages in your local system

step-2 : Create a 'requirements.txt' file streamlit python-dotenv google-generativeai

Now open the terminal and write pip install -r requirements.txt

step-3 : Now we will create '.env' file in which we will store our secrets . Go to Browser and write Makersuite api key ===> Create an api key ==> copy it and paste it into .env file GOOGLE_API_KEY = "paste_your_api_key"

step-4 : We will create 'app.py' file where we will create a function that will take our query as an argument and send it to google_generative model and our generative model will response based on your query in the textual format . Here we will use streamlit for our page_title design , Input_field design . When user click to submit button then our function will run and return our response .

open the terminal and write streamlit run app.py

step-5 : create a .gitginore file and venv/ .env put all the files and folder here which you do not want to push on github.

step-5 : Go to Github and create a new repository and fill repository name and write commands on the terminal of our vs code

git init git add . git commit -m "first commit" git branch -M main git remote add origin https://github.com/githubusername/pce_bot.git git push -u origin main
