import { useState } from 'react'

const vocabulary = [
  { word: 'apple', meaning: 'elma' },
  { word: 'book', meaning: 'kitap' },
  { word: 'cat', meaning: 'kedi' }
]

function Flashcard({ word, meaning }) {
  const [showMeaning, setShowMeaning] = useState(false)
  return (
    <div className="card" onClick={() => setShowMeaning(!showMeaning)}>
      <h3>{word}</h3>
      {showMeaning && <p>{meaning}</p>}
    </div>
  )
}

export default function App() {
  return (
    <div className="container">
      {vocabulary.map((item, index) => (
        <Flashcard key={index} {...item} />
      ))}
    </div>
  )
}
