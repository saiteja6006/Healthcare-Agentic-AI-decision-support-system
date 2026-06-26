from app.services.clinical_retrieval_service import (
    RetrievalService
)

retrieval_service = (
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
            "MRI insurance authorization",

        "expected_keywords":
            [
                "prior authorization"
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

total_tests = len(
    test_cases
)

passed_tests = 0

print("\n==============================")
print("RETRIEVAL EVALUATION")
print("==============================")

for test_case in test_cases:

    query = (
        test_case["query"]
    )

    expected_keywords = (
        test_case["expected_keywords"]
    )

    print("\n--------------------------------")
    print(f"Query: {query}")

    results = (
        retrieval_service.retrieve(
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

    # -----------------------
    # Negative Test Case
    # -----------------------

    if expect_no_results:

        if len(results) == 0:

            success = True

        else:

            success = False

            print(
                "Expected no results, but documents were retrieved."
            )

    # -----------------------
    # Positive Test Case
    # -----------------------

    else:

        for keyword in expected_keywords:

            if keyword.lower() not in combined_text:

                success = False

                print(
                    f"Missing keyword: {keyword}"
                )

    # -----------------------
    # PASS / FAIL
    # -----------------------

    if success:

        print("\nPASS")

        passed_tests += 1

    else:

        print("\nFAIL")

print("\n==============================")
print(
    f"Passed {passed_tests}/{total_tests}"
)
print("==============================")