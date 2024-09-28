# PDM Project Templates

This repository contains project templates for [PDM](https://pdm.fming.dev/), a modern Python package and project manager. These templates can be used to quickly set up Python projects with a predefined structure and configuration.

## Features

- Predefined directory structures for Python projects.
- Customizable templates to suit different types of projects (e.g., applications, libraries, or APIs).

## Available Templates

### 1. Clean Architecture Python Project Template

This template provides a basic structure for Python projects following the Clean Architecture principles. It includes separate directories for applications, contexts, and tests.

```plaintext
my_project
├── src
│   ├── apps
│   |   ├── __init__.py
│   |   └── shared
│   |       ├── __init__.py
|   |       └── api
|   |           ├── __init__.py
|   |           └── v0
|   |               ├── __init__.py
|   |               └── controller.py
│   └── contexts
│       ├── __init__.py
│       └── shared
│           ├── __init__.py
|           ├── domain
|           |   ├── __init__.py
|           |   ├── command_bus
|           |   |   ├── __init__.py
|           |   |   ├── command.py
|           |   |   ├── command_bus.py
|           |   |   └── command_handler.py
|           |   ├── criteria
|           |   |   ├── __init__.py
|           |   |   ├── condition.py
|           |   |   ├── condition_field.py
|           |   |   ├── condition_operator.py
|           |   |   ├── condition_value.py
|           |   |   ├── criteria.py
|           |   |   ├── filter.py
|           |   |   ├── page_number.py
|           |   |   ├── page_size.py
|           |   |   ├── sort.py
|           |   |   ├── sort_direction.py
|           |   |   └── sort_field.py
|           |   ├── event_bus
|           |   |   ├── __init__.py
|           |   |   └── event_bus.py
|           |   ├── query_bus
|           |   |   ├── __init__.py
|           |   |   ├── query.py
|           |   |   ├── query_bus.py
|           |   |   └── query_handler.py
|           |   ├── aggregate_root.py
|           |   ├── domain_event.py
|           |   ├── domain_event_subscriber.py
|           |   ├── domain_event_exception.py
|           |   ├── entity.py
|           |   └── entity_id.py
|           └── infrastructure
|               ├── command_bus
|               |   ├── __init__.py
|               |   └── in_memory_command_bus.py
|               ├── criteria
|               |   ├── __init__.py
|               |   └── criteria_to_sqlalchemy.py
|               ├── event_bus
|               |   ├── __init__.py
|               |   └── domain_event_deserializer.py
|               ├── logger
|               |   ├── __init__.py
|               |   ├── config.py
|               |   └── logger.py
|               └── query_bus
|                   ├── __init__.py
|                   └── in_memory_query_bus.py
|
├── tests
│   ├── __init__.py
│   ├── apps
│   |   └── __init__.py
│   └── contexts
│       ├── __init__.py
│       └── shared
│           ├── __init__.py
|           └── factory
|               ├── __init__.py
|               └── entity_id_factory.py
|
├── .gitignore
└── pyproject.toml
```


## Usage

The templates are branches in this repository, so you have to specify the branch name when using a specific template.
To use one of these templates with PDM, follow these steps:

1. Run `pdm init` with the desired template. For example, to use the `clean-architecture` template:

    ```bash
    pdm init -p my-project https://github.com/damian-ontivero/pdm-templates@clean-architecture
    ```

2. Follow the prompts to set up your project.

## Contributing

If you have ideas for new templates or improvements to existing ones, feel free to contribute! You can submit a pull request or open an issue to discuss changes.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.