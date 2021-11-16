from flask import Flask, jsonify

app = Flask(__name__)


users = [
    {
        'id': "1",
        'name': "Sanat Mondal",
        'emp_id': "20170546",
        'dept': "IT",
        'des': "Asst Manager",
        'salary': "20000"
    }, {
        'id': "2",
        'name': "Badal Biswas",
        'emp_id': "20181010",
        'dept': "IT",
        'des': "Asst Manager",
        'salary': "30000"
    }, {
        'id': "3",
        'name': "Sonjoy Day",
        'ID': "20170546",
        'Dept': "IT",
        'salary': "25000"
    }, {
        'id': "4",
        'name': "AlimUddin",
        'emp_id': "20150551",
        'dept': "IT",
        'des': "Manager",
        'salary': "22000"
    }
]


@app.route('/')
def index():
    return "hello api"


@app.route("/users", methods=['GET'])
def get_users():
    return jsonify({'Users:': users})


@app.route("/get_user_by_index/<int:index>", methods=['GET'])
def get_user_by_index(index):
    return jsonify({'Users:': users[index]})


if __name__ == "__main__":
    app.run(debug=True)

