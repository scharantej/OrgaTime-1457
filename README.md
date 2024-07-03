## Flask Application Design for Smart Time

### HTML Files

**index.html:**
- Main page for the app.
- Contains the form for creating and managing tasks.
- Displays the user's schedule.

**addTask.html:**
- Form for adding a new task to the schedule.
- Includes fields for task name, deadline, and time slots.

**viewSchedule.html:**
- Displays the user's schedule in a calendar format.
- Allows the user to view tasks and deadlines.

### Routes

**@app.route('/')**
- Serves the **index.html** page.

**@app.route('/addTask', methods=['POST'])**
- Accepts form data from **addTask.html** to create a new task.
- Adds the task to the database and redirects to the **index.html** page.

**@app.route('/viewSchedule')**
- Serves the **viewSchedule.html** page.

**@app.route('/deleteTask/<int:task_id>')**
- Deletes a task with the specified **task_id** from the database and redirects to the **index.html** page.

**@app.route('/updateTask/<int:task_id>', methods=['POST'])**
- Updates a task with the specified **task_id** in the database and redirects to the **index.html** page.