# app.py - FIFA World Cup 2026 Predictor (TASK 6 - 15/15)
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
with open('final_model.pkl', 'rb') as f:
    data = pickle.load(f)
    model = data['model']
    scaler = data['scaler']
    features = data['features']
    teams = sorted(data['teams'])

# Load full dataset for real ELO values
df = pd.read_csv('elo_features_O.csv')
df.columns = ['team1', 'team2', 'team1_elo_before', 'team2_elo_before', 'elo_diff_before',
              'expected_team1_win', 'goal_margin_factor', 'team1_elo_after', 'team2_elo_after',
              'elo_change_team1', 'elo_change_team2', 'result_numeric']

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        team_a = request.form['team_a']
        team_b = request.form['team_b']

        # Get average ELO for both teams (from historical matches)
        elo_a = df[df['team1'] == team_a]['team1_elo_before'].mean()
        elo_b = df[df['team2'] == team_b]['team2_elo_before'].mean()

        # Fallback to median if team not found much
        if pd.isna(elo_a): elo_a = df['team1_elo_before'].median()
        if pd.isna(elo_b): elo_b = df['team2_elo_before'].median()

        # Calculate ELO difference (team_a - team_b)
        elo_diff = elo_a - elo_b
        expected_win_a = 1 / (1 + 10 ** (-elo_diff / 400))
        goal_factor = df['goal_margin_factor'].median()

        # Prepare input
        X = np.array([[elo_diff, expected_win_a, goal_factor]])
        X_scaled = scaler.transform(X)

        # Predict
        prob = model.predict_proba(X_scaled)[0]
        pred_class = model.predict(X_scaled)[0]

        # Map prediction
        if pred_class == 1:
            winner = team_a
            confidence = prob[1]
        elif pred_class == 2:
            winner = team_b
            confidence = prob[2]
        else:
            winner = "DRAW"
            confidence = prob[0]

        prediction = {
            'team_a': team_a,
            'team_b': team_b,
            'winner': winner,
            'confidence': round(confidence * 100, 1),
            'team_a_win': round(prob[1] * 100, 1),
            'draw': round(prob[0] * 100, 1),
            'team_b_win': round(prob[2] * 100, 1),
            'elo_a': round(elo_a, 1),
            'elo_b': round(elo_b, 1),
            'elo_diff': round(elo_diff, 1)
        }

    return render_template('index.html', teams=teams, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)