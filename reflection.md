# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

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

I used an AI assistant (Claude) to help me find and fix the bugs.

**A time the AI was right:** The AI figured out that the "Too High" and "Too Low" hints were 
backwards. It noticed the code was turning the secret number into text on every other guess, 
which messed up the comparison. It told me to keep the numbers as numbers and clean up the 
check_guess function. I checked this by writing a test that makes sure a high guess says "Go 
LOWER" and a low guess says "Go HIGHER." The test passed, so I knew it worked.

**A time the AI was wrong:** For a while the AI kept thinking my code was broken because the 
game still showed the wrong hints. But the code was actually fine — the real problem was that 
an old version of the game was still running in the background. I found this out by searching 
my files to confirm the code was correct, then closing everything and restarting. After that 
it worked. This taught me not to just trust what the AI says or what the screen shows, and to 
check the actual files myself.

---

## 3. Debugging and testing your fixes

I knew a bug was fixed when two things happened: the game worked right after a fresh restart, 
and my tests passed.

I ran pytest and it ran 6 tests, all passing. Three of them checked my fixes: one made sure 
the hints point the right way, one made sure a wrong guess loses points instead of gaining 
them, and one made sure Hard mode is actually harder than Normal.

The AI helped me with the tests too. The original tests were written expecting check_guess to 
return just a word, but mine returns two things at once, so the AI showed me how to fix that. 
It also helped me when pytest couldn't find my logic file — we added a small conftest.py file 
to fix it.

---

## 4. What did you learn about Streamlit and state?

I'd explain it like this: every time you click a button or type something in Streamlit, the 
whole script runs again from top to bottom — it doesn't just update one part, it reruns 
everything. That's a "rerun." The problem is, if it reruns everything, how does it remember 
your score or the secret number? That's where session state comes in. Session state is like a 
little backpack that holds onto your stuff (your score, your guesses, the secret) so it 
doesn't get wiped every time the script reruns. I actually ran into this myself — an old game 
session got stuck in memory and kept showing me wrong results until I cleared it out and 
started fresh.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is writing tests to prove a fix actually works. It felt way better to 
see "6 passed" than to just guess that my code was right. I'll also keep committing my work to 
Git in steps instead of all at once.

Next time, I'd double-check the AI's claims sooner. We spent a while thinking the code was 
broken when it was really just an old version still running. I should have checked the actual 
files earlier instead of trusting what the screen showed.

This project changed how I see AI-generated code. The AI wrote the original game and swore it 
was "production-ready," but it was full of bugs. Now I know not to trust AI code just because 
it looks finished — you have to actually test it and read it yourself.
