import { Loader2, Brain, Image, MessageSquare, Target } from 'lucide-react'

export default function LoadingView() {
    return (
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl shadow-2xl p-12 border border-white/20">
            <div className="flex flex-col items-center justify-center space-y-8">
                <div className="relative">
                    <Loader2 className="w-20 h-20 text-purple-300 animate-spin" />
                    <Brain className="w-10 h-10 text-yellow-300 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" />
                </div>

                <div className="text-center space-y-3">
                    <h2 className="text-3xl font-bold text-white">Analyzing Your Personality</h2>
                    <p className="text-purple-200 text-lg">
                        This may take 2-3 minutes. Please wait while AI works its magic...
                    </p>
                </div>

                <div className="w-full max-w-md space-y-4">
                    <LoadingStep
                        icon={<Brain />}
                        text="Analyzing your profile..."
                        delay={0}
                    />
                    <LoadingStep
                        icon={<MessageSquare />}
                        text="Generating creative scenarios..."
                        delay={500}
                    />
                    <LoadingStep
                        icon={<Image />}
                        text="Creating visual prompts..."
                        delay={1000}
                    />
                    <LoadingStep
                        icon={<Target />}
                        text="Determining personality type..."
                        delay={1500}
                    />
                </div>

                <div className="flex gap-2">
                    <div className="w-3 h-3 bg-purple-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
                    <div className="w-3 h-3 bg-pink-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
                    <div className="w-3 h-3 bg-yellow-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
                </div>
            </div>
        </div>
    )
}

function LoadingStep({ icon, text, delay }) {
    return (
        <div
            className="flex items-center gap-3 text-purple-100 animate-pulse"
            style={{ animationDelay: `${delay}ms` }}
        >
            <div className="text-purple-300">
                {icon}
            </div>
            <span className="text-sm">{text}</span>
        </div>
    )
}
