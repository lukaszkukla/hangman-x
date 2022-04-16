# HANGMAN-X

[View the live deployment here](https://hangman-x-2022.herokuapp.com/)

[GitHub](https://github.com/lukaszkukla/hangman-x)

# Goal of this project
Welcome to HANGMAN-X. This is na interactive game which runs in Python terminal. It was built using Code Institute [template](https://github.com/Code-Institute-Org/python-essentials-template) which runs in web browser and is deployed on Heroku. 

It is a third project on my journey with [Code Institute](https://codeinstitute.net/ie/) to become a fullstack web developer. It is intended to put my knowledge into practice.

[Hangman game](https://en.wikipedia.org/wiki/Hangman_(game)#:~:text=Though%20the%20origins%20of%20the,to%20fill%20in%20the%20blanks.) requires user to reveal the secret word by guessing the individual letters. Player have 6 attempts per word to beat the game before it will be 'hanged'.

My version of the game calls for random word via API. Player can enter its name and choose between 2 languages. Game continues until user stops, loose all lives or resigns.

For the purpose of testing its functionality user may enter word **'cheat'** to get a hint of the hidden word. This functionality is only for the [Code Institute](codeinstitute.com) testing and grading purposes.

![HANGMAN-X in browser screenshot](docs/screenshots/hangman-x-main-menu-screenshot.jpg "HANGMAN-X in browser screenshot")

# Table of contents

* [UX](#ux "UX")
    * [User goals](#user-goals "User goals")
    * [User stories](#user-stories "User stories")
    * [User requirements and expectations](#user-requirements-and-expectations "user requirements and expectations")
         * [Requirements](#requirements "Requirements")
         * [Expectations](#expectations "Expectations")
         * [Flow chart](#flow-chart "Flow chart")
     * [Design choices](#design-choices "Design choices")
        * [Colors](#colors "Colors")
    * [Features](#features "Features")
        * [Future developments](#future-developments "Future developments")
    * [Technologies used](#technologies-used "Technologies used")
        * [Languages](#languages "Languages")
        * [Libraries and frameworks](#libraries-and-frameworks "Libraries and frameworks")
        * [Tools](#tools "Tools")
    * [Testing](#testing "Testing")
        * [Markup validation](#markup-validation "Markup validation")
        * [CSS validation](#markup-validation "CSS validation")
        * [Python validation](#markup-validation "Python validation")
        * [Images](#images "Images")
        * [Unfixed bugs](#unfixed-bugs "Unfixed bugs")        
    * [Deployment](#deployment "Deployment")
        * [Heroku](#heroku "Heroku deployment")
    * [Cloning repository](#gitpod-terminal-or-local-machine "Cloning repository")
    * [Credits](#credits "Credits")
    
# UX

## User goals
* Intuitive and responsive to user's interaction
* Easily navigated around
* High scores should be stored and accessible to other users to view it

## User stories
As a user, I want to:
* See welcome page with menu option
* Know how the game works (how to)
* See list of 10 best players
* See my score
* Stop game at any time
* Track number of correct guessed words
* See the final score upon game completion
* Change language of guessed words

## User requirements and expectations

### Requirements
* Fetch random words via API call from [Random Word API](https://random-word-api.herokuapp.com/home "Random Word API")
* Language options
* Record player score in [google sheets](https://docs.google.com/spreadsheets/d/1jcsqlHpeQ3zNnlo41blYo2_BDiXg_OEw_oLaPTjD4dM/edit?usp=sharing)
* Visually neat and tidy design

### Expectations
* I expect game to function without any errors
* I expect clear and simple navigation
* I expect appropriate response to user inputs
* I expect words to not to repeat over and over

## Flow chart
In order to meet above requirements and expectations I built flowchart which served me as a road map to successfull completion of the project:

![HANGMAN-X flowchart](docs/screenshots/hangman-x-flowchart.jpg "Game flowchart")

### Language addition
I added extra step in the gameplay where user can now choose between English (default) and Italian language. This is reflected on chart below.

![HANGMAN-X flowchart language addition](docs/screenshots/hangman-x-flowchart-language.jpg "Game flowchart with language added")

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

## Design choices

### Colors

![Color palette](docs/screenshots/color-palette.jpg "Color palette")
 
 * RED = '\033[91m'
 * VIOLET = '\033[95m'
 * BLUE = '\033[94m'
 * CYAN = '\033[96m'
 * GREEN = '\033[92m'
 * YELLOW = '\033[93m'    
 * ORANGE = '\001[32;1m'
 * WHITE = '\033[0m'
 * BOLD = '\033[1m'
 * UNDERLINE = '\033[4m'

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

# Features

## Game template and background
I modified [Code Institute's template](https://github.com/Code-Institute-Org/python-essentials-template "Code Institute's template") for better user experience and visual design. Terminal is centered on the width and there is a custom background behind it.

## Welcome screen
User can access four options from the welcome screen:
1. Start the game
1. How to play
1. Hall of fame
1. Quite game

![Welcome screen](docs/screenshots/hangman-x-main-menu.jpg "HANGMAN-X main menu screen")

## Rules
The rules display information on how game works and wait for user input 'press ENTER to continue...' to get back to main menu.

![Rules screen](docs/screenshots/hangman-x-rules.jpg "HANGMAN-X rules screen")

## Gameplay
- Player is prompted to enter its name at the start of the game
- Player is then given choice between 2 languages of word to be guessed, English (default) and Italian
- Guess word is picked randomly via API call to [Random word API](https://random-word-api.herokuapp.com/home "Random word API"), masked and displayed to user as string of '_' underscores 
- User must enter letters to guess the first and subsequent hidden letters in the game
- User advances to the next word when all the letters of current word has been revealed
- Game ends when:
    - User runs out of tries
    - User choose to not continue after successful word guess
    - User types *'resign'* at any stage during the game
- keyword *'resign'* completes the game in its current state and adds user to the hall of fame if enough points accumulated
- Only the user who accumulates enough points will get an honour to be added to the hall of fame

#### Scoring system
* Each successfuly guessed letter adds 1 point to the final score
* Guessing the whole word add 10 points to the player's score
* Each unsuccessful try cost player 1 point

#### Tries
Player starts game with 6 lives. Each successful guess saves user from losing a life.
Each unsuccessful try will decrease user's life by 1 point and add a body part to the gallows:

* Initial state

![HANGMAN-X gallows initial state](docs/screenshots/hangman-x-gallows-state-001.jpg "HANGMAN-X gallows initial state")

* Head

![HANGMAN-X gallows 5 tries](docs/screenshots/hangman-x-gallows-state-002.jpg "HANGMAN-X gallows with head")

* Head and torso

![HANGMAN-X gallows 4 tries](docs/screenshots/hangman-x-gallows-state-003.jpg "HANGMAN-X gallows with head and torso")

* Head, torso, and one arm

![HANGMAN-X gallows 3 tries](docs/screenshots/hangman-x-gallows-state-004.jpg "HANGMAN-X gallows with head, torso, and one arm")

* Head, torso, and both arms

![HANGMAN-X gallows 2 tries](docs/screenshots/hangman-x-gallows-state-005.jpg "HANGMAN-X gallows with head, torso, and both arms")

* Head, torso, both arms, and one leg

![HANGMAN-X gallows 1 try](docs/screenshots/hangman-x-gallows-state-006.jpg "HANGMAN-X gallows with head, torso, both arms, and one leg")

* Final state: head, torso, both arms, and both legs

![HANGMAN-X gallows final state](docs/screenshots/hangman-x-gallows-state-007.jpg "HANGMAN-X final state gallows with head, torso, both arms, and both legs")

## Error handling

In order to deliver good user experience I ensured that the inalid input from the user is handled correctly and does not crash the game.

### Main menu

* User must enter 1 of the 4 options anything else will trigger warning message

![Main menu error handling](docs/screenshots/hangman-x-main-menu-errors.jpg "Main menu screen error handling")

### Username input

![Username input error handling](docs/screenshots/hangman-x-user-input-error-handling.jpg "Username input error handling")

### Language choice

![Language choice menu error handling](docs/screenshots/hangman-x-language-choice.jpg "Language choice menu error handling")

### Gameplay

* User can only enter letters, numbers and special characters are not allowed and will prompt the user:

![Gameplay error handling](docs/screenshots/hangman-x-gameplay-error-handling.jpg "Gameplay error handling ")

\
&nbsp;

[back to top](#table-of-contents)
\
&nbsp;

## Future developments
* Add 3 difficulty levels:
    * Easy - up to 5 letters
    * Medium - between 6 and 10 letters
    * Hard - 11 to 15 letters
* Add more language options - this also requires different validation for words with spaces and non-english letters
* Allow user to sacrifice some points to reveal 1 random letter per word
* Make it more visually appealing with Colorama library
* Refactor the code and split larger functions into their own files

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

# Technologies used

## Languages
* [HTML](https://en.wikipedia.org/wiki/HTML "HTML")
* [CSS](https://en.wikipedia.org/wiki/CSS "CSS")
* [Python](https://www.python.org/ "Python")

## Libraries and frameworks
* [Google Fonts](https://fonts.google.com/ "Google Fonts")
* [Font Awesome library](https://fontawesome.com/ "Font Awesome")

## Tools
* [Gitpod](https://www.gitpod.io/ "Gitpod")
* [Github](https://www.github.com/ "Github")
* [diagrams.net](https://diagrams.net/ "diagrams.net")
* [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML")
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS")
* [PEP8](http://pep8online.com/ "Python Validator")
* [Autoprefixer](https://autoprefixer.github.io/ "Autoprefixer")
* [Lighthouse](https://developers.google.com/web/tools/lighthouse "Lighthouse")
* [Text to ASCII generator](http://patorjk.com/software/taag/ "taag")
* [Pixabya](https://pixabay.com/ "Pixabay")
* [TinyPNG](https://tinypng.com/ "TinyPNG")
* [Photoshop](https://www.adobe.com/ie/products/photoshop.html "Adobe Photoshop")

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

# Testing
During the development, I tested my game in the terminal of VScode. I also used done it directly in the Code Institute's terminal template after final deployment.

I used print statements for every piece of code that I worked on to test if it is performing as expected. Any bugs were corrected 'on the fly' while building the app.

For the final test I tried each of the menu and game functions and performed below test to ensure correct functionality of the game:
* Entering invalid charcters, multiple characters, blanks(empty or space) and special characters:
    * In main game menu
    * During username input
    * During language choice
    * During the game when guessing the letters
    * In 'play again' menu option after winning and losing the game
* Adding over 100 player names to google sheet file to ensure still sorting and display correctly
* API calls were returning the same word over and over. I moved *'res = requests.get(f'{APIURL}/word')'* into the *get_word()* function and that fixed the problem.
* As a last addition to the game I introduced Italian language. I tested it thoroughly to ensure stable functionality of the game experience. During the testing of German and Spanish language I come accross issues with spaces and language specific letters that require additional time to resolve. I decided to only implement Italian language with this iteration. 

### Markup Validation
I tested my application with [W3C Markup Validation Service](https://validator.w3.org/ "Markup validation service").

### CSS Validation
Subsequently validated my css styles using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS Validation Service").

![CSS Validation](docs/screenshots/css-validation.jpg "validation of the CSS of HANGMAN-X")

### Python Validation
Python code was validated using [PEP8 online](http://pep8online.com/ "PEP8 online").

#### Before

* game.py

![Python Validation](docs/screenshots/python-validation-before.png "Validation of the Python of HANGMAN-X")

#### After
* game.py

![Python Validation](docs/screenshots/python-validation-after-001.png "Validation of the Python of HANGMAN-X")

* utils.py

![Python Validation](docs/screenshots/python-validation-after-002.png "Validation of the Python of HANGMAN-X")

* api.py

![Python Validation](docs/screenshots/python-validation-after-003.png "Validation of the Python of HANGMAN-X")

### Lighthouse

Final testing was performed by Google's [Lighthouse](https://developers.google.com/web/tools/lighthouse "Lighthouse")

![Lighthouse test ](docs/screenshots/lighthouse-desktop-validation.jpg "Lighthouse test")

### Images
All images on the website were compressed using [TinyPNG](https://tinypng.com/ "tinypng.com for image compression")

![TinyPNG image compression results](docs/screenshots/hangman-x-background-optimisation.jpg "Image compression results")

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

## Unfixed bugs
Games is not responsive. It is not recommended to play on mobile devices. The Code Institute's Python terminal emulator is not build to be scaled down to fit small screens.
Also other python files show minor 'trailing whitespace' and 'indentation' errors when checked with PEP8 online. They do not have any impact on functionality of the game and user experience.

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

# Deployment

## Heroku  
  
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
1. Log in to [Heroku](https://id.heroku.com/login) or [sign up](https://signup.heroku.com/login) for free account
1. Click **new** button in the top right corner
1. Select **create new app** from the drop down list
1. Enter a unique app name in the 'App name' input field - green thick will appear to confirm availability
1. Select appropriate **region** to your location from the 'choose a region' drop down list
1. Click **create app** button to proceed
1. 'Deploy' tab will be shown. scroll down to the **config vars** section in the **settings** tab
1. Click **reveal config vars** button
1. Enter **PORT** in the 'KEY' field
1. Enter **8000** in the 'VALUE' filed
1. Click the **add** button
1. Below, in the **buildpacks** section click **add buildpack** button
1. Type and select 'Python' and click 'save changes' button
1. Repeat above step to add 'node.js' pack
\
&nbsp;
   * **IMPORTANT** The buildpacks **must** be in this **particular order**. If they are not, then click and drag to change it
   \
&nbsp;
1. Select **Github** as the deployment method from the **deploy tab**
1. Connect to Github to confirm
1. Type repository name and click **search** button
1. Click **connect** button that appeared next to your repository name
1. Select your preferred deployment type:
   * 'Enable Automatic Deploys' for automatic deployments when you push updates to Github - NOT RECOMMENDED if you have a free account  
   * 'Deploy Branch' for manual deployments - RECOMMENDED for free account users

## Gitpod terminal or local machine
This project was developed using Code Institute's [template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser.
Due to this, I optimized the game to work via the [final Heroku deployment](https://hangman-x-2022.herokuapp.com/), and I do not recommend playing it locally. That said, I have included this section to give you a choice.  

1. Navigate to the [GitHub repository](https://github.com/lukaszkukla/hangman-x), and follow [these steps to clone the project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) into your IDE of choice.   
   
   * **Gitpod** only **requires** you to have the **web extension** installed and **click** the **green Gitpod button** from the repositories main page. If you are **using Gitpod** please **skip step 2** below as you do not require a virtual environment to protect your machine.  
  
1. **Create** the **virtual environment** with the terminal command **"python3 -m venv venv".** Once complete add the "venv" file to you're ".gitignore" file and use the terminal command **"venv\Scripts\activate.bat" to activate it.**
   
   * ***IMPORTANT*** If developing locally on your device, ensure you **set up/activate the virtual environment before installing/generating the requirements.txt file**; failure to do this will pollute your machine and put other projects at 
 
1. **Install the requirements** listed in requirements.txt using the terminal command  **"pip3 install -r requirements.txt"**
   * Kindly note that since I developed the project from scratch and installed the required libraries as progressed **I have already included a requirements.txt for this app** by using the terminal command **"pip3 freeze > requirements.txt"** to generate it.

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

# Credits

* [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin") - for code inspiration, help and advice

* [Sam Timmins](https://github.com/sam-timmins/T4Tri-triathlon-club "Sam Timmins") - for readme template, structure and some ideas that sparked from using it

* [David Bowers](https://github.com/dnlbowers "David Bowers GitHub") - for interesting approaches to some code challenges

* Peer community on [Code Institute](https://codeinstitute.net/ie/) Slack channel

* Kasia_ci from [Code Institute](https://codeinstitute.net/ie/) - for keeping up the spirit and leading weekly standups

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;