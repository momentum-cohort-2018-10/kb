/* globals $ */

const username = 'clinton!'
const password = 'password'

$.ajaxSetup({
  headers: {
    'Authorization': 'Basic ' + window.btoa(username + ':' + password)
  }
})

function noteHTML (note) {
  return `
  <article id="note-${note._id}" class="center mw5 mw6-ns br3 hidden ba b--black-30 mv4">
    ${note.title
    ? `<h1 class="f4 bg-moon-gray br3 br--top black-60 mv0 pv2 ph3">${note.title}</h1>`
    : ''}    
    <div class="pa3 bt b--black-10">
      <p class="f6 f5-ns lh-copy measure">
        ${note.text}
      </p>
    </div>
    <div class="f4 bg-near-white br3 br--bottom black-60 mv0 pv2 ph3">
      <button data-note-id="${note._id}" class="delete-note-button f6 link dim br2 ph3 pv2 mb2 dib white bg-dark-red">Delete note</button>
    </div>
  </article>
  `
}

function loadNotes () {
  $.ajax({
    method: 'GET',
    url: 'https://notes-api.glitch.me/api/notes',
    success: function (result) {
      for (let note of result.notes) {
        let html = noteHTML(note)
        $('#notes').append(html)
      }
    }
  })
}

function deleteNote (noteId) {
  $.ajax({
    url: `https://notes-api.glitch.me/api/notes/${noteId}/`,
    method: 'DELETE',
    success: function (result) {
      $(`#note-${noteId}`).remove()
    }
  })
}

$('#new-note-form').on('submit', function (event) {
  event.preventDefault()
  const noteTitle = $('#new-note-title').val()
  const noteText = $('#new-note-text').val()

  $.ajax({
    method: 'POST',
    url: 'https://notes-api.glitch.me/api/notes',
    data: JSON.stringify({
      'title': noteTitle,
      'text': noteText
    }),
    contentType: 'application/json; charset=utf-8',
    success: function (result) {
      const html = noteHTML(result)
      $('#new-note-title').val('')
      $('#new-note-text').val('')
      $('#new-note-container').after(html)
    }
  })
})

$('#notes').on('click', function (event) {
  if (event.target.classList.contains('delete-note-button')) {
    let noteId = event.target.dataset['noteId']
    deleteNote(noteId)
  }
})

loadNotes()
