# Wsd 2018 project Colb Paukkeri Lygdman

Documentation


Project team members:
Nicholas Colb 591301
Akseli Paukkeri 474995
Jonatan Lygdman 540654


This is the documentation of our project. First there are description of features completed, after that there is basic information of workload and teamwork. At the end, there is link to our application hosted in Heroku and instructions to use it.


---- Features of the webshop

    - Authentication

    We implemented login, logout and register functionalities with email validation.
    All works smoothly with Django auth so we think we deserve 200/200 points from that.

    - Basic player functionalities

    Buy/play games. Buying happens through the courses payment system.
	We also categorized the games so the users can find them more easily.
	Player can play only games what has been bought. From back-end, we will provide auth for that.
	Since everything works, we think we deserve 300p from this section.



    - Basic developer functionalities


    A developer can add games by url (and set price etc). Only developer can add games.
    Sales statistics of developer's own games can be seen in developers profile. We did not conduct the ability
    to modify or delete games from webstore. Since we have this mod/del functionality missing,
    we think we deserve 150/200p from this section.

    - Game/service interaction

    High scores for games. When a game ends the app will compare the score with global high scores for the game.
    Since everything works, we think that 200/200p is correct amount of points.

    - Quality of work

    The code is clean, stuctured and mostly commented. The application is structured as it should be in Django.
    User experience is good, and we've tested functionalities. Since there is nothing missing, we deserve 100p.

    - Non-functional requirements

    Impossible to analyze correctly. We made project plan and mostly sticked in it.
    We also made the project as a team - eventhough one of the members has significantly more commits than others. 
    We think that 150p is enough for this section.

    - Own game

    We developed simple game with JavaScript.
    The game can be found from GitHub,
    from link <a href="https://github.com/jonatanlygdman/jonatanlygdman.github.io"> Link to our game </a>

  ----- Success and failures
  
  We think that basic use of Django was easy and we had no large trouble in functionalities. The only enormous challenge was deploying our 
  app to Heroku. We tried that dozens of hours, even some with an assistant with no results. Finally one of our group managed to do that,
  without that struggle we would have time to complete more extra features as well.



  -----  Teamwork

  We did not have any specific responsibilities. We had at least one meeting weakly and continued the work from last time.
  Our philosophy was to complete compulsory parts as fast as possible. Most of the meetings were just between two members instead of three,
  since we all were quite busy during this period.

  Jonatan worked than Akseli or Nicholas, since he made some additional work outside the meetings,
  which can also be seen from amount of commits.

  ----- Instructions

  <a href="http://webstorefinal.herokuapp.com/games">Link to our app</a>

  The link will take the user to our frontpage. To login, press nav-button in top-right corner and press Login.
  In the login page, there is button for registration if the user does not have an account yet. In the registration,
  there can be selected usertypes: developer or customer.

  When pressing register, an activation link comes to the user's email, and by pressing the link user get's again to the frontpage of our app.
  
  In the frontpage we have categories for games, and by pressing category it takes user to the page where are all games from specific category. 
  To buy a game, user need to press the game name in the game view.

  Registered user can also check his profile, where the user can see developed and bought games.

  If user is a developer, game can be added from nav-button in top-right corner "Add game". If opens a form where developer puts specific information about the game, also URL.
