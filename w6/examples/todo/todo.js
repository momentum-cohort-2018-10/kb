function q (selector) {
  return document.querySelector(selector)
}

const todoItems = []

function addNewTodo (event) {
  let todoField = q('#new-todo-field')
  let newTodo = todoField.value
  let todoList = q('#todo-list')
  let newListItem = document.createElement('li')
  newListItem.classList.add('todo')
  newListItem.addEventListener('dblclick', toggleTodo)
  newListItem.innerText = newTodo
  newListItem.style.cursor = 'pointer'
  todoItems.push(newTodo)
  todoList.appendChild(newListItem)
  todoField.value = ''
}

function toggleTodo (event) {
  let target = event.target
  target.classList.toggle('strike')
}

q('#add-todo').addEventListener('click', addNewTodo)
q('#new-todo-field').addEventListener('keyup', function (event) {
  if (event.keyCode === 13) {
    addNewTodo()
  }
})

// document.addEventListener('keyup', function (event) {
//   if (event.keyCode === 13) {
//     addNewTodo()
//   }
// })
