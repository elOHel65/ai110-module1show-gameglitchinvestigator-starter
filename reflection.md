# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
when i first ran the game i noticed the an attempt was already documented when I never submitted a guess. So the attempt counter started at 1 instead of 0. 

- List at least two concrete bugs you noticed at the start  
hints were backwards
I got rewarded points for guessing wrong. 

  

**Bug Reproduction Log**

input used :  expected behavior  : actual behavior : console error output :
guessed 70  |  game should tell |  game tells me to|  none 
when seceret|  me to go lower   |   to go higher   |
number is   |
56.         |
used same   |  game should not  |  Increased my   | none 
input       |increase score for | points from     |
            | for wrong guessing| 0 to 5          | 

 used 40   | game should tell me| game displayed  |         
           | to go higher       | to go lower     | none 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used chatgpt 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  One AI suggestion that was correct was moving the check_guess function from app.py into logic_utils.py and fixing the reversed hint messages. The AI suggested that a guess that was too high should tell the player to go lower, and a guess that was too low should tell the player to go higher. I verified this by running the pytest tests and by manually entering guesses above and below the secret number in the Streamlit game

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

One AI suggestion I did not accept as complete was the scoring refactor. The AI said the scoring changes were working and that the tests passed, but when I tested the live game, a correct guess was still being treated as incorrect and the score decreased. I investigated the code and found that app.py was converting the secret number into a string on alternating attempts. I changed the code so the secret stayed as an integer. I then ran the tests again and manually tested the game to verify that a correct guess registered as a win and increased the score.
---

## 3. Debugging and testing your fixes

I decided a bug was really fixed only after I tested it myself. I did not rely only on the AI saying the code was correct. I used both pytest and manual testing in the Streamlit game to make sure the behavior matched what I expected.

One test I ran was `python3 -m pytest`. After the scoring tests were added, all 136 tests passed. These tests showed that the `check_guess` and `update_score` functions were working correctly for different inputs. For example, the tests checked that incorrect guesses did not increase the score.

I also manually tested the game in Streamlit. I checked that a guess above the secret number told me to go lower, a guess below the secret told me to go higher, and the correct number registered as a win. Manual testing helped me find a problem that the automated tests did not catch: the secret number was sometimes being converted into a string, which caused a correct guess to be treated as incorrect.

AI helped me understand and design the tests by suggesting pytest cases for the game logic and scoring functions. It also helped explain what each test was checking. However, I still ran the tests myself and tested the full application manually because passing automated tests did not always mean the entire Streamlit game worked correctly.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? 
## 4. What did you learn about Streamlit and state?

Streamlit reruns the Python file from top to bottom whenever the user interacts with the app. Session state is used to save values like the score, attempts, secret number, and history so they do not reset every time the app reruns.

I also learned that the order of the code matters. If information is displayed before session state is updated, the screen can show old values until the next interaction.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to make sure I get used to testing and retesting what im running. Im new to vsCode so its kind of a big jargin of things to do on here that im getting used to but the more I practice and interact with my labs I think it will come second hand.
  
- What is one thing you would do differently next time you work with AI on a coding task? 
the one thing ill do differently is have my WSL open when i first began I wasnt in  WSL at all for some reason But i did have the wsl Terminal open.
- In one or two sentences, describe how this project changed the way you think about AI generated code. 
I Cant thank AI enough for helping me do this project. Its super helpful and direct its basically like plug and play all you have to really do is follow directions.
