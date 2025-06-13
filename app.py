from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# GOAT Comparison Page
@app.route('/goat')
def goat():
    return render_template('goat.html')

# Trophy Cabinet Page
@app.route('/trophies')
def trophies():
    return render_template('trophies.html')

# Career Timeline Page
@app.route('/career')
def career():
    return render_template('career.html')

# Records & Legendary Moments Page
@app.route('/records')
def records():
    return render_template('records.html')

# Wallpapers & Fan Gallery Page
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# FunZone Quiz + Vote Tracker
votes = {"ronaldo": 0, "messi": 0}

@app.route('/funzone', methods=['GET', 'POST'])
def funzone():
    score = None
    vote_stats = None

    if request.method == 'POST':
        # Handle quiz answers
        answers = {
            'q1': 'sporting',
            'q2': '5',
            'q3': '2008',
            'q4': 'messi',
            'q5': 'portugal'
        }
        user_answers = {q: request.form.get(q, '').strip().lower() for q in answers}
        score = sum(user_answers[q] == a for q, a in answers.items())

    if sum(votes.values()) > 0:
        total_votes = votes["ronaldo"] + votes["messi"]
        vote_stats = {
            "ronaldo": round((votes["ronaldo"] / total_votes) * 100, 1),
            "messi": round((votes["messi"] / total_votes) * 100, 1)
        }

    return render_template("funzone.html", score=score, vote_stats=vote_stats)

# Vote submission endpoint
@app.route('/vote', methods=['POST'])
def vote():
    selected = request.form.get('vote')
    if selected in votes:
        votes[selected] += 1
    return redirect(url_for('funzone'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
