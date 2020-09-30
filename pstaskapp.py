from flask import Flask, jsonify, request
from pstaskmodel import TaskModel

app = Flask(__name__)


@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    model = TaskModel()
    tasks = model.get_tasks()
    return jsonify(dict(tasks=tasks))


@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    model = TaskModel()
    task = model.get_task(task_id)
    return jsonify(dict(task=task))


@app.route('/todo/tasks', methods=['POST'])
def create_task():
    title = request.json.get('title')
    description = request.json.get('description', '')
    done = request.json.get('done', False)
    task = [[title, description, done]]
    model = TaskModel()
    model.dump_tasks(task)

    return jsonify(dict(status='success'))


@app.route('/todo/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    model = TaskModel()
    response = model.delete_task(task_id)
    return jsonify(dict(status=response))


if __name__ == '__main__':
    app.run(debug=True)
