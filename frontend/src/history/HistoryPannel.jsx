import "react"
import { useState, useEffect } from "react"
import { MCQChallenge } from "../challenge/MCQChallenge"

export function HistoryPannel(){
    const [history, setHistory] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const [error, setError ] = useState(null)

    // As soon as the component load, fetch History
    useEffect(() => {
        fetchHistory()

    }, [])

    const fetchHistory = async() => {
        setIsLoading(false)
    }

    if (isLoading){
        return <div className="loading">Loading History...</div>
    }

    if (error){
        return <div>
            <p>{error}</p>
            <button onClick={fetchHistory}>Retry</button>
        </div>
    }

    return <div className="history-panel">
        <h2>History</h2>
        {history.length === 0 ? <p>No challenge history</p> : 
            <div className="history-list">
                {history.map((challenge) =>{
                    return <MCQChallenge challenge={challenge} 
                            key={challenge.id} 
                            showExplaination
                        />
                    })
                }
            </div>
        
        }
    </div>
}