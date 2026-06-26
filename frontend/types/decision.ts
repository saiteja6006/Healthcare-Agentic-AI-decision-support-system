export interface DecisionResponse {

    recommendation: string;

    reasoning: string;

    confidence: string;

    status: string;

    reason: string;

    evidence: string[];

    tools_used: string[];
}