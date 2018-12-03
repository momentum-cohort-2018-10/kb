function findShortest (array) {
  let shortest = null
  for (let element of array) {
    if (shortest === null || shortest.length > element.length) {
      shortest = element
    }
  }
  return shortest
}

let names = [
  'Rowan',
  'Allison',
  'Cadence',
  'Dale',
  'Frankie',
  'River'
]

for (let name of names) {
  console.log(`${name} has ${name.length} letters`)
}

console.log(`${findShortest(names)} is the shortest name.`)
