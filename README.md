# Automobile-price-prediction-project

Deploying the Automobile price prediction ML problem using flask

Steps followed in deploying Machine Learning model using flask to Heroku are-

## 1. Train ML model
Machine Learning model is build using Regression technique in order to predict the price of the automobile.

![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPZiXPBr7XDKCTKtbbmxQXyochA2hFha9Opw&usqp=CAU "Car")


## 2. Create a web app using Flask
I have defined the app routes and completing the app.py file, and created a Index.html which will serve as the home page, which contains all the field required to run the model.

![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0AyQalvJjESKOdjwVPFY858-db7ejzx2xhA&usqp=CAU "Flask")

## 3. Commit the code to GitHub
 Now create some of the required files for deployement and then commit all the files to GitHub.

  Most important thing is to create a Procfile and requirement.txt, which handles the configuration part in order to deploy the model into heroku server. web: gunicorn is the       fixed command, after that the first parameter is app.py file i.e the file which will be executed first. Provide the first parameter without the file extension. Second parameter   is the flask app name.
![alt text](https://res.cloudinary.com/practicaldev/image/fetch/s--NcrUjXyB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/hzfr4vqx1qm3wzirzuff.JPG "Procfile")

Requirements consists of all the libraries that has to get installed in heroku environment.

## 4. Connect GitHub to Heroku
Heroku is a multi-language cloud application platform that enables developers to deploy, scale, and manage their applications. Heroku is elegant, flexible, and easy to use, offering developers the simplest path to getting their apps to market.


![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbOjLuz9j6DwSLqIbIlDp5B1HQZoTcs-y4iQ&usqp=CAU "Heroku")

Heroku gives the direct option to connect with GitHub and deploy the code.

## 5. Deploy the model
After successful deployment, app will be created.
Check out the web-app and provide your suggestions
https://automobile-price-pred-app.herokuapp.com/
