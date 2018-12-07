/* globals $ */

function sum (numbers) {
  let total = 0
  for (let num of numbers) {
    total += num
  }
  return total
}

function day1 () {
  $.get('day1.txt', function (results) {
    const freqChanges = []
    const lines = results.split('\n')
    for (let line of lines) {
      let change = parseInt(line)
      if (!isNaN(change)) {
        freqChanges.push(change)
      }
    }

    day1a(freqChanges)
    day1b(freqChanges)
  })
}

function day1a (freqChanges) {
  let total = sum(freqChanges)

  $('#day1').append(
    $('<p>').html(`<b>Problem 1</b>: ${total}`)
  )
}

function day1b (freqChanges) {
  let currentFreq = 0
  let prevFreqs = new Set()

  while (true) {
    for (let change of freqChanges) {
      prevFreqs.add(currentFreq)
      currentFreq += change
      if (prevFreqs.has(currentFreq)) {
        $('#day1').append(
          $('<p>').html(`<b>Problem 2</b>: ${currentFreq}`)
        )
        return
      }
    }
  }
}

function day2 () {
  $.get('day2.txt', function (results) {
    const keys = []
    const lines = results.split('\n')
    for (let line of lines) {
      if (line !== '') {
        keys.push(line)
      }
    }

    day2a(keys)
  })
}

function day2a (keys) {
  let dupCount = 0
  let tripCount = 0

  for (let key of keys) {
    if (hasXLetters(2, key)) {
      dupCount += 1
    }
    if (hasXLetters(3, key)) {
      tripCount += 1
    }
  }

  $('#day2').append(
    $('<p>').html(`<b>Problem 1</b>: ${dupCount * tripCount}`)
  )
}

function hasXLetters (x, string) {
  const letterCounts = letterCounter(string)
  for (let letter of Object.keys(letterCounts)) {
    let count = letterCounts[letter]
    if (count === x) {
      return true
    }
  }
  return false
}

function letterCounter (string) {
  const letterCounts = {}
  for (let letter of string) {
    if (letterCounts[letter] === undefined) {
      letterCounts[letter] = 1
    } else {
      letterCounts[letter] += 1
    }
  }
  return letterCounts
}

day1()
day2()
