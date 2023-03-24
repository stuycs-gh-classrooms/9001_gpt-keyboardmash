# ChatGPT on Graphics

### Name0: YOUR NAME HERE
### Name1: TABLE_BUDDY NAME HERE
### Name2: TABLE_BUDY+ NAME HERE 
### Name3: TABLE_BUDY+ NAME HERE (if applicable, delete this line if not)

---

## Background
Your goal is to get ChatGPT to create a program that meets all the requirements of our graphics engine up to the latest assignment. This includes:
* Drawing lines
* Drawing circles, and Bezier and Hermite curves.
* Maintining an edge list of points.
* Being able to perform & potentially combine transformations, rotations and dilations.
* Being able to save and display the images.
* Being able to correctly read in files using the graphics scripting language we've developed.

Some Notes:
* Please stick to C, Python or Java as the language of choice.
* Don't let ChatGPT use an existing graphics engine, it's got to work as hard as you have!
* If the program has multiple files, feel free to get ChatGPT to create a makefile for you.
* If you get it to create a useable grpahics engine, see if it can generate an image that shows off its capabilities.



## Task 0: Setup
Only one member of your group needs to have an account to use ChatGPT, if someone has one already, go ahead and use that. If not, pick one person to sign up, the simplest method to sign up would be to authenticate with google and use your stuy.edu email address. Authentication will require recieving a text message, so pick someone that has easy access to their phone.

You can find ChatGPT here: <https://chat.openai.com/chat>

## Task 1: The First Program
### Your Prompt
Provide below the first description you gave ChatGPT:

You are writing a graphics engine from scratch with no libraries in python. It should be able to draw lines, circles, bezier curves, hermite curves, maintain an edge list of points, perform transformations, rotations, and dilations, be able to save and display images. Create a makefile to run the program. Give the code required for this.

Write the code for the canvas implementation

Write a simple program using the code above to draw a single line


### The Code
Crate a folder in this repository called __0-program__ containing all the relevant code initially created by ChatGPT.

### Your Analysis
Answer the Following Questions after seeing the initial program.

#### Question 0
Overall, how well did ChatGPT do?

90/100

#### Question 1
What did ChatGPT get right?
  - drawing pixels & coloring
  - The line algorithm
  - the main file, draw file, and canvas file (after asking)
  - the code for the macros (like it referenced (after asking)
  - the bezier & hermite curve algorithms
  - image save & display
  
#### Question 2
What did ChatGPT get wrong?
  - Line alg had wrong parameters (had to be fixed manually by Paul)
  - didn't give code for some of the macros
  - no main file

#### Question 3:
How much of the code generated by ChatGPT do you understand?
  - Everything, all the functions are appropriately named.

#### Question 4:
How does ChatGPT's approach differe from yours?

  - It doesn't use the edge matrix when it draws.
  - Also, it uses class.


## Task 2: Refinement
if possible, run the code made by ChatGPT. Based on your answers the questions above, and your observations about how the program runs, ask ChatGPT to improve the code. ChatGPT will generally understand that you are asking to make changes to your inital prompt, so you don't need to restate the enire problem, instead, ask for specific changes or improvements.

Provide each prompt you gave ChatGPT bellow. Give each prompt a header like this :`#### Prompt X` where X is a counter starting at 1.
#### Prompt 1

#### Prompt 2

#### Prompt 3

#### Prompt 4

etc

## Task 3: The Final Program
Include the final program created by ChatGPT in this repository in a folder called __1-program__.



