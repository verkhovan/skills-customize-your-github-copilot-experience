# 📘 Assignment: Interactive Web Pages

## 🎯 Objective

Build an interactive to-do list web page using HTML, CSS, and JavaScript. In this assignment, you will structure a page with HTML, style it with CSS, and use DOM manipulation to make it respond to user actions.

## 📝 Tasks

### 🛠️ Structure the Page with HTML

#### Description
Create the HTML skeleton for a to-do list app with an input field, a button to add tasks, and an area to display the task list.

#### Requirements
Completed program should:

- Include a text `<input>` element for typing a new task
- Include a button labeled **Add Task** that the user can click
- Include an empty `<ul>` or `<ol>` element where tasks will be displayed
- Use semantic HTML elements (`<header>`, `<main>`, `<section>`) to organise the page


### 🛠️ Style the Page with CSS

#### Description
Apply CSS to make the to-do list visually clear and easy to use.

#### Requirements
Completed program should:

- Center the app on the page with a readable max-width
- Style the input and button so they appear on the same line
- Give each task item a distinct look (border, padding, or background color)
- Change the button's appearance on hover to indicate it is clickable


### 🛠️ Add Interactivity with JavaScript

#### Description
Write JavaScript to allow users to add new tasks to the list and mark them as complete by clicking on them.

#### Requirements
Completed program should:

- Add a new `<li>` task to the list when the **Add Task** button is clicked
- Clear the input field after a task is added
- Prevent adding an empty task (ignore clicks when the input is blank)
- Toggle a visual "completed" style (e.g. strikethrough text) when a task item is clicked
