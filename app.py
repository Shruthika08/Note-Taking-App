from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note.strip():
            notes.append(note)
    return render_template("home.html", notes=notes)

@app.route('/delete/<int:index>', methods=["POST"])
def delete(index):
    del notes[index-1]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
