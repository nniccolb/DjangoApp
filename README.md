# Wsd 2018 project Colb Paukkeri Lygdman

Project team members:
Nicholas Colb 591301
Akseli Paukkeri 474995
Jonatan Lygdman 540654


In this project we will implement game store with Django framework. Users can sign in as either players or developers. 
In the game store, there are web-based games that developers can add to store, and players who can buy and play games they have bought. 
In this project plan there are list of features we will provide in the game store. 
At the end of the plan, there are implementation of the Django models, views and also our timetable to complete this project. 


---- Features of the webshop 

    - Authentication

    We plan on implementing authentication through email validation and 3rd party authentication. 
    We will use Django’s authentication for registration and other issues considered. 

    - Basic player functionalities 
    
    Buy/play games. Buying happens through the courses payment system.
	We also plan on categorizing the games so the users can find them more easily. 
	Player can play only games what has been bought. From back-end, we will provide auth for that. 

    - Basic developer functionalities

    Add and modify games in addition to all the same functionalities that the players have. 
    Developer can add games to the store by a link for correct files. 

    - Game/service interaction

    High scores for games. When a game ends the app will compare the score with global high scores for the game.  

    - Games

    We have developed games for the course Verkkojulkaisemisen Perusteet that we plan on using in our project if we don’t have time to create new games.
    We also plan on making the games shearable through social media.

    - Mobile Friendly

    The webshop will be mobile-friendly. We will use the Bootstrap library to implement this

    - GDPR considerations

	User must accept cookies to use site. We will make a pop-up window, where we elaborate data privacy issues in EU and provide options to accept cookies or not. 
	


---- Views and models 

In our Django application, we will have models for User, Developer and Game. Also, in registration we will implement model for users Profile. 
Also, in game store where we have different kinds of games we’ll probably have a model for game-category. 
In Profile model, we we’ll have fields for username, email and password. User and developer use Profile model fields in their actions. 
Game model will have fields such as name and price. Category model has Game models as a Foreignkey and category name. 
In our app, we have views for registration page, home-page where the games are listed and own view for developers to download their games 
to the store. Also, we have a view for purchasing games. Relating views and models, in registration page we use Profile, user and developer
models. In home-page view, we have Game models listed, and for purchasing a game we have view which uses Game and User models. 
In addition, when pushing game to the store as a developer, there is a spesific view for that. These are the minimum requirements for 
models and views, but it is likely that there’ll be some more. 


---- Work plan 

In total, we have two months to complete this project. Since our team-members are quite busy in February, we will have two-week sprint at the 
beginning of the January. In the sprint, we’ll complete the models, views, and basic functionality of the game-store. After that, we’ll meet 
every week and calculate the workload approximately to one work day per week. Weekly meetings are most likely face-to-face, depending a 
situation and problems we probably face. Still, the most important thing in our working plan is to complete the basics quickly in January. 
After the basics, we will complete more functionalities and features to our app in order that the compulsory are done first and optional
after that. We plan to complete at least couple of optional features if we have time at the end. 


---- Timetable

1. Models, views and finally templates (January 1 - January 14)
2. Features starting from compulsory (January 14 - January 30)
3. Testing and improving features (February 1 - February 19)
