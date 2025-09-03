# 🔐 Code Vault

An interactive Streamlit app designed for Mathayom 1–3 students to practice combinatorics (combinations and permutations) by solving multi-step code puzzles.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://code-vault.streamlit.app)

---

## 🎓 About

Code Vault is a classroom-friendly challenge that helps students:

- Practice multiplying combination counts
- Understand character-based codes and constraints
- Learn through gamified problem solving

It’s designed to be paired with a printable worksheet for offline calculation before checking answers in the app.

---

## 📋 How It Works

1. Students receive 5 math problems on a worksheet.
2. They calculate the total number of possible code combinations for each.
3. They enter the results into the app to attempt to unlock the vault.
4. If all answers are correct, the vault opens with a final code word.

---

## 📝 Worksheet

The Code Vault app is intended to be used alongside this printable worksheet:

📄 [**Download the Worksheet**](./worksheet.md)

The worksheet includes:

- 5 challenge problems
- Clear restrictions per puzzle
- Hints for each problem
- Encouragement to use logical multiplication

---

## 🖼️ Visual Aids

The app and worksheet include character-length images to help students visualize the codes:

- `3char.png` – for 3-character codes  
- `4char.png` – for 4-character codes  
- `5char.png` – for 5-character codes  

---

## 🚀 Running Locally

```bash
pip install streamlit qrcode pillow
streamlit run streamlit-app.py
```

## File Structure
```plaintext
/code-vault
├── app.py              # Main Streamlit app
├── worksheet.md        # Companion worksheet for students
├── 4char.png           # Visual aid for 4-character codes
├── 5char.png           # Visual aid for 5-character codes
```
---

## License

MIT License.
Feel free to use and adapt for classrooms or educational purposes.
