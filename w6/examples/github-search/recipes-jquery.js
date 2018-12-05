/* globals $, jQuery */

/*

https://api.github.com/search/repositories?q=lasagna&language=python

https - protocol
api.github.com - domain
/search/repositories - path
q=lasagna - query string

*/
$('#search-button').on('click', function (event) {
  let query = $('#search-field').val()
  let language = $('#search-language').val()

  if (language) {
    query += ` language:${language}`
  }

  $.get('https://api.github.com/search/repositories', { q: query }, function (results) {
    console.log(results)
    let $resultsDiv = $('#search-results')

    $resultsDiv
      .empty()
      .append(
        $('<p>')
          .text(`Total count: ${results.total_count}`)
      )
      .append(results.items.map(repoHtml))
  })
})

function repoHtml (repo) {
  return `    
    <p><a href="${repo.html_url}">${repo.name}</a> - ${repo.description || 'no description'}</p>
  `
}
