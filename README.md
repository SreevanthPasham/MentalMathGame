# MentalMathGame
A fun and fast-paced **math quiz game** built with **Python (Tkinter)**.  
Players have **30 seconds** to solve as many addition, subtraction, multiplication, and division problems as possible.  
The game tracks your score, displays your problem history, and lets you play again to improve your skills!

---

## Features

- **Random math problems**:
  - Addition & subtraction: numbers between 2–100  
  - Multiplication: 2–12 × 2–100  
  - Division: divisible problems between 2–100 ÷ 2–12
 
- **30-second timer** with progress bar countdown  
- **Automatic answer checking** (no need to press Enter if correct)  
- **Score tracking** with real-time updates  
- **Instant feedback** on each answer  
- **Problem history log** with correct answers and user responses  
- **Replay option** after the game ends

---

## How to Play

1. Launch the game and click **Start Game**.  
2. A math problem will appear — type your answer in the box.  
3. If correct, the game **auto-advances**. You can also press **Submit**.  
4. Keep solving until the **30-second timer** runs out.  
5. When finished:
   - View your **final score**  
   - Review your **problem history**  
6. Click **Play Again** to restart!  

---

## 🛠️ Customization

- Change timer length → update `self.time_left = 30`  
- Adjust number ranges → modify inside `generate_math_problem()`  
- Style the game → edit fonts, widget colors, and layouts in the Tkinter code  

---
