import { DecisionResponse } from "@/types/decision";

export async function makeDecision(
    condition: string,
    durationWeeks: number,
    physicalTherapy: boolean
): Promise<DecisionResponse> {

    const response = await fetch(
        "/api/decision",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                condition,
                duration_weeks: durationWeeks,
                physical_therapy: physicalTherapy
            })
        }
    );

    return response.json();
}