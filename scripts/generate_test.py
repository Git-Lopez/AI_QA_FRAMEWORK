import sys
import os
import json
import glob
import subprocess
import argparse

# Add project root to Python path

sys.path.append(

    os.path.abspath(

        os.path.join(os.path.dirname(__file__), "..")

    )

)

from ai_engine.orchestrator import run_llm_test_generation

# Optional for future Jira integration
# from ai_engine.integrations.jira_client import get_jira_story

# ======================================================
# PLAYWRIGHT TRACE VIEWER
# ======================================================

def open_trace():

    print("\nOpening Playwright Trace Viewer...\n")

    subprocess.Popen([
        "playwright",
        "show-trace",
        "reports/traces/trace.zip"
    ])


# ======================================================
# PYTEST EXECUTION
# ======================================================

def run_pytest(
    open_report=False,
    open_trace_viewer=False
):

    print("\nRunning pytest execution...\n")

    subprocess.run([
        "pytest",
        "tests/ui",
        "-v",
        "-s",
        "--alluredir=reports/allure-results"
    ])

    # -----------------------------------------
    # OPEN ALLURE REPORT
    # -----------------------------------------

    if open_report:

        print("\nOpening Allure report...\n")

        subprocess.Popen([
            "allure",
            "serve",
            "reports/allure-results"
        ])

    # -----------------------------------------
    # OPEN PLAYWRIGHT TRACE VIEWER
    # -----------------------------------------

    if open_trace_viewer:

        open_trace()


# ======================================================
# MAIN EXECUTION
# ======================================================

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # ==================================================
    # INPUT TYPES
    # ==================================================

    parser.add_argument(
        "--input",
        help="Single JSON input file"
    )

    parser.add_argument(
        "--batch",
        help="Folder containing JSON files"
    )

    parser.add_argument(
        "--jira",
        help="Jira story ID"
    )

    # ==================================================
    # EXECUTION OPTIONS
    # ==================================================

    parser.add_argument(
        "--execute",
        action="store_true",
        help="Execute pytest after generation"
    )

    parser.add_argument(
        "--report",
        action="store_true",
        help="Open Allure report after execution"
    )

    parser.add_argument(
        "--trace",
        action="store_true",
        help="Open Playwright trace viewer after execution"
    )

    args = parser.parse_args()

    # ==================================================
    # BATCH MODE
    # ==================================================

    if args.batch:

        json_files = glob.glob(f"{args.batch}/*.json")

        print("\nBatch files detected:")
        print(json_files)

        for file in json_files:

            print(f"\nProcessing: {file}")

            with open(file) as f:

                test_input = json.load(f)

            result = run_llm_test_generation(test_input)

            print("\nGenerated files:")

            for k, v in result.items():

                print(f"{k}: {v}")

    # ==================================================
    # SINGLE JSON INPUT
    # ==================================================

    elif args.input:

        with open(args.input) as f:

            test_input = json.load(f)

        result = run_llm_test_generation(test_input)

        print("\nGenerated files:")

        for k, v in result.items():

            print(f"{k}: {v}")

    # ==================================================
    # JIRA MODE (FUTURE)
    # ==================================================

    elif args.jira:

        print("\nJira integration not yet enabled.\n")

        # Future implementation:
        #
        # test_input = get_jira_story(args.jira)
        # result = run_llm_test_generation(test_input)

    # ==================================================
    # SIMPLE STORY MODE
    # ==================================================

    else:

        if len(sys.argv) > 1:

            story = sys.argv[1]

            test_input = {
                "story": story
            }

            result = run_llm_test_generation(test_input)

            print("\nGenerated files:")

            for k, v in result.items():

                print(f"{k}: {v}")

        else:

            print("\nNo valid input provided.\n")

    # ==================================================
    # EXECUTE TESTS
    # ==================================================

    if args.execute:

        run_pytest(
            open_report=args.report,
            open_trace_viewer=args.trace
        )

    