# Python AI Bootcamp — Level 1: Python Foundations

**Author:** Venkatesan Vetrimurasu  
**YouTube:** Venkat's Tech Lab

Hands-on Python skills you need before starting Machine Learning and Deep Learning.  
Each topic explains the basic idea in plain English first, then shows complete runnable code.

This folder contains:

- `Level1_Python_Foundations_Guide.pdf` — complete guide with explanations + code
- `samples/` — one runnable `.py` file for every topic

---

## How to use

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

2. Install the few extra packages used in later samples:

```bash
pip install requests httpx pydantic pydantic-settings email-validator mypy
```

3. Open the PDF and work through the topics one by one.

4. Run each sample:

```bash
cd samples
python 01_unit_converter.py
python 02_word_counter.py
# ... and so on
```

5. After running a sample, **modify it and break it on purpose**. Then fix it. That is how you really learn.

---

## Topics Checklist

| #  | Topic                                      | Sample File                        | Status |
|----|--------------------------------------------|------------------------------------|--------|
| 1  | Variables, types, f-strings                | `01_unit_converter.py`             | ☐ |
| 2  | Lists, dicts, sets, tuples                 | `02_word_counter.py`               | ☐ |
| 3  | Loops and comprehensions                   | `03_filter_dataset.py`             | ☐ |
| 4  | Functions, *args, **kwargs, lambdas        | `04_calculator.py`                 | ☐ |
| 5  | File I/O (CSV, JSON, TXT) + pathlib        | `05_contact_manager.py`            | ☐ |
| 6  | Error handling and custom exceptions       | `06_safe_reader.py`                | ☐ |
| 7  | OOP and dataclasses                        | `07_dataset_class.py`              | ☐ |
| 8  | Modules, packages, venv, pip / uv          | `08_modules_packages.py`           | ☐ |
| 9  | Reproducibility (seeds, uv)                | `09_reproducibility.py`            | ☐ |
| 10 | Type hints with mypy                       | `10_type_hints.py`                 | ☐ |
| 11 | Pydantic                                   | `11_pydantic_demo.py`              | ☐ |
| 12 | Generators, iterators, decorators          | `12_generators_decorators.py`      | ☐ |
| 13 | Context managers (`with` statement)        | `13_context_managers.py`           | ☐ |
| 14 | collections (defaultdict, deque, NamedTuple)| `14_collections_demo.py`          | ☐ |
| 15 | requests and REST APIs                     | `15_api_demo.py`                   | ☐ |
| 16 | Async with asyncio and httpx               | `16_async_demo.py`                 | ☐ |
| 17 | Simple CLI with argparse                   | `17_train_cli.py`                  | ☐ |

---

## Recommended Practice Order

1. Run the sample exactly as written.
2. Read the explanation in the PDF.
3. Do the **Practice tip** at the end of each topic.
4. Only then move to the next topic.

After finishing all 17 topics, build one small combined project that uses at least 8 of them  
(example: a CLI that fetches data from an API, validates it with Pydantic, saves it as JSON, and prints summary statistics).

---

## Next Level

Once you are comfortable with Level 1, move to **Level 2: Math and Data Tools**  
(NumPy, Pandas, Matplotlib, basic statistics & linear algebra).

---

Happy coding!  
Keep breaking things. Keep fixing them.

---

**Author:** Venkatesan Vetrimurasu  
**YouTube Channel:** Venkat's Tech Lab
