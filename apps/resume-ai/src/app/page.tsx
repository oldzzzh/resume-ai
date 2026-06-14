import { FileText, Sparkles, ArrowRight, Check } from "lucide-react";

export default function Home() {
  return (
    <div className="min-h-screen">
      {/* Nav */}
      <header className="border-b border-gray-200 bg-white/80 backdrop-blur-sm sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2 font-semibold text-lg"><FileText className="w-5 h-5 text-blue-600" /><span>ResumeAI</span></div>
          <nav className="flex items-center gap-6 text-sm text-gray-600">
            <a href="#how-it-works" className="hover:text-gray-900">How It Works</a>
            <a href="#pricing" className="hover:text-gray-900">Pricing</a>
            <a href="/upload" className="bg-blue-600 text-white px-5 py-2 rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors">Get Started Free</a>
          </nav>
        </div>
      </header>
      {/* Hero */}
      <section className="max-w-6xl mx-auto px-4 pt-24 pb-16 text-center">
        <div className="inline-flex items-center gap-2 bg-blue-50 text-blue-700 text-sm px-4 py-1.5 rounded-full mb-6"><Sparkles className="w-4 h-4" /> AI-Powered Resume Optimization</div>
        <h1 className="text-5xl sm:text-6xl font-bold tracking-tight text-gray-900 leading-tight mb-6">Your resume, optimized by AI.<br /><span className="text-blue-600">More interviews, guaranteed.</span></h1>
        <p className="text-xl text-gray-500 max-w-2xl mx-auto mb-8">Upload your resume and job description. Our AI rewrites your experience to match what employers are looking for. Get a tailored resume in 30 seconds.</p>
        <a href="/upload" className="inline-flex bg-blue-600 text-white px-8 py-3.5 rounded-xl text-lg font-medium hover:bg-blue-700 transition-colors shadow-lg shadow-blue-200 items-center gap-2">Optimize Your Resume Free <ArrowRight className="w-5 h-5" /></a>
        <p className="text-sm text-gray-400 mt-4">No credit card required &middot; 3 free optimizations</p>
      </section>
    </div>
  );
}