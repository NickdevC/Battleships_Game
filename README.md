<h1 align="center"> :anchor: Battleships Game :anchor: </h1>

[View the live project here](https://nickdevc-battleships.herokuapp.com/)

Based on the popular, classic boardgame, Battleships is a Python terminal game running on Heroku. It provides 4x overlapping fields of play, allowing the user to place their ships and also target those of the computer. The user manually selects their ship placements, whilst the computer is randomly assigned coordinates. The game is won when all 5 of the opponent's ships have been destroyed!

![mockup](assets/images/am_i_responsive.png)

## Index - Table of Contents
*  [Scope](#scope)
*  [Features](#features)
*  [Design](#design)
*  [Technologies Used](#technologies-used)
*  [Testing](#testing)
*  [Deployment](#deployment)
*  [Credits](#credits)


## Scope

-  ### Initial plan
   


## Features

   ### Existing/current Features
      
-   __Welcome Screen__

    - 

      ![Navbar](assets/images/welcome_screen.png)

-   __Rules__

    - A 

      ![Navbar](assets/images/rules_message.png)
      
-   __Player Placement__

    - 

      ![Navbar](assets/images/user_placement.png)
      
-   __Player/computer Guesses__

    - 

      ![Navbar](documentation/website-screenshots/End-page.png)

-   __Visual feedback__

    - 

      ![Navbar](documentation/website-screenshots/Leaderboard.png)

   ### Potential Future Features
   
- User name input
   - This would add a personal touch to the game and allow for further feedback throughout the playtime ie. messages throughout the game could include direct reference to the user.
- APIs
   - Using Google Cloud APIs, I could store the user's name into a database.
   - I could then ensure unique usernames are used and check against returning players, displaying previous scores before playing. This could potentially add an additional competitive element.
- A visual leaderboard
   - With the use of APIs, I could create a 'Top 5' leaderboard to be displayed at the start of the game. This could be measured with 'least amounts of guesses'.

## Design

   ### Colour
- 

   ![Navbar](documentation/website-screenshots/Coolors-quiz-scheme.png)
   


## Technologies and Support

### Languages Used

-   [Python](https://en.wikipedia.org/wiki/python)

### Frameworks, Libraries, Programs, and Websites

-   ['Time' module](https://docs.python.org/3/library/time.html)
      - Used to support my understanding of the time module and ultimately lead to the inclusion of time delays on various 'print' messages throughout the game, leading to more comfortabel user experience.
      
-   ['Sys' module](https://docs.python.org/3/library/sys.html)
      - Used to support my understanding of the sys module which resulted in the 'typewriter' style animation attached to various 'print' statements. This was an aesthetic addition that helped slow down the pace of the game and a better user experience.

-   ['Random' module](https://docs.python.org/3/library/random.html)
      - This module was needed to incorporate the 'randint' method of returning random integers for the computer's ship placement.
      
-   [ASCII Art Library](https://pypi.org/project/art/)
      - This website helped familiarise myself with ASCII art and lead to me finding the 'Battleships' welcome text and my own devleopment of the 'ship' image (also on the welcome screen).

-   [Randint method(w3schools)](https://www.w3schools.com/python/ref_random_randint.asp)
      - Used this website to refresh my knowledge of randint, and helped me to apply this method to the computer's random choice function. 

-   [Slow typing effect in Python(stack overflow)](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing)
      - Referenced this post to learn about how to implement the slow typing effect on Python print statements. This lead me to using the 'sys' module.

-   [Coloured text in Python(stackabuse)](https://stackabuse.com/how-to-print-colored-text-in-python/)
      - Referenced this guide for applying colours to various different ships (on the welcome screen) and applying a base colour of blue to the majority of text in the terminal.

-   [Placeholders within strings(stack overflow)](https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting)
      - Used this to help me overcome some difficulties I was facing with certain strings in my code.

-   [Unexpected unident error(stack overflow)](https://stackoverflow.com/questions/10239668/indentationerror-unexpected-unindent-why)
      - Referenced this post to help me work through a challenging bug regarding some of my indentation which was breaking the entirity of my code.

-   [Battleship function ideas(stack overflow](https://codereview.stackexchange.com/questions/tagged/battleship)
      - Referenced posts within the stack overflow community to support the building of some of my functions. This also helped me visualise the 4x overlapping fields-of-play concept.

-   [Am I Responsive](https://ui.dev/amiresponsive)
      - Used to produce the 'mockup' image of my game running on different devices (top of readme file).

## Testing
   
#### PEP8

- Due to the fact that the PEP8 website is currently down, I added the PEP8 validator to my Gitpod Workspace and ensured pycodestyle was enabled. This returned **no 'red' errors** and the only 'yellow' errors present were those referencing whitespace in and around my ASCII art at the start of my code.
   
   
### Browser Compatibility

- Testing has been successfully carried out on the following browsers:
   
   - Google Chrome - Version 100.0.4896.60 (Official Build) (64-bit)
   - Microsoft Edge - Version 100.0.1185.50 (Official build) (64-bit)
   - Mozilla FIrefox - Version 99.0.1 (64-bit)
   - Safari - Version 13.1.3 (15609.4.1)

### User Testing

- A total of **6 different users** tested the website on desktop devices. At the time of testing, the main conclusions drawn were as follows:
      
     - The game opened successfully and everyone was greeted with the welcome message :white_check_mark:
     - All users successfully saw the 'sys' and 'time' modules working as text was delayed and followed a typerwriter effect :white_check_mark:
     - All users could see the colour variations of text :white_check_mark:
     - All users saw the field of play displayed and were correctly guided through prompts to place their ships :white_check_mark:
     - On placing their ships, users were unable to place ships vertically :red_circle: 
          - This is still unresolved and, although I have sought and found workable solutions through the Slack community (including a different method of displaying the grid using complex mathematics) I am unable to implement these in my current timeframe.
     - During the game, all users reported the successful, random, deployment of the computer's ships :white_check_mark:
     - All users were able to see the correct markers for 'hits' and 'misses', and were able to read visual prompts regarding this :white_check_mark:
     - When the total number of hits was reached, all users experienced the 'end message' either congratulating or commiserating :white_check_mark:

### Resolved Bugs

- **Raising ValueError**
      - I struggled with the syntax surrounding the multiple applications of the ValueError. Ultimately, I used advice on the internet and realised that one of my lines of code required the KeyError exception instead.

### Unresolved Bugs

- raising ValueError - struggled with syntax which lead to multiple errors...
- player_input function - not correctly completing my 'try' statement with an 'except'...
- ship placement issues - not correctly placing ships vertically...
 
## Deployment

   ### How to deploy

- Go to the GitHub repository and navigate to the 'Settings' tab. Once there, select 'Pages' from the menu
- Go to the 'Source' menu (drop-down box) and select 'Master Branch'
- After the page has auto-refreshed, you should see a detailed ribbon display - this demonstrates a successful deployment
- Now, any changes pushed from GitPod to the master branch will be visible and take effect on the live project [live project link](https://nickdevc.github.io/Film_Quiz)

   ### How to clone

- Go to the following repository on GitHub: https://github.com/NickdevC/Film_Quiz
- At the top right of the screen, click the 'Code' button, and then click 'HTTPs'
- Copy the link in this field
- In GitPod, open a new GitBash terminal and go to the directory where you want to find the clone
- On the command line type "git clone", then paste the copied url and press 'Enter'
- The clone process should now begin

## Credits


  ### Code
  
-  '

### Acknowledgements

- 
