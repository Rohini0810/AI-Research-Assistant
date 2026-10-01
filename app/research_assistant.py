
#import requests
#from langchain_ollama import ChatOllama
#
#
## --------------------------------------------------
## 1. Get repository information from GitHub API
## --------------------------------------------------
#
#url = "https://api.github.com/repos/langchain-ai/langchain"
#
#response = requests.get(url)
#
#if response.status_code != 200:
#    print(f"GitHub API request failed: {response.status_code}")
#    exit()
#
#data = response.json()
#
#
## --------------------------------------------------
## 2. Extract only the information we need
## --------------------------------------------------
#
#research_data = {
#    "repository": data["full_name"],
#    "description": data["description"],
#    "stars": data["stargazers_count"],
#    "forks": data["forks_count"],
#    "language": data["language"],
#    "owner": data["owner"]["login"],
#}
#
#
## --------------------------------------------------
## 3. Initialize local LLM
## --------------------------------------------------
#
#llm = ChatOllama(
#    model="llama3.2:3b",
#    base_url="http://localhost:11434",
#    temperature=0,
#)
#
#
## --------------------------------------------------
## 4. Get question from user
## --------------------------------------------------
#
#user_question = input(
#    "\nWhat would you like to know about this repository? "
#)
#
#
## --------------------------------------------------
## 5. Build prompt
## --------------------------------------------------
#
#prompt = f"""
#You are a research assistant.
#
#Answer the user's question using ONLY the repository
#information provided below.
#
#Repository information:
#{research_data}
#
#User question:
#{user_question}
#
#If the provided information does not contain the answer,
#say:
#
#"The available repository data does not contain this information."
#
#Do not invent facts or make assumptions.
#"""
#
#
## --------------------------------------------------
## 6. Ask the LLM
## --------------------------------------------------
#
#response = llm.invoke(prompt)
#
#
## --------------------------------------------------
## 7. Display answer
## --------------------------------------------------
#
#print("\nResearch Answer:")
#print(response.content)

#Step 4 — Refactor into functions (software-engineering side of AI engineering)

import requests
from langchain_ollama import ChatOllama


def get_repository_data(repository):
    """Fetch repository information from GitHub."""

    url = f"https://api.github.com/repos/{repository}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            raise ValueError(
                "Repository not found. Check the owner/name."
            )

        if response.status_code != 200:
            raise RuntimeError(
                f"GitHub API request failed: "
                f"{response.status_code}"
            )

        return response.json()

    except requests.exceptions.Timeout:
        raise RuntimeError(
            "GitHub API request timed out."
        )

    except requests.exceptions.RequestException as e:
        raise RuntimeError(
            f"Network error while contacting GitHub: {e}"
        )

def extract_research_data(data):
    """Extract and validate the fields required by our application."""

    required_fields = [
        "full_name",
        "description",
        "stargazers_count",
        "forks_count",
        "language",
        "owner",
    ]

    for field in required_fields:
        if field not in data:
            raise ValueError(
                f"Expected field '{field}' was not found in API response."
            )

    if "login" not in data["owner"]:
        raise ValueError(
            "Expected owner login was not found in API response."
        )

    return {
        "repository": data["full_name"],
        "description": data["description"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "language": data["language"],
        "owner": data["owner"]["login"],
    }
      
def create_llm():
    """Create the local Ollama LLM."""

    return ChatOllama(
        model="llama3.2:3b",
        base_url="http://localhost:11434",
        temperature=0,
    )


def ask_llm(llm, research_data, user_question):
    """Generate an answer using only the retrieved information."""

    prompt = f"""
    You are a research assistant.

    Answer the user's question using ONLY the repository
    information provided below.

    Repository information:
    {research_data}

    User question:
    {user_question}

    If the provided information does not contain the answer,
    say:

    "The available repository data does not contain this information."

    Do not invent facts or make assumptions.
    """

    response = llm.invoke(prompt)

    return response.content


def main():

    repository = input(
        "Enter GitHub repository (owner/name): "
    )

    print("\nFetching repository information...")

    try:
        data = get_repository_data(repository)

        research_data = extract_research_data(data)

        llm = create_llm()

        user_question = input(
            "\nWhat would you like to know about this repository? "
        )

        answer = ask_llm(
            llm,
            research_data,
            user_question
        )

        print("\nResearch Answer:")
        print(answer)

    except Exception as e:
        print(f"\nError: {e}")
if __name__ == "__main__":
    main()