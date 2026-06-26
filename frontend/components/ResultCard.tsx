import { DecisionResponse } from "@/types/decision";

interface Props {
    result: DecisionResponse;
}

export default function ResultCard(
    { result }: Props
) {

    return (

        <div className="bg-slate-800 rounded-xl p-6 mt-8">

            <h2 className="text-2xl text-cyan-400 mb-4">
                Case Result
            </h2>

            <div className="mb-4">
                <h3 className="font-bold text-green-400">
                    Status
                </h3>

                <p>{result.status}</p>
            </div>

            <div className="mb-4">
                <h3 className="font-bold text-cyan-400">
                    Reason
                </h3>

                <p>{result.reason}</p>
            </div>

            <div className="mb-4">

                <h3 className="font-bold text-cyan-400">
                        Recommendation
                </h3>

                <p>
                     {result.recommendation}
                </p>

        </div>


        <div className="mb-4">

            <h3 className="font-bold text-cyan-400">
                Reasoning
            </h3>

            <p>
                {result.reasoning}
            </p>

            </div>


            <div className="mb-4">

                <h3 className="font-bold text-cyan-400">
                      Confidence
                </h3>

             <p>
                  {result.confidence}
            </p>

        </div>
            <div className="mb-4">
                <h3 className="font-bold text-cyan-400">
                    Evidence
                </h3>

                <ul className="list-disc pl-5">
                    {
                        result.evidence.map(
                            (evidence, index) => (
                                <li key={index}>
                                    {evidence}
                                </li>
                            )
                        )
                    }
                </ul>
            </div>

            <div>
                <h3 className="font-bold text-cyan-400">
                    Tools Used
                </h3>

                <ul className="list-disc pl-5">
                    {
                        result.tools_used.map(
                            (tool, index) => (
                                <li key={index}>
                                    {tool}
                                </li>
                            )
                        )
                    }
                </ul>
            </div>

        </div>
    );
}