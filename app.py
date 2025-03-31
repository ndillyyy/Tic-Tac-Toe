import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Allow frontend to connect

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

board = [" "]*9
turn = "X"

def check_winner():
    win_patterns = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

@app.route("/move")
def move():
    global turn
    pos = int(request.args.get("pos"))
    
    if board[pos] == " ":
        board[pos] = turn
        winner = check_winner()
        turn = "O" if turn == "X" else "X"
        return jsonify({"player": board[pos], "winner": winner})
    return jsonify({"error": "Invalid move"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use environment variable for port
    app.run(debug=True, host="0.0.0.0", port=port)


