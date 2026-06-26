import CaseForm from "@/components/CaseForm";

export default function Home() {

    return (

        <main className="min-h-screen bg-slate-900 text-gray-200">

            <div className="max-w-5xl mx-auto p-10">

                <h1 className="text-4xl font-bold text-cyan-400 mb-10">

                    Healthcare Agentic AI Platform

                </h1>

                <CaseForm />

            </div>

        </main>
    );
}