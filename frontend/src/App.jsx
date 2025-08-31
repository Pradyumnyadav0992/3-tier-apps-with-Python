import React, { useEffect, useState } from 'react'

function App() {
  const [msg, setMsg] = useState('Loading...')

  useEffect(() => {
    const apiUrl = import.meta.env.VITE_API_URL || ''  // fallback if not set
     fetch("http://18.209.211.124:8000/api/hello")
      .then(res => res.json())
      .then(data => setMsg(data.message))
      .catch(() => setMsg('Error fetching backend'))
  }, [])

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>3-Tier App</h1>
      <p>{msg}</p>
    </div>
  )
}

export default App

