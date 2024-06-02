## Example of using CrewAI agents with open source LLM

[Article on Mediumh](https://artem-goncharov.medium.com/how-to-use-open-source-llms-to-power-a-reliable-team-of-ai-agents-c1f7d70a97c7 with full explanation how it works and how to make it run. 

[CrewAI](https://www.crewai.io/)

[CrewAI Github](https://github.com/joaomdmoura/crewAI)

Install LLM server, preferrably [LM Studio](https://lmstudio.ai)

Inside LM Studio download any Instruct model. I personally found Mistral Instruct 0.3 and Phi3 Medium Instruct the most capable ones for the agents use case. 

Clone this repo:
```
git clone git@github.com:madmag77/crewai-article-example.git
cd crewai-article-example
````

**Note: I use my own fork of CrewAI where I've done some changes that allow open source LLMs work more stable. I hope my PRs to main repo will be merged and then I'll change the dependency and readme files.**

Create `.env` file
```
touch .env
```
Open it and add all the requried API Keys:
```
OPENAI_API_BASE = "http://localhost:1234/v1/"
OPENAI_API_KEY = "NA" # don't need it for LM Studio
OPENAI_MODEL_NAME = "model name" # add the full model name here

SERPER_API_KEY = "api key" # you can register at https://serper.dev and get free 2500 searches
```

Install dependendencies
```
poetry install
```

Activate environment
```
poetry shell
```

Run example
```
python example_crew.py
```


