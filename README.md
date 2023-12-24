# Langchain Example:


getting insights from PDF using Langchain and OpenAI (change the OpenAI_API_KEY with one of yours if you want OpenAI accept your query)


to run jupyter:

jupyter notebook

(Use Control-C to stop this server)

----
pip install -r requirements.txt

python -m pip install jupyter

---
memory profile:

@memory_profiler.profile

python -m memory_profiler main.py

---

from line_profiler_pycharm import profile

@profile

python -m line_profiler main.py.lprof > results.txt
