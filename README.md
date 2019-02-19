# Wsd 2018 project Colb Paukkeri Lygdman


Project team members:
*Nicholas Colb 591301
Akseli Paukkeri 474995
Jonatan Lygdman 540654*



**This is the documentation of our project.**

First there is a description of completed features, followed by some basic information of the overall workload and teamwork. 
Finally, there is link to our application hosted in Heroku and instructions on how to use it.


## Features of the webshop

    - Authentication

    We implemented the login, logout and register functionalities with email validation.
    It works with Django auth so we think we deserve 200/200 points from that.

    - Basic player functionalities

    Buy/play games. Buying happens through the course's provided payment system.
	We also categorized the games so the users can find them more easily.
	Players can only play games which have been bought. Our backend provides the verification.
	Since everything works as stated in the requirements, we believe 300 points would be fair from this.



    - Basic developer functionalities

    A developer can add games by url (and set price etc). Only a developer can add games.
    The statistics of how many times a given game has been bought can be seen in the developer's profile. We did not implement the ability
    to modify or delete games from the webstore. Since we have this mod/del functionality missing,
    we think we deserve 150/200p from this section.

    - Game/service interaction

    High scores for games. When a user chooses to submit his/her score the app will add the score to our database of global high scores. The score is received through a Javascript event. The highest 10 scores are shown to players in descending order. 
    Since everything works, we think that 200/200p is correct amount of points.

    - Quality of work

    The code is clean, stuctured and commented. The application is structured as it should be in Django.
    User experience is good, and we've tested functionalities. Since there is nothing missing, we believe we deserve 100p.

    - Non-functional requirements

    Impossible to analyze thoroughly. We made project plan and mostly sticked in it.
    We also made the project as a team - eventhough one of the members has significantly more commits than others. (We often worked as a group and had one computer connected to a large TV display.) 
    We think that 150p is enough for this section.

    - Own game

    We developed simple game with JavaScript.
    The game can be found from GitHub,
    from link https://github.com/jonatanlygdman/jonatanlygdman.github.io [here](https://github.com/jonatanlygdman/jonatanlygdman.github.io)

## Success and failures
  
  We think that basic use of Django was easy and we had little trouble in learning its functionalities. The only significant challenge was deploying our 
  app to Heroku. We attended the lecture on Heroku deployment but found it too fast-paced to follow. The Heroku documentation was not thorough nor clear, and we went through 8-10 blogs/videos on how to structure the app and deploy it to the service. Many guides were misleading and deceptive. We pursued our efforts for approximately 30 hours and even struggled with an assistant without results. Finally one of our group managed to do it.
  Without that struggle we would have time to complete more extra features as well.



## Teamwork

  We did not have any specific, designated tasks. We had at least one meeting weakly and continued the work from last time.
  Our philosophy was to complete compulsory parts as well as possible. Most of the meetings were just between two members, alternating between the group. 

  Jonatan worked more than Akseli or Nicholas, since he did a lot of additional work outside the meetings,
  which can also be seen from amount of commits. Nicholas and Akseli did, however, work quite a bit on debugging and the fiasco of deploying the app to Heroku. 

# Instructions on how to use our app

  <a href="http://webstorefinal.herokuapp.com/games">Link to our app</a>

  The link will take the user to our frontpage. 
  In the login page, there is button for registration if the user does not have an account yet. In the registration,
  the user can select their user type: developer or customer.
  
## **IMPORTANT**  
since the email validation works locally in the terminal, you should use pre-existing accounts to log in.

*  For testing the customer's experience use credentials: username: *customer* password: *apple25!*
*  For testing the developer's experience use credentials: username: *developer* password: *banana25!*

  With these accounts you can buy games and play them. Use the developer account to add new games! 


  When pressing register, an activation link will be sent to the user's email, and by pressing the link the user will be redirected to the frontpage of our app.
  
  In the frontpage we have categories for games, and by selecting a category it takes the user to the page where all the games from specific category are listed. 
  To buy a game, the user needs to press the game name in the game view.
  
  **The high score feature only works on our primary game, "Ball game",** as we did not implement the score system on our other game,
  "Sun Jump". Sun Jump was a group project Jonatan was part of 2 years ago and was only added to the web store as a demo. 

  Registered users can also check their profile, where the user can see a list of developed and bought games.

  If user is a developer, a game can be added from nav-button in top-right corner "Add game". It opens a form for the developer to enter the required, specific details about the game. 