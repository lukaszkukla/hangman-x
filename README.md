# HANGMAN-X.com 

[view the live site here](https://lukaszkukla)

[github](https://github.com/lukaszkukla/hangman-x)

# goal of this project
Welcome to HANGMAN-X. This is na interactive game which runs in Python terminal. It was built using Code Institute [terminal template](https://github.com/Code-Institute-Org/python-essentials-template) which runs in web browser and deployed on Heroku. 

It is a third project on my journey with [code institute](https://codeinstitute.net/ie/) to become a fullstack web developer. It is intended to put my knowledge into practice.

[Hangman game](https://en.wikipedia.org/wiki/Hangman_(game)#:~:text=Though%20the%20origins%20of%20the,to%20fill%20in%20the%20blanks.) requires user to guess the secret word by guessing the individual letters. Users have 6 attempts per word to beat the game before they will be 'hanged'.

My version of the game shows word category and it allows user to choose between 3 levels of difficutly. Game continues until user stops, loose or guesses all questions from database.

![responisive design](docs/screenshots/responsive-design.jpg "responive design for variouse device sizes")

# table of contents

* [ux](#ux "ux")
    * [user goals](#user-goals "user goals")
    * [user stories](#user-stories "user stories")
    * [user requirements and expectations](#user-requirements-and-expectations "user requirements and expectations")
         * [requirements](#requirements "requirements")
         * [expectations](#expectations "expectations")
         * [flow chart](#flow-chart "flow chart")
     * [design choices](#design-choices "design choices")
        * [fonts](#fonts "fonts")
        * [colors](#colors "colors")
    * [wireframes](#wireframes "wireframes")
    * [features](#features "features")
        * [existing features](#existing-features "existing features")
            * [main game](#main-game "main game")           
        * [future developments](#future-developments "future developments")
    * [technologies used](#technologies-used "technologies used")
        * [languages](#languages "languages")
        * [libraries and frameworks](#libraries-and-frameworks "libraries and frameworks")
        * [tools](#tools "tools")
    * [testing](#testing "testing")
        * [images](#images "images")
        * [during testing](#during-testing "during testing") 
        * [unfixed bugs](#unfixed-bugs "unfixed bugs")        
    * [deployment](#deployment "deployment")
        * [Heroku](#Heroku-deployment "heroku deployment")
    * [cloning repository](#cloning-repository "cloning repository")
    * [credits](#credits "credits")
    
# ux

## user goals
* intuitive and responsive to user's interaction
* easily navigated around
* choice of difficulty levels
* high scores should be stored and accessible to other users to view it

## user stories
* as a user, I want to see welcome page with menu option
* as a user, I want to know how the game works (help)
* as a user, I want to see list of 10 best players
* as a user, I want to be able to choose difficulty level
* as a user, I want to know word category
* as a user, I want to see my score
* as a user, I want to stop game at any time
* as a user, I want to track number of correct guessed words
* as a user, I want to see the final score upon game completion

## user requirements and expectations

### requirements
* fetch data from [google sheets](https://docs.google.com/spreadsheets/d/1jcsqlHpeQ3zNnlo41blYo2_BDiXg_OEw_oLaPTjD4dM/edit?usp=sharing) - read only access
* randomise questions on reload
* visually neat and tidy design

### expectations
* I expect game to function without any errors
* I expect clear and simple navigation
* I expect appropriate response to user inputs
* I expect words to not to repeat over and over

## flow chart
In order to meet above requirements and expectations I built flowchart which served me as a road map to successfull completion of the project:

![HANGMAN-X flowchart](docs/wireframes/HANGMAN-X-flowchart.jpg "game flowchart")

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

## design choices

### fonts
I used [Google Fonts](https://fonts.google.com/ "Google Fonts"). The font used for the entire website is [Poppins](https://fonts.google.com/specimen/Roboto+Slab?query=rob "Poppins"). 

The use of **small caps** on the website is **intentional** and is part of the design. This also applies to readme.md file.

### colors

![color Pallete](docs/screenshots/color-pallette.jpg)
 
 * white: #fff; - main font color

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

# wireframes
I use [diagrams.net](https://www.diagrams.net/ "diagrams.net") to develop wireframes for the website. 

The wireframe of pages below:

* game screen wireframes
\
&nbsp;

![index page](docs/wireframes/HANGMAN-X-wireframes.jpg "game screens wireframes")

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

# features

## welcome screen
user can access four options from the welcome screen:
1. start the game
1. how to play
1. hall of fame
1. quite game

![welcome screen](docs/wireframes/HANGMAN-X-welcome.jpg "HANGMAN-X welcome screen")

### welcome screen error handling
* user must enter 1 of the 4 options anything else will trigger warning message

![welcome screen error handling](docs/wireframes/HANGMAN-X-welcome.jpg "HANGMAN-X welcome screen error handling")

### rules
the rules are broken into 2 screens with 'press any key to continue...' in between

![rules screen 1/2](docs/wireframes/HANGMAN-X-rules-001.jpg "HANGMAN-X rules screen 1/2")


![rules screen 2/2](docs/wireframes/HANGMAN-X-rules-002.jpg "HANGMAN-X rules screen 2/2")

### gameplay
- user can choose the difficulty level upon game startup
- guess words are picked from database based on the difficulty level in the previous step and their order is shuffled
- user must enter letters to guess the first and subsequent words in the game
- user advances to the next word when all letters of current has been revealed
- game ends when:
    - user runs out of tries
    - user guess all available words from the database
    - user types 'done' at any stage during the game
- keyword 'done' completes the game in its current state and adds user to the hall of fame if enough points accumulated
- only the user who accumulates enough points will get an honour to be added to the hall of fame and will be prompted to add her/his name at the end of the game - this is design from old arcade games of 80's and 90's ;-)

#### tries
each missed letter will decrease user's life by 1 point and add another body part to the gallow:

* initial state
![HANGMAN-X gallow initial state](docs/wireframes/HANGMAN-X-gallow-state-001.jpg "HANGMAN-X gallow initial state")

* head

![HANGMAN-X gallow 5 tries](docs/wireframes/HANGMAN-X-gallow-state-002.jpg "HANGMAN-X gallow with head")

* head and torso

![HANGMAN-X gallow 4 tries](docs/wireframes/HANGMAN-X-gallow-state-003.jpg "HANGMAN-X gallow with head and torso")

* head, torso, and one arm

![HANGMAN-X gallow 3 tries](docs/wireframes/HANGMAN-X-gallow-state-004.jpg "HANGMAN-X gallow with head, torso, and one arm")

* head, torso, and both arms

![HANGMAN-X gallow 2 tries](docs/wireframes/HANGMAN-X-gallow-state-005.jpg "HANGMAN-X gallow with head, torso, and both arms")

* head, torso, both arms, and one leg

![HANGMAN-X gallow 1 try](docs/wireframes/HANGMAN-X-gallow-state-006.jpg "HANGMAN-X gallow with head, torso, both arms, and one leg")

* final state: head, torso, both arms, and both legs

![HANGMAN-X gallow final state](docs/wireframes/HANGMAN-X-gallow-state-007.jpg "HANGMAN-X final state gallow with head, torso, both arms, and both legs")

#### error handling
- user can only enter letters, numbers and special characters are not allowed and will prompt the user:

![gameplay error handling](docs/wireframes/HANGMAN-X-gameplay-error-handling-001.jpg "gameplay error handling ")
\
&nbsp;

[back to top](#table-of-contents)
\
&nbsp;

## future developments

* extend categories and words in the database 
* allow user to choose category
* make it more visually appealing with Colorama library

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

# technologies used

## languages
* [HTML](https://en.wikipedia.org/wiki/HTML "HTML")
* [CSS](https://en.wikipedia.org/wiki/CSS "CSS")
* [Python](https://www.python.org/ "Python")

## libraries and frameworks
* [Google Fonts](https://fonts.google.com/ "Google Fonts")
* [Font Awesome library](https://fontawesome.com/ "Font Awesome")

## tools
* [Gitpod](https://www.gitpod.io/ "Gitpod")
* [Github](https://www.github.com/ "Github")
* [diagrams.net](https://diagrams.net/ "diagrams.net")
* [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML")
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS")
* [PEP8](http://pep8online.com/ "Python Validator")
* [autoprefixer](https://autoprefixer.github.io/ "autoprefixer")
* [lighthouse](https://developers.google.com/web/tools/lighthouse "lighthouse")
* [text to ASCII generator](http://patorjk.com/software/taag/ "taag")
* [Enchanted Learning](https://www.enchantedlearning.com/wordlist/ "word lists")
* [vecteezy](https://www.vecteezy.com/ "vecteezy")
* [WebFX](https://www.webfx.com/web-design/color-picker/F1F1F1/ "WebFX color scheme generator")
* [TinyPNG](https://tinypng.com/ "TinyPNG")
* [Photoshop](https://www.adobe.com/ie/products/photoshop.html "Adobe Photoshop")

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

# testing

I used print statements for every piece of code that I worked on to test if it is performing as expected. Any bugs were corrected 'on the fly' while building the app

### Markup Validation
I tested my application with [W3C Markup Validation Service](https://validator.w3.org/ "Markup validation service").


![Markup Validation](docs/screenshots/markup-validation.jpg "validation of the markup of HANGMAN-X")

### CSS Validation
Subsequently validated my css styles using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS Validation Service").

![CSS Validation](docs/screenshots/css-validation.jpg "validation of the CSS of HANGMAN-X")

### Python Validation
Python code was validated using ![Python Validation](docs/screenshots/python-validation.jpg "validation of the Python code of HANGMAN-X")

### Accessibility Validation
Accessibility test was done via [experte.com](https://www.experte.com/accessibility "accessibility testing").

![Accessibility Test Initial](docs/screenshots/accessibility-validation.jpg "accessibility test of HANGMAN-X").

### Lighthouse

Final testing was performed by Google's [Lighthouse](https://developers.google.com/web/tools/lighthouse "lighthouse")

![lighthouse test ](docs/screenshots/lighthouse-desktop-validation.jpg "lighthouse test")

### Images
All images on the website were compressed using [TinyPNG](https://tinypng.com/ "tinypng.com for image compression")

![TinyPNG image compression results](docs/screenshots/background-optimised-tinyPNG.jpg "image compression results")

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

## unfixed bugs
Games is not responsive. It is not recommended to play on mobile devices. The Code Institute's Python terminal emulator is not build to be scaled down to fit small screens

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;

# deployment
## Heroku deployment  
  
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
1. log in to [Heroku](https://id.heroku.com/login) or [sign up](https://signup.heroku.com/login) for free account
1. click **new** button in the top right corner
1. select **create new app** from the drop down list
1. enter a unique app name in the 'App name' input field - green thick will appear to confirm availability
1. select appropriate **region** to your location from the 'choose a region' drop down list
1. click **create app** button to proceed
1. 'deploy' tab will be shown. scroll down to the **config vars** section in the **settings** tab
1. click **reveal config vars** button
1. enter **PORT** in the 'KEY' field
1. enter **8000** in the 'VALUE' filed
1. click the **add** button
1. below, in the **buildpacks** section click **add buildpack** button
1. type and select 'Python' and click 'save changes' button
1. repeat above step to add 'node.js' pack
\
&nbsp;
   * **IMPORTANT** The buildpacks **must** be in this **particular order**. If they are not, then click and drag to change it
   \
&nbsp;
1. select **Github** as the deployment method from the **deploy tab**
1. connect to Github to confirm
1. type repository name and click **search** button
1. click **connect** button that appeared next to your repository name
1. select your preferred deployment type:
   * 'Enable Automatic Deploys' for automatic deployments when you push updates to Github - NOT RECOMMENDED if you have a free account  
   * 'Deploy Branch' for manual deployments - RECOMMENDED for free account users

## Gitpod terminal or local machine
This project was developed using Code Institute's [template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser.
Due to this, I optimized the game to work via the [final Heroku deployment](https://dnlbowers-battleship.herokuapp.com/), and I do not recommend playing it locally. That said, I have included this section to give you a choice.  

1. Navigate to the [GitHub repository](https://github.com/dnlbowers/battleships), and follow [these steps to clone the project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) into your IDE of choice.   
   
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

# credits

* [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin") - for code inspiration, help and advice

* [Sam Timmins](https://github.com/sam-timmins/T4Tri-triathlon-club "Sam Timmins") - for readme template, structure and some ideas that sparked from using it

* peer community on [code institute](codeinstitute.com) slack channel

* kasia_ci from [code institute](codeinstitute.com) - for keeping up the spirit and leading weekly standups

\
&nbsp;
[back to top](#table-of-contents)
\
&nbsp;