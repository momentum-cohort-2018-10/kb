/* globals $, jQuery */

const searchButton = document.getElementById('search-button')
const searchField = document.getElementById('search-field')

searchButton.addEventListener('click', function (event) {
  $.ajax({
    url: 'https://api.github.com/search/repositories',
    data: {
      q: searchField.value
    },
    success: function (results) {
      console.log(results)
      let resultsDiv = document.getElementById('search-results')
      resultsDiv.innerHTML = ''
      let countP = document.createElement('p')
      countP.innerText = `Total count: ${results.total_count}`
      resultsDiv.appendChild(countP)

      for (let repo of results.items) {
        let repoP = document.createElement('p')
        let repoLink = document.createElement('a')
        repoLink.href = repo.html_url
        repoLink.innerText = repo.name
        repoP.appendChild(repoLink)
        resultsDiv.appendChild(repoP)
      }
    }
  })
})
