const names = [
  'Roguy Bertson',
  'Gerey',
  'Cyne',
  'Symes',
  'Ewip',
  'Ealdwyth',
  'Gauwill',
  'Burgwiu',
  'Helne',
  'Berny Warry',
  'Efrin',
  'Ellyn',
  'Aten',
  'Elys Erneyng',
  'Ecin',
  'Conguia',
  'Jane',
  'Aerorn',
  'Aethed',
  'Hily',
  'Gili',
  'Umrat',
  'Dinain',
  'Abar',
  'Urur',
  'Throinain',
  'Gamil',
  'Kharkal',
  'Kali',
  'Ukhur',
  'Banain',
  'Kilmah',
  'Geda',
  'Thrazagh',
  'Disanz',
  'Kurdu',
  'Banarv',
  'Urud',
  'Thrinarv',
  'Sharkurd',
  'Willas',
  'Robert',
  'Reyny',
  'Gorme',
  'Richye Nyne',
  'Lesym',
  'Wisym',
  'Gyles Pyley',
  'Andes',
  'Tinbrard',
  'Atrix',
  'Mosa',
  'Landa Gammugw',
  'Elan Banksi',
  'Lada Bolge',
  'Athet',
  'Daldra Groper',
  'Atrin',
  'Fira',
  'Tella Oldbubb'
]

const traitTables = {
  physique: [
    'Athletic',
    'Brawny',
    'Corpulent',
    'Delicate',
    'Gaunt',
    'Hulking',
    'Lanky',
    'Ripped',
    'Rugged',
    'Scrawny',
    'Short',
    'Sinewy',
    'Slender',
    'Flabby',
    'Statuesque',
    'Stout',
    'Tiny',
    'Towering',
    'Willowy',
    'Wiry'
  ],
  face: [
    'Bloated',
    'Blunt',
    'Bony',
    'Chiseled',
    'Delicate',
    'Elongated',
    'Patrician',
    'Pinched',
    'Hawkish',
    'Broken',
    'Impish',
    'Narrow',
    'Ratlike',
    'Round',
    'Sunken    ',
    'Sharp',
    'Soft',
    'Square',
    'Wide',
    'Wolfish'
  ],
  skin: [
    'Birthmark',
    'Calloused',
    'Freckled',
    'Hairless',
    'Hirsute',
    'Leathery',
    'Lined',
    'Oily',
    'Perfect',
    'Pierced',
    'Pockmarked',
    'Rosy',
    'Rough',
    'Scaly',
    'Scarred',
    'Silky',
    'Sunburned',
    'Tanned',
    'Tattooed',
    'Weathered'
  ],
  hair: [
    'Bald',
    'Braided',
    'Bristly',
    'Cropped',
    'Curly',
    'Disheveled',
    'Dreadlocks',
    'Filthy',
    'Frizzy',
    'Greased',
    'Limp',
    'Long',
    'Luxurious',
    'Mohawk',
    'Oily',
    'Ponytail',
    'Silky',
    'Topknot',
    'Wavy',
    'Wispy'
  ],
  clothing: [
    'Antique',
    'Bloody',
    'Ceremonial',
    'Decorated',
    'Eccentric',
    'Elegant',
    'Fashionable',
    'Filthy',
    'Flamboyant',
    'Stained',
    'Foreign',
    'Frayed',
    'Frumpy',
    'Livery',
    'Oversized',
    'Patched',
    'Perfumed',
    'Rancid',
    'Torn',
    'Undersized'
  ],
  virtue: [
    'Ambitious',
    'Cautious',
    'Courageous',
    'Courteous',
    'Curious',
    'Disciplined',
    'Focused',
    'Generous',
    'Gregarious',
    'Honest',
    'Honorable',
    'Humble',
    'Idealistic',
    'Just',
    'Loyal',
    'Merciful',
    'Righteous',
    'Serene',
    'Stoic',
    'Tolerant'
  ],
  vice: [
    'Aggressive',
    'Arrogant',
    'Bitter',
    'Cowardly',
    'Cruel',
    'Deceitful',
    'Flippant',
    'Gluttonous',
    'Greedy',
    'Irascible',
    'Lazy',
    'Nervous',
    'Prejudiced',
    'Reckless',
    'Rude',
    'Suspicious',
    'Vain',
    'Vengeful',
    'Wasteful',
    'Whiny'
  ],
  speech: [
    'Blunt',
    'Booming',
    'Breathy',
    'Cryptic',
    'Drawling',
    'Droning',
    'Flowery',
    'Formal',
    'Gravelly',
    'Hoarse',
    'Mumbling',
    'Precise',
    'Quaint',
    'Rambling',
    'Rapid-fire',
    'Dialect',
    'Slow',
    'Squeaky',
    'Stuttering',
    'Whispery'
  ],
  misfortunes: [
    'Abandoned',
    'Addicted',
    'Blackmailed',
    'Condemned',
    'Cursed',
    'Defrauded',
    'Demoted',
    'Discredited',
    'Disowned',
    'Exiled',
    'Framed',
    'Haunted',
    'Humiliated',
    'Kidnapped',
    'Mutilated',
    'Poor',
    'Pursued',
    'Rejected',
    'Replaced',
    'Robbed',
    'Suspected'
  ]
}

const armorDefense = {
  'No armor': 1,
  'Gambeson': 2,
  'Brigandine': 3,
  'Chain': 4
}

const weaponClasses = [
  ['Dagger', 'Cudgel', 'Sickle', 'Staff'],
  ['Spear', 'Mace', 'Sword', 'Axe', 'Flail'],
  ['Halberd', 'War Hammer', 'Battle Axe', 'Longsword']
]

const weapons = {
  'Bow': {
    damage: 'd6', slots: 2
  },
  'Sling': {
    damage: 'd4', slots: 1
  },
  'Crossbow': {
    damage: 'd8', slots: 3
  }
}
for (var weaponClass = 0; weaponClass < weaponClasses.length; weaponClass++) {
  let weaponList = weaponClasses[weaponClass]
  for (let weapon of weaponList) {
    weapons[weapon] = {
      damage: `d${4 + weaponClass * 2}`,
      slots: weaponClass + 1
    }
  }
}

const equipmentTables = {
  armor: makeWeightedArray({
    'No armor': 3, 'Gambeson': 11, 'Brigandine': 4, 'Chain': 1
  }),
  helmetAndShield: makeWeightedArray({
    'None': 13, 'Helmet': 3, 'Shield': 3, 'Helmet and Shield': 1
  }),
  weapons: makeWeightedArray({
    'Dagger': 3,
    'Cudgel': 3,
    'Sickle': 3,
    'Staff': 3,
    'Spear': 3,
    'Sword': 2,
    'Axe': 2,
    'Flail': 1,
    'Sling': 2,
    'Bow': 2,
    'Crossbow': 2,
    'Halberd': 1,
    'War Hammer': 1,
    'Battle Axe': 1,
    'Longsword': 1
  }),
  dungeoneering: [
    'Rope, 50ft',
    'Pulleys',
    'Candles, 5',
    'Chain, 10ft',
    'Chalk, 10',
    'Crowbar',
    'Tinderbox',
    'Grap. hook',
    'Hammer',
    'Waterskin',
    'Lantern',
    'Lamp oil',
    'Padlock',
    'Manacles',
    'Mirror',
    'Pole, 10ft',
    'Sack',
    'Tent',
    'Spikes, 5',
    'Torches, 5'
  ],
  general1: [
    'Air bladder',
    'Bear trap',
    'Shovel',
    'Bellows',
    'Grease',
    'Saw',
    'Bucket',
    'Caltrops',
    'Chisel',
    'Drill',
    'Fishing rod',
    'Marbles',
    'Glue',
    'Pick',
    'Hourglass',
    'Net',
    'Tongs',
    'Lockpicks',
    'Metal file',
    'Nails'
  ],
  general2: [
    'Incense',
    'Sponge',
    'Lens',
    'Perfume',
    'Horn',
    'Bottle',
    'Soap',
    'Spyglass',
    'Tar pot',
    'Twine',
    'Fake jewels',
    'Blank book',
    'Card deck',
    'Dice set',
    'Cook pots',
    'Face paint',
    'Whistle',
    'Instrument',
    'Quill & Ink',
    'Small bell'
  ]
}

function makeWeightedArray (weights) {
  let array = []
  for (let key in weights) {
    for (let i = 0; i < weights[key]; i++) {
      array.push(key)
    }
  }
  return array
}

function rollStat () {
  let rolls = []
  for (let i = 0; i < 3; i++) {
    rolls.push(Math.floor(Math.random() * 6 + 1))
  }
  return Math.min(rolls[0], rolls[1], rolls[2])
}

function randomChoice (array) {
  return array[Math.floor(Math.random() * array.length)]
}

function makeItemSlot (item) {
  return `<div class="bg-white w-25-l w-33-m w-50 h2 outline br bb pa2">${item || ''}</div>`
}

function makeCharacter () {
  console.log('makeCharacter')
  const name = randomChoice(names)
  document.getElementById('name').innerText = name

  const stats = ['str', 'dex', 'con', 'int', 'wis', 'cha', 'luck']
  let numOfSlots

  for (let stat of stats) {
    let score = rollStat()
    if (stat === 'con') {
      numOfSlots = 10 + score
    }
    document.getElementById(stat).querySelector('.score').innerText = `${10 + score}/+${score}`
  }

  const hp = Math.floor(Math.random() * 4 + 5)
  document.getElementById('hp').querySelector('.score').innerText = hp

  const traits = Object.keys(traitTables)
  for (let trait of traits) {
    let result = randomChoice(traitTables[trait])
    document.getElementById(trait).querySelector('.trait').innerText = result
  }

  let equipment = []

  const weapon = randomChoice(equipmentTables['weapons'])
  const weaponSlots = weapons[weapon].slots
  if (weaponSlots > 1) {
    for (let i = 1; i <= weaponSlots; i++) {
      equipment.push(`${weapon} (slot ${i})`)
    }
  } else {
    equipment.push(weapon)
  }

  const armor = randomChoice(equipmentTables['armor'])
  let armorScore = armorDefense[armor]
  for (let i = 1; i < armorScore; i++) {
    equipment.push(`${armor} (slot ${i})`)
  }

  const helmetAndShield = randomChoice(equipmentTables['helmetAndShield'])

  if (helmetAndShield === 'Helmet' || helmetAndShield === 'Helmet and shield') {
    equipment.push('Helmet')
    armorScore++
  }

  if (helmetAndShield === 'Shield' || helmetAndShield === 'Helmet and shield') {
    equipment.push('Shield')
    armorScore++
  }

  document.getElementById('armor').querySelector('.score').innerText = `${10 + armorScore}/+${armorScore}`

  equipment = equipment.concat([
    randomChoice(equipmentTables['dungeoneering']),
    randomChoice(equipmentTables['dungeoneering']),
    randomChoice(equipmentTables['general1']),
    randomChoice(equipmentTables['general2'])
  ])

  document.getElementById('item-slots').innerHTML = ''
  for (let i = 0; i < numOfSlots; i++) {
    document.getElementById('item-slots').innerHTML += makeItemSlot(equipment[i])
  }
}

document.getElementById('reroll').addEventListener('click', makeCharacter)
makeCharacter()
