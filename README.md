# football_xg_prediction_model
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

| Metric                | Value                           |
|-----------------------|---------------------------------|
| **Mean Squared Error**| `0.0204` (Low error)            |
| **R-squared (R²)**    | `0.4069` (Explains ~40.7% variance) |
| **Real Match Example 1** | Actual Goals: `2` → Predicted xG: `2.01` ✅ |
| **Real Match Example 2** | Actual Goals: `1` → Predicted xG: `0.54` ⚠ |
| **Real Match Example 3** | Actual Goals: `2` → Predicted xG: `1.93` ✅ |

Even without using the xG column directly, the model successfully learns relationships from other stats that affect scoring potential.

---

## 🌐 API Deployment

This project now includes a working **REST API** built with Flask to make real-time predictions.

### 🔗 How the API Works

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Input:** JSON object with player match stats
- **Output:** Predicted `xG` value

### 🧪 Sample Request (using `curl`)
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
           "Minutes": 90,
           "Assists": 0,
           "Total Shoot": 3,
           "Touches": 78,
           "Carries": 0
      }'
✅ **Sample Response**
{
  "predicted_xG": 0.52
}

## 🛠️ How It Works

1. Loads and preprocesses the dataset
2. Drops unnecessary columns (`Player`, `Position`, actual `xG` from input)
3. Trains a **Gradient Boosting Regressor** on the remaining features
4. Evaluates performance on the test set
5. Predicts xG for real match stats as a test case

---

## 🚀 How to Use

1. Open the notebook in Google Colab or Jupyter
2. Upload or mount your own CSV file (or use the existing one)
3. Run all cells step by step
4. Input a player's match stats to get their predicted xG

---

## 🌟 Why This Project Matters

- ✅ Builds your own logic behind how xG is estimated
- ✅ Mimics real-world football data systems
- ✅ Great foundation for more advanced analytics like goal prediction, overperformance tracking, or player scouting

---

## 🔮 Possible Extensions

- Train a second model to predict **Goals** using your **predicted xG**
- Visualize player overperformance: `Goals - xG`
- Deploy the model as a Flask API **[✅ **Done**]**
- Build a fantasy football helper app using this model

---

## 👤 Author

**Faizan J.**  
BS Software Engineering  
📫 [fazanii092@gmail.com]  



