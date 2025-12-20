import { useState } from 'react'
import { User, ArrowRight } from 'lucide-react'

export default function ProfileForm({ onSubmit }) {
    const [formData, setFormData] = useState({
        name: '',
        age: '',
        gender: '',
        profession: '',
        nationality: ''
    })

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        onSubmit({
            ...formData,
            age: parseInt(formData.age)
        })
    }

    const isValid = formData.name && formData.age && formData.gender &&
        formData.profession && formData.nationality

    return (
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl shadow-2xl p-8 border border-white/20">
            <div className="flex items-center gap-3 mb-6">
                <User className="w-8 h-8 text-purple-300" />
                <h2 className="text-3xl font-bold text-white">Tell Us About Yourself</h2>
            </div>

            <form onSubmit={handleSubmit} className="space-y-5">
                <div>
                    <label className="block text-purple-100 font-medium mb-2">Name</label>
                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        className="w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white placeholder-purple-200 focus:outline-none focus:ring-2 focus:ring-purple-400"
                        placeholder="Enter your name"
                        required
                    />
                </div>

                <div>
                    <label className="block text-purple-100 font-medium mb-2">Age</label>
                    <input
                        type="number"
                        name="age"
                        value={formData.age}
                        onChange={handleChange}
                        className="w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white placeholder-purple-200 focus:outline-none focus:ring-2 focus:ring-purple-400"
                        placeholder="Enter your age"
                        min="1"
                        max="120"
                        required
                    />
                </div>

                <div>
                    <label className="block text-purple-100 font-medium mb-2">Gender</label>
                    <select
                        name="gender"
                        value={formData.gender}
                        onChange={handleChange}
                        className="w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white focus:outline-none focus:ring-2 focus:ring-purple-400"
                        required
                    >
                        <option value="">Select gender</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Non-binary">Non-binary</option>
                        <option value="Prefer not to say">Prefer not to say</option>
                    </select>
                </div>

                <div>
                    <label className="block text-purple-100 font-medium mb-2">Profession</label>
                    <input
                        type="text"
                        name="profession"
                        value={formData.profession}
                        onChange={handleChange}
                        className="w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white placeholder-purple-200 focus:outline-none focus:ring-2 focus:ring-purple-400"
                        placeholder="e.g., Software Engineer"
                        required
                    />
                </div>

                <div>
                    <label className="block text-purple-100 font-medium mb-2">Nationality</label>
                    <input
                        type="text"
                        name="nationality"
                        value={formData.nationality}
                        onChange={handleChange}
                        className="w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white placeholder-purple-200 focus:outline-none focus:ring-2 focus:ring-purple-400"
                        placeholder="e.g., American"
                        required
                    />
                </div>

                <button
                    type="submit"
                    disabled={!isValid}
                    className="w-full bg-gradient-to-r from-purple-500 to-pink-500 text-white font-bold py-4 px-6 rounded-lg hover:from-purple-600 hover:to-pink-600 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 shadow-lg"
                >
                    Start Analysis
                    <ArrowRight className="w-5 h-5" />
                </button>
            </form>
        </div>
    )
}
