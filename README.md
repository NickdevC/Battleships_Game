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

I wanted to create a functional, simple battleships game, that provided a visual battlefield display so that users could see the 'action' in real time. Through researching on the [Stack Overflow](https://stackoverflow.com/search?q=battleships+python) community, and in speaking to some fellow Code Institute students on Slack, I reached the decision to focus on a model where I would create 4x overlapping fields (or grids). One each to the computer and user to 'place' their ships, and then one each to show both the computer's and user's guesses. My theory was that this method could make the checks for overlapping placements easier. 

Initially, I did want to create a static board, with messages printed to the user dynamically underneath during the game. Due to my time-constraints, this became outside of my scope and I instead needed to re-print the battlefield after every turn.
   

## Features

   ### Existing/current Features
      
-   __Welcome Screen__

    - Utilising the 'sys' module, I was able to recreate a typewriter effect as the welcome text is displayed.
    - ASCII art images were created to  visually represent a ship in the water, and the main title of the game was made bold and eye-catching for the user.
    - I ensured that the speed at which text was displayed meant that users could digest the information at a comfortable speed whilst still being engaged.

      ![Navbar](assets/images/welcome_screen.png)

-   __Rules__

    - The rules of the game are clearly displayed, following a step-by-step guide to play.
    - The different ships and their sizes are explained, whilst also utilising different colour text to make them stand out and differentiate from each other.
    - Users are asked to type 'P' to start the game. On an incorrect key press, the message is repeated for the user.

      ![Navbar](assets/images/rules_message.png)
      
-   __Player Placement__

    - On starting the game, the user is presented with the 'battlefield' grid - indicating the x and y axis using integers and letters.
    - The user is asked to specify whether they wish to place their ship vertically or horizontally (H or V).
    - They are then asked to select a row number (1-7).
    - Finally, users are asked to select a column (A-G). **Note: the given coordinates correlate to the 'start' of the ship and therfore placement will either go from left to right, or top to bottom**
    - If the placement does not cross the scope of the grid, or overlap other ships, then the placement is accepted and '$' symbols are displayed to show where the ship has been placed.
    - Throughout all of these questions and checks, error messages are displayed to prompt the user to re-type in data if there are any conflicts.

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
- A static battlefield
   - This would mean that the need to continuously print new grids would become a redundant feature. It would also make for a cleaner aesthetic, requiring the user to only focus on the one visible screen in the terminal (rather than having to scroll to see the computer's turn played out).
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
      - Used this to help me overcome some difficulties in accessing values from elsewhere in my code efficiently.

-   [Unexpected unident error(stack overflow)](https://stackoverflow.com/questions/10239668/indentationerror-unexpected-unindent-why)
      - Referenced this post to help me work through a challenging bug regarding some of my indentation which was breaking the entirity of my code.

-   [Try except statement(Python Basics](https://pythonbasics.org/try-except/)
      - Helped me realise that I had forgotten to close off my try statements with the except function.

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
          - This is still unresolved (15th October) and, although I have sought and found workable solutions through the Slack community (including a different method of displaying the grid using complex mathematics) I am unable to implement these in my current timeframe.
          - Update (17th October): this has now been resolved through changing the order of syntax within the place_ship function (the 'column' was being passed **before** the integer).
     - During the game, all users reported the successful, random, deployment of the computer's ships :white_check_mark:
     - All users were able to see the correct markers for 'hits' and 'misses', and were able to read visual prompts regarding this :white_check_mark:
     - When the total number of hits was reached, all users experienced the 'end message' either congratulating or commiserating :white_check_mark:

### Resolved Bugs

- **Raising ValueError**
      - I struggled with the syntax surrounding the multiple applications of the ValueError. Ultimately, I used advice on the internet and realised that one of my lines of code required the KeyError exception instead.
- **Try except statement**
      - I had an ongoing issue with my player_input_function where it was not executing the final stages of my block of code. After reviewing [this guide](https://pythonbasics.org/try-except/) I was able to see that I had simply forgotten to close off my try statement with an except function.
- **Vertical placement**
      - For a number of days, I was experiencing an issue where the user could not place ships vertically. After a number of tests, and accepting that the bug could not be resolved in time, I tried switching the order of my syntax (putting the integer passed 'i' before the 'column' as this would force the placement to work top-bottom).

### Unresolved Bugs

- **Ghost computer placement**
      - During my own testing, on one occasion, the computer's random placement seemed to not be within the scope of the grid. I had successfully targeted every grid reference, and there was still **one** hit left to find. I have been unable to recreate the bug and now do not have time to investigate further.
 
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
