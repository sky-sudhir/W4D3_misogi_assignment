'use client'

import { useState } from 'react'

export default function Home() {
  const [inputs, setInputs] = useState<string[]>(['', ''])
  const [matrix, setMatrix] = useState<number[][]>([])
  const [clones, setClones] = useState<[number, number][]>([])

  const handleInputChange = (index: number, value: string) => {
    const newInputs = [...inputs]
    newInputs[index] = value
    setInputs(newInputs)
  }

  const addInput = () => setInputs([...inputs, ''])

  const analyze = async () => {
    const response = await fetch('http://localhost:8000/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ texts: inputs }),
    })
    const result = await response.json()
    setMatrix(result.matrix)
    setClones(result.clones)
  }

  const isClone = (i: number, j: number) =>
    clones.some(([a, b]) => (a === i && b === j) || (a === j && b === i))

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Semantic Similarity Checker</h1>

      {inputs.map((text, idx) => (
        <textarea
          key={idx}
          value={text}
          onChange={(e) => handleInputChange(idx, e.target.value)}
          placeholder={`Text ${idx + 1}`}
          className="w-full p-3 mb-3 border rounded bg-white"
        />
      ))}

      <div className="flex gap-4 mb-6">
        <button onClick={addInput} className="bg-blue-600 text-white px-4 py-2 rounded">
          + Add Text
        </button>
        <button onClick={analyze} className="bg-green-600 text-white px-4 py-2 rounded">
          Analyze
        </button>
      </div>

      {matrix.length > 0 && (
        <div className="overflow-x-auto">
          <table className="table-auto border-collapse border w-full text-center">
            <thead>
              <tr>
                <th className="border p-2 bg-gray-100">#</th>
                {inputs.map((_, j) => (
                  <th key={j} className="border p-2 bg-gray-100">Text {j + 1}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {matrix.map((row, i) => (
                <tr key={i}>
                  <td className="border p-2 bg-gray-100 font-bold">Text {i + 1}</td>
                  {row.map((val, j) => (
                    <td
                      key={j}
                      className={`border p-2 ${isClone(i, j) && i !== j ? 'bg-red-100 text-red-700 font-semibold' : ''}`}
                    >
                      {val.toFixed(2)}%
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}
