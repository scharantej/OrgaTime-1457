
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample data objects
tasks = [
    {'id': 1, 'name': 'Task 1', 'deadline': '2023-03-08', 'time_slots': ['09:00-10:00', '14:00-15:00']},
    {'id': 2, 'name': 'Task 2', 'deadline': '2023-03-15', 'time_slots': ['10:00-11:00', '16:00-17:00']},
    {'id': 3, 'name': 'Task 3', 'deadline': '2023-03-22', 'time_slots': ['11:00-12:00', '17:00-18:00']}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/addTask', methods=['POST'])
def addTask():
    task_name = request.form['task_name']
    deadline = request.form['deadline']
    time_slots = request.form.getlist('time_slots')

    new_task = {
        'id': len(tasks) + 1,
        'name': task_name,
        'deadline': deadline,
        'time_slots': time_slots
    }

    tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/viewSchedule')
def viewSchedule():
    return render_template('viewSchedule.html', tasks=tasks)

@app.route('/deleteTask/<int:task_id>')
def deleteTask(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            break
    return redirect(url_for('index'))

@app.route('/updateTask/<int:task_id>', methods=['POST'])
def updateTask(task_id):
    task_name = request.form['task_name']
    deadline = request.form['deadline']
    time_slots = request.form.getlist('time_slots')

    for task in tasks:
        if task['id'] == task_id:
            task['name'] = task_name
            task['deadline'] = deadline
            task['time_slots'] = time_slots
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
