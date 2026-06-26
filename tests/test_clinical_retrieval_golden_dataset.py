from app.services.clinical_retrieval_service import (
    RetrievalService
)

clinical_service = (
    RetrievalService()
)

test_cases = [

    {
        "query":
            "MRI lower back pain after physical therapy",

        "expected_keywords":
            [
                "six weeks",
                "physical therapy"
            ]
    },

    {
        "query":
            "CT imaging trauma",

        "expected_keywords":
            [
                "CT"
            ]
    },

    {
        "query":
            "liver cancer MRI",

        "expected_keywords":
            [],

        "expect_no_results":
            True
    }

]

passed_tests = 0

print("\n===== CLINICAL RETRIEVAL EVALUATION =====")

for test_case in test_cases:

    query = test_case["query"]

    expected_keywords = (
        test_case["expected_keywords"]
    )

    print("\n--------------------------------")
    print(f"Query: {query}")

    results = (
        clinical_service.retrieve(
            query
        )
    )

    print("\nRetrieved Documents:")

    for result in results:

        print("-", result)

    combined_text = (
        " ".join(results)
    ).lower()

    success = True

    expect_no_results = (
        test_case.get(
            "expect_no_results",
            False
        )
    )

    if expect_no_results:

        if len(results) != 0:

            success = False

            print(
                "Expected no results, but documents were retrieved."
            )

    else:

        for keyword in expected_keywords:

            if keyword.lower() not in combined_text:

                success = False

                print(
                    f"Missing keyword: {keyword}"
                )

    if success:

        passed_tests += 1

        print("\nPASS")

    else:

        print("\nFAIL")

print("\n===================")
print(
    f"Passed {passed_tests}/{len(test_cases)}"
)
print("===================")