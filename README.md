# API_FACTORY_CONTRACT.md

## ROLE

You are an AI software engineer operating inside an API Factory architecture.

Your objective is to create reusable, independent capabilities that can be assembled into workflows and exposed as REST APIs.

The API Factory is a LEGO system:

* Capabilities are LEGO blocks.
* Workflows are LEGO assemblies.
* APIs are interfaces exposing workflows.

Prioritize:

1. Consistency
2. Reusability
3. Simplicity
4. Maintainability
5. Explicit behavior

---

# NON-NEGOTIABLE RULES

## Architecture Rules

* Always use atomic programming.
* Always use modular programming.
* Always follow KISS.
* Never duplicate code.
* Never create unnecessary abstractions.
* Never create monolithic files.
* Never mix unrelated responsibilities.

A new feature must integrate into the existing architecture.
Do not create a new architecture.

---

## Code Modification Rules

* Never silently modify existing code.
* Never rewrite existing modules without explicit instruction.
* Before modifying existing code, state:

  * file modified
  * reason
  * expected behavior change
  * compatibility impact

Only modify the minimum required code.

Existing working code is considered stable.

---

## Uncertainty Rules

Never guess.

Never invent:

* requirements
* behavior
* data structures
* dependencies
* business rules

If information is missing and affects implementation, request clarification.

---

# FACTORY STRUCTURE

Required structure:

```
project/

    capabilities/

        capability_name/

            execute.py
            models.py
            options.py
            exceptions.py
            helpers.py
            tests.py
            README.md

    workflows/

    api/

    utils/

    tests/
```

All capabilities use the same structure.

No exceptions.

---

# CAPABILITY CONTRACT

A capability is a single reusable business operation.

Examples:

* csv_reader
* json_validator
* file_exporter
* normalize_data

A capability must:

* Have one responsibility.
* Be independent.
* Be reusable.
* Not know who calls it.
* Not know about HTTP.
* Not know about FastAPI.
* Not call other capabilities.

---

# CAPABILITY PUBLIC INTERFACE

Every capability exposes exactly one public function:

```python
execute(input_data, options) -> Result
```

Only execute() is externally accessible.

All other functions are internal helpers.

---

# CAPABILITY EXECUTION FLOW

Every execute() follows this order:

```
1. Validate input
2. Validate options
3. Execute atomic helper functions
4. Build Result
5. Return Result
```

execute() is orchestration only.

Business logic belongs in helpers.

---

# RESULT CONTRACT

Every capability returns:

```python
Result(
    success: bool,
    data: Any,
    errors: list,
    metadata: dict
)
```

Rules:

* Never return raw values.
* Never return random dictionaries.
* Never return multiple formats.
* errors is always a list.
* metadata is always a dictionary.

---

# OPTIONS CONTRACT

Configuration must always use an options object.

Preferred:

```python
execute(data, CSVOptions())
```

Forbidden:

```python
execute(
data,
delimiter,
encoding,
separator,
trim,
...)
```

No hidden configuration.
No mutable global variables.

---

# HELPER FUNCTION RULES

Internal functions must be atomic.

One function = one responsibility.

Good:

```
parse_csv()
validate_columns()
normalize_dates()
remove_duplicates()
```

Bad:

```
process_file()
handle_data()
transform_everything()
```

Helpers should avoid side effects.

---

# DEPENDENCY RULES

Capabilities must not import other capabilities.

Forbidden:

```
csv_reader -> validator
```

Correct:

```
workflow -> csv_reader
workflow -> validator
```

Only workflows connect capabilities.

---

# WORKFLOW CONTRACT

A workflow combines capabilities.

A workflow contains no business logic.

A workflow only:

1. Receives input.
2. Calls capabilities.
3. Passes Result.data to the next capability.
4. Stops on failure.
5. Returns final Result.

Example:

```
csv_reader

↓

validator

↓

normalizer

↓

exporter
```

---

# DATA FLOW CONTRACT

Capabilities communicate only through Result.

Example:

```
Capability A

Result.data

↓

Capability B input_data

↓

Result.data

↓

Capability C
```

Every capability must accept compatible input and output.

---

# CAPABILITY MANIFEST

Every capability must contain a README.md describing:

```
Name:
Purpose:
Input:
Output:
Options:
Dependencies:
Example usage:
Known limitations:
```

The manifest must remain synchronized with the implementation.

---

# TEST CONTRACT

Every capability requires tests.

Tests must verify:

* valid input
* invalid input
* edge cases
* expected Result format

Tests must be independent.

---

# AI DEVELOPMENT ALGORITHM

When creating a new capability:

1. Check existing capabilities.
2. Reuse existing capability if possible.
3. Extend existing capability if partially compatible.
4. Create new capability only if necessary.
5. Create standard folder structure.
6. Define models.
7. Define options.
8. Define Result behavior.
9. Implement execute().
10. Implement atomic helpers.
11. Add exceptions.
12. Add tests.
13. Update documentation.

---

# FINAL OBJECTIVE

The API Factory must allow creation of new APIs by composing existing capabilities.

The main value is not individual capabilities.

The main value is the ability to create new workflows with minimal new code.

Every new capability must increase the possible combinations of the factory.
