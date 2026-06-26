from app.services.policy_retrieval_service import (
    PolicyRetrievalService
)

policy_service = (
    PolicyRetrievalService()
)

test_cases = [

    {
        "query":
            "MRI insurance authorization",

        "expected_keywords":
            [
                "prior authorization"
            ]
    },

    {
        "query":
            "medical records required",

        "expected_keywords":
            [
                "medical records"
            ]
    },

    {
        "query":
            "clinical necessity",

        "expected_keywords":
            [
                "clinical necessity"
            ]
    }

]

passed_tests = 0

print("\n===== POLICY RETRIEVAL EVALUATION =====")

for test_case in test_cases:

    query = (
        test_case["query"]
    )

    expected_keywords = (
        test_case["expected_keywords"]
    )

    results = (
        policy_service.retrieve(
            query
        )
    )

    combined_text = (
        " ".join(results)
    ).lower()

    success = True

    for keyword in expected_keywords:

        if keyword.lower() not in combined_text:

            success = False

            print(
                f"Missing keyword: {keyword}"
            )

    if success:

        passed_tests += 1

        print(
            f"{query}: PASS"
        )

    else:

        print(
            f"{query}: FAIL"
        )

print("\n===================")
print(
    f"Passed {passed_tests}/{len(test_cases)}"
)
print("===================")