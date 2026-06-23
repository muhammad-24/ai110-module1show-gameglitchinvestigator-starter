# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

## 1. What was broken when you started?

When I first ran the game it looked normal — a number guessing game with a text input, 
submit button, and difficulty selector. But after playing a couple rounds, things felt off.
The hints were misleading me and my score was changing in ways that didn't make sense.

### Bugs I found:

1. **Wrong hints on even attempts** — The game told me "Go Lower" when the secret number 
   was actually higher than my guess. This happened because the code converts the secret 
   number to a string on every even attempt, breaking the comparison logic.

2. **Hard mode is easier than Normal** — Selecting "Hard" gives a range of 1–50, which is 
   actually easier than Normal's range of 1–100. The difficulty ranges are not ordered correctly.

3. **Score increases on wrong guesses** — On every even-numbered attempt, a wrong "Too High" 
   guess awards +5 points instead of subtracting points. Wrong guesses should never increase 
   your score.

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|---|---|---|---|
| Guess 40, secret 50, attempt 2 | Show "Go Higher" | Showed "Go Lower" | none |
| Select "Hard" difficulty | Range 1–200 (harder) | Range is 1–50 (easier than Normal) | none |
| Wrong guess on attempt 2 | Score decreases | Score increased by +5 | none |

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
