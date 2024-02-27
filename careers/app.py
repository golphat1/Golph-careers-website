from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Nairobi, Kenya',
        'salary': 'ksh. 350,000'
    },
    {
        'id': 2,
        'title': 'Data Analyst',
        'location': 'Kampala, Uganda',
        'salary': 'ush. 5,000,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Califonia, USA'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Kingstone, Jamaica',
        'salary': '$ 3000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Golph')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
