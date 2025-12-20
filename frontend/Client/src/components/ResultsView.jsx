import { Trophy, RefreshCw, Images, MessageSquare } from 'lucide-react'

export default function ResultsView({ results, onReset }) {
    return (
        <div className="space-y-6">
            {/* MBTI Result Card */}
            <div className="bg-gradient-to-br from-yellow-400 to-orange-500 rounded-2xl shadow-2xl p-8 border border-white/20">
                <div className="flex items-center gap-3 mb-4">
                    <Trophy className="w-10 h-10 text-white" />
                    <h2 className="text-3xl font-bold text-white">Your Personality Type</h2>
                </div>

                <div className="bg-white/20 backdrop-blur rounded-lg p-6">
                    <p className="text-white text-lg whitespace-pre-line">
                        {results?.mbti_result || 'Analysis in progress...'}
                    </p>
                </div>

                <div className="mt-4 grid grid-cols-2 gap-4 text-white/90">
                    <div className="bg-white/10 rounded-lg p-3">
                        <div className="text-sm opacity-80">Images Generated</div>
                        <div className="text-2xl font-bold">{results?.images_generated || 0}</div>
                    </div>
                    <div className="bg-white/10 rounded-lg p-3">
                        <div className="text-sm opacity-80">Questions Created</div>
                        <div className="text-2xl font-bold">{results?.mcqs_count || 0}</div>
                    </div>
                </div>
            </div>

            {/* Profile Analysis */}
            {results?.analysis && (
                <div className="bg-white/10 backdrop-blur-lg rounded-2xl shadow-2xl p-6 border border-white/20">
                    <h3 className="text-2xl font-bold text-white mb-3">Profile Analysis</h3>
                    <p className="text-purple-100 mb-4">{results.analysis.summary}</p>

                    {results.analysis.style_cues && (
                        <div className="space-y-3">
                            <div>
                                <span className="text-purple-300 font-medium">Tone: </span>
                                <span className="text-white">{results.analysis.style_cues.tone}</span>
                            </div>
                            <div>
                                <span className="text-purple-300 font-medium">Themes: </span>
                                <span className="text-white">{results.analysis.style_cues.themes?.join(', ')}</span>
                            </div>
                        </div>
                    )}
                </div>
            )}

            {/* MCQs Preview (if available) */}
            {results?.mcqs_count > 0 && (
                <div className="bg-white/10 backdrop-blur-lg rounded-2xl shadow-2xl p-6 border border-white/20">
                    <div className="flex items-center gap-3 mb-4">
                        <MessageSquare className="w-6 h-6 text-purple-300" />
                        <h3 className="text-2xl font-bold text-white">Sample Questions</h3>
                    </div>
                    <p className="text-purple-200 text-sm">
                        {results.mcqs_count} personality questions were generated based on visual scenarios.
                        These help determine your MBTI type through situational analysis.
                    </p>
                </div>
            )}

            {/* Reset Button */}
            <button
                onClick={onReset}
                className="w-full bg-white/20 hover:bg-white/30 text-white font-bold py-4 px-6 rounded-lg transition-all flex items-center justify-center gap-2 border border-white/30"
            >
                <RefreshCw className="w-5 h-5" />
                Start New Analysis
            </button>
        </div>
    )
}
