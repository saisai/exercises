
import React, { useState, useEffect } from 'react'

function UseEffectHookCounterOne() {
	const [count, setCount] = useState(0)

	useEffect( () => {
		document.title = `you clicked ${count} times`
	})

	return (
		<div>
			<button onClick={() => setCount(count + 1)}>Click {count} times.</button>
		</div>
	)
} 

export default UseEffectHookCounterOne
