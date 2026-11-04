Day 2 — Python Functions, Arguments, *args, **kwargs
Goal: Understand function argument binding, object references, parameter kinds, and edge cases relevant to Python APIs.

Status: Concepts covered; final implementation exercise and production trade-off review remain.
1. Argument passing and object references
Python binds function parameter names to objects supplied by the caller. Mutating a shared mutable object is visible to the caller; rebinding a local parameter is not.
def append_item(items):
    items.append(10)

data = [1, 2]
append_item(data)
print(data)  # [1, 2, 10]


def replace_local(items):
    items = [10, 20]

replace_local(data)
print(data)  # [1, 2, 10]
- items.append(x) mutates the existing list.
- items = items + [x] creates a new list and rebinds the local name.
- items += [x] mutates a list in place (though += behavior depends on the object's type).
- items[:] = [...] replaces the list's contents while preserving its identity.
- id() and is can help inspect object identity.
2. Positional and keyword arguments
def execute(name, model):
    print(name, model)

execute("Agent", "gpt-4o")
execute(name="Agent", model="gpt-4o")
execute("Agent", model="gpt-4o")
All three are valid. Binding a parameter twice is not:
execute("Agent", name="OtherAgent", model="gpt-4o")  # TypeError
3. *args and iterable unpacking
def execute(name, *tools):
    print(name)
    print(tools)

execute("Agent", "search", "calculator")
# Agent
# ('search', 'calculator')

available_tools = ["search", "calculator"]
execute("Agent", *available_tools)
*tools in a definition collects extra positional arguments into a tuple. *iterable in a call unpacks elements into positional arguments. The name args is only a convention.
4. **kwargs and mapping unpacking
def execute(name, **config):
    print(config)

execute("Agent", timeout=30, retries=3)
# {'timeout': 30, 'retries': 3}
**config in a definition collects unmatched keyword arguments into a dict. **mapping in a call unpacks mapping entries into keyword arguments.
defaults = {"timeout": 10}
overrides = {"timeout": 30}
config = {**defaults, **overrides}
print(config)  # {'timeout': 30}
Dictionary merging permits overlapping keys (later values win). A function call with duplicate keyword bindings raises TypeError instead.
5. Defaults and mutable default arguments
Default expressions are evaluated when the def statement executes, not each time the function is called.
def add_tool(tool, tools=[]):
    tools.append(tool)
    return tools

print(add_tool("search"))      # ['search']
print(add_tool("calculator"))  # ['search', 'calculator']
Both calls share the same default list. Use a sentinel such as None when a fresh list is intended:
def add_tool(tool, tools=None):
    if tools is None:
        tools = []
    tools.append(tool)
    return tools
6. Parameter kinds: / and *
def execute_agent(name, /, model="gpt-4o", *, temperature=0.7):
    print(name, model, temperature)
Parameter	Rule
name	Positional-only (before /)
model	Positional or keyword (between / and *)
temperature	Keyword-only (after *)


execute_agent("Agent", "gpt-4.1", temperature=0.5)  # Valid
execute_agent("Agent", model="gpt-4.1")             # Valid
execute_agent(name="Agent")                         # TypeError
execute_agent("Agent", "gpt-4.1", 0.5)               # TypeError
The markers determine how parameters may be supplied, not whether they are required. Defaults determine whether omission is permitted.
7. Edge case: positional-only names and **kwargs
def execute_agent(name, /, **kwargs):
    print(name)
    print(kwargs)

execute_agent("ResearchAgent", name="CodeAgent")
# ResearchAgent
# {'name': 'CodeAgent'}
The keyword name cannot bind the positional-only parameter, so **kwargs collects it. However:
execute_agent(name="ResearchAgent")
# TypeError: missing required positional argument 'name'
Collecting name into kwargs does not satisfy the required positional-only parameter. If that parameter has a default, the call succeeds:
def execute_agent(name="DefaultAgent", /, **kwargs):
    print(name)
    print(kwargs)

execute_agent(name="ResearchAgent")
# DefaultAgent
# {'name': 'ResearchAgent'}
8. Combined signature
def execute_agent(name, /, *tools, model="gpt-4o", **config):
    return {
        "name": name,
        "tools": tools,
        "model": model,
        "config": config,
    }

result = execute_agent(
    "ResearchAgent",
    "search",
    "calculator",
    model="gpt-4.1",
    timeout=30,
    retries=3,
)

print(result)
# {'name': 'ResearchAgent',
#  'tools': ('search', 'calculator'),
#  'model': 'gpt-4.1',
#  'config': {'timeout': 30, 'retries': 3}}
This is the pending hands-on exercise from the discussion; the implementation above is a reference solution, not a completed user submission.
9. Production implications to review
- Explicit parameters make APIs easier to discover and validate than unconstrained **kwargs.
- Changing an existing parameter from positional-or-keyword to positional-only can break callers using its name.
- Mutable defaults can accidentally retain state between requests or calls.
- Forwarding *args and **kwargs through wrappers requires careful handling of collisions and function signatures.
These trade-offs were identified but not yet fully explored or tested during the session.
Completion checklist
- [x] Explain positional, keyword, variable, and unpacked arguments.
- [x] Predict key binding errors and edge cases with feedback.
- [x] Explain mutable default behavior and object identity.
- [ ] Submit and review the combined implementation exercise.
- [ ] Test failure cases and discuss production API design trade-offs.
Next step: Finish the combined exercise and production review before marking this tracker item complete.