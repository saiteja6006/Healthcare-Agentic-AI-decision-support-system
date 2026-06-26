"use client";

import { useState } from "react";
import { makeDecision } from "@/services/api";
import ResultCard from "./ResultCard";

export default function CaseForm() {
    const [condition, setCondition] = useState("");
    const [durationWeeks, setDurationWeeks] = useState<number | "">("");
    const [physicalTherapy, setPhysicalTherapy] = useState(false);

    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<any>(null);

    function clearForm() {
        setCondition("");
        setDurationWeeks("");
        setPhysicalTherapy(false);
        setResult(null);
    }

    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault();

        if (!condition.trim()) {
            alert("Please enter a medical condition.");
            return;
        }

        if (durationWeeks === "" || durationWeeks <= 0) {
            alert("Duration must be greater than 0.");
            return;
        }

        setLoading(true);
        setResult(null);

        try {
           

            const response = await makeDecision(
                condition,
                durationWeeks,
                physicalTherapy
            );

            setResult(response);
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    }

    return (
        <>
            <form
                onSubmit={handleSubmit}
                className="bg-slate-800 p-8 rounded-xl"
            >
                <div className="mb-5">
                    <label className="block mb-2">
                        Condition
                    </label>

                    <input
                        className="w-full p-3 rounded bg-slate-700 text-white"
                        placeholder="e.g. Neck Pain"
                        value={condition}
                        onChange={(e) =>
                            setCondition(e.target.value)
                        }
                    />
                </div>

                <div className="mb-5">
                    <label className="block mb-2">
                        Duration (Weeks)
                    </label>

                    <input
                        type="number"
                        className="w-full p-3 rounded bg-slate-700 text-white"
                        placeholder="Enter duration"
                        value={durationWeeks}
                        onChange={(e) =>
                            setDurationWeeks(
                                e.target.value === ""
                                    ? ""
                                    : Number(e.target.value)
                            )
                        }
                    />
                </div>

                <div className="mb-6 flex items-center gap-3">
                    <input
                        type="checkbox"
                        checked={physicalTherapy}
                        onChange={(e) =>
                            setPhysicalTherapy(
                                e.target.checked
                            )
                        }
                    />

                    <label>
                        Physical Therapy Completed
                    </label>
                </div>

                <div className="flex gap-4">

                    <button
                        type="submit"
                        disabled={loading}
                        className="flex-1 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white py-3 rounded-lg transition"
                    >
                        {loading ? (
                            <div className="flex items-center justify-center gap-3">
                                <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>

                                <span>
                                    Analyzing...
                                </span>
                            </div>
                        ) : (
                            "Evaluate Case"
                        )}
                    </button>

                    <button
                        type="button"
                        onClick={clearForm}
                        disabled={loading}
                        className="px-6 bg-slate-700 hover:bg-slate-600 disabled:bg-slate-800 rounded-lg text-white transition"
                    >
                        Clear
                    </button>

                </div>
            </form>

            {loading && (
                <div className="mt-6 bg-slate-800 rounded-xl border border-slate-700 p-6">
                    <div className="flex items-center gap-4">

                        <div className="w-8 h-8 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>

                        <div>
                            <h2 className="text-xl font-semibold text-white">
                                AI is analyzing the patient case...
                            </h2>

                            <p className="text-gray-400 mt-2">
                                Retrieving clinical guidelines,
                                validating evidence, checking
                                insurance policies, and generating
                                recommendations...
                            </p>
                        </div>

                    </div>
                </div>
            )}

            {!loading && result && (
                <ResultCard
                    result={result}
                />
            )}
        </>
    );
}