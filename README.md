# Football xG Prediction Model
# ⚽ Predicting Expected Goals (xG) from Football Match Stats Using Machine Learning

## 📌 About the Project

Expected Goals (`xG`) is one of the most important metrics in modern football analytics. It estimates the likelihood of a player scoring based on the quality of their chances. Football platforms like SofaScore, FotMob, and Understat use proprietary models to calculate it — but in this project, I set out to **build my own xG predictor using raw match data only**.

This model learns how to predict xG values for individual player performances using stats like shots, touches, assists, and minutes — **without using xG as an input**. The goal is to simulate how real-world platforms generate xG behind the scenes.

---

## 📊 Dataset

- Format: `.csv` file containing player match-by-match statistics  
- Features: `Shots`, `Touches`, `Carries`, `Key Passes`, `Assists`, `Minutes`, etc.  
- Target: `Expected Goals (xG)`  
- Source: Manually compiled + cleaned data  

---

## 🤖 Machine Learning Approach

- **Model:** Gradient Boosting Regressor  
- **Train/Test Split:** 80/20  
- **Libraries:** scikit-learn, pandas, seaborn, matplotlib  
- **Platform:** Google Colab (with Google Drive integration)  

---

## 📈 Results Achieved

The model was evaluated using real match scenarios and the results are very promising:

| Metric                | Value                                |
|-----------------------|--------------------------------------|
| **Mean Squared Error**| `0.0204` (Low error)                 |
| **R-squared (R²)**    | `0.4069` (Explains ~40.7% variance)  |
| **Real Match Example 1** | Actual Goals: `2` → Predicted xG: `2.01` ✅ |
| **Real Match Example 2** | Actual Goals: `1` → Predicted xG: `0.54` ⚠ |
| **Real Match Example 3** | Actual Goals: `2` → Predicted xG: `1.93` ✅ |

Even without using the xG column directly, the model successfully learns relationships from other stats that affect scoring potential.

---

## 🌐 Live API Demo

You can test the trained xG model using a public Flask-based API.

🔗 **Live URL:**  
[https://7d5ea032-fbbf-4953-9cd7-d8ac39c8a33b-00-1mvj8t1y36w8k.pike.replit.dev](https://7d5ea032-fbbf-4953-9cd7-d8ac39c8a33b-00-1mvj8t1y36w8k.pike.replit.dev)

### 📮 Endpoint: `POST /predict`

Send match stats as JSON to get predicted xG.

#### ✅ Example Request:
<pre>
```json
{
  "shots": 12,
  "passes": 500,
  "possession": 55.3,
  "fouls": 9,
  "corners": 4
}
🔁 Example Response:
json
Copy
Edit
{
  "predicted_xG": 2.18
}
### 🧪 Test with curl:
bash
Copy
Edit
curl -X POST https://7d5ea032-fbbf-4953-9cd7-d8ac39c8a33b-00-1mvj8t1y36w8k.pike.replit.dev/predict \
  -H "Content-Type: application/json" \
  -d '{"shots": 12, "passes": 500, "possession": 55.3, "fouls": 9, "corners": 4}'
  ```
</pre>

### 🛠️ How It Works
Loads and preprocesses the dataset

Drops unnecessary columns (Player, Position, actual xG from input)

Trains a Gradient Boosting Regressor on the remaining features

Evaluates performance on the test set

Predicts xG for real match stats as a test case

### 🚀 How to Use
Open the notebook in Google Colab or Jupyter

Upload or mount your own CSV file (or use the existing one)

Run all cells step by step

Input a player's match stats to get their predicted xG

### 🌟 Why This Project Matters
✅ Builds your own logic behind how xG is estimated

✅ Mimics real-world football data systems

✅ Great foundation for more advanced analytics like goal prediction, overperformance tracking, or player scouting

### 🔮 Possible Extensions
Train a second model to predict Goals using your predicted xG

Visualize player overperformance: Goals - xG

Deploy the model as a Flask API ✅ Done

Build a fantasy football helper app using this model

### 👤 Author
Faizan J.
BS Software Engineering
📫 fazanii092@gmail.com
