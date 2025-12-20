import { useState } from 'react'
import { Sparkles, User, Loader2, Brain, Images, MessageSquare } from 'lucide-react'
import ProfileForm from './components/ProfileForm'
import LoadingView from './components/LoadingView'
import ResultsView from './components/ResultsView'

function App() {
    const [stage, setStage] = useState('input') // input | loading | results
    const [results, setResults] = useState(null)
    const [error, setError] = useState(null)

    const handleAnalyze = async (profile) => {
        setStage('loading')
        setError(null)

        try {
            const response = await fetch('/api/v1/personality/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(profile),
            })

            if (!response.ok) {
                throw new Error(`API Error: ${response.status}`)
            }

            const data = await response.json()
            setResults(data)
            setStage('results')
        } catch (err) {
            console.error('Analysis error:', err)
            setError(err.message)
            setStage('input')
        }
    }

    const handleReset = () => {
        setStage('input')
        setResults(null)
        setError(null)
    }

    return (
        <div className="min-h-screen flex flex-col items-center justify-center p-4">
            <div className="w-full max-w-6xl">
                {/* Header */}
                <div className="text-center mb-8">
                    <div className="flex items-center justify-center gap-3 mb-4">
                        <Sparkles className="w-12 h-12 text-yellow-300" />
                        <h1 className="text-5xl font-bold text-white">Personality Game</h1>
                    </div>
                    <p className="text-xl text-purple-100">
                        AI-Powered Visual Personality Assessment
                    </p>
                </div>

                {/* Error Display */}
                {error && (
                    <div className="bg-red-500/20 border border-red-500 text-white rounded-lg p-4 mb-6">
                        <strong>Error:</strong> {error}
                    </div>
                )}

                {/* Main Content */}
                {stage === 'input' && <ProfileForm onSubmit={handleAnalyze} />}
                {stage === 'loading' && <LoadingView />}
                {stage === 'results' && <ResultsView results={results} onReset={handleReset} />}

                {/* Footer */}
                <div className="text-center mt-8 text-purple-200 text-sm">
                    Powered by Google Gemini & LangGraph
                </div>
            </div>
        </div>
    )
}

export default App
