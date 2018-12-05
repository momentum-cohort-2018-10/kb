/* globals $, jQuery */

/*

https://api.github.com/search/repositories?q=lasagna&language=python

https - protocol
api.github.com - domain
/search/repositories - path
q=lasagna - query string

*/

const searchButton = document.getElementById('search-button')
const searchField = document.getElementById('search-field')
const searchLanguage = document.getElementById('search-language')

searchButton.addEventListener('click', function (event) {
  let query = searchField.value
  let language = searchLanguage.value

  if (language) {
    query += ` language:${language}`
  }

  $.get('https://api.github.com/search/repositories', { q: query }, function (results) {
    console.log(results)
    let resultsDiv = document.getElementById('search-results')
    resultsDiv.innerHTML = ''
    let countP = document.createElement('p')
    countP.innerText = `Total count: ${results.total_count}`
    resultsDiv.appendChild(countP)

    for (let repo of results.items) {
      let repoP = document.createElement('p')
      repoP.innerHTML = repoHtml(repo)
      resultsDiv.appendChild(repoP)
    }
  })
})

function repoHtml (repo) {
  return `    
    <a href="${repo.html_url}">${repo.name}</a> - ${repo.description}
  `
}
