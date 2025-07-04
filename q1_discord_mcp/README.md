Directory structure:
└── jlowin-fastmcp/
    ├── README.md
    ├── AGENTS.md
    ├── CLAUDE.md
    ├── justfile
    ├── LICENSE
    ├── pyproject.toml
    ├── uv.lock
    ├── Windows_Notes.md
    ├── .ccignore
    ├── .pre-commit-config.yaml
    ├── .python-version
    ├── docs/
    │   ├── changelog.mdx
    │   ├── docs.json
    │   ├── updates.mdx
    │   ├── clients/
    │   │   ├── client.mdx
    │   │   ├── elicitation.mdx
    │   │   ├── logging.mdx
    │   │   ├── messages.mdx
    │   │   ├── progress.mdx
    │   │   ├── prompts.mdx
    │   │   ├── resources.mdx
    │   │   ├── roots.mdx
    │   │   ├── sampling.mdx
    │   │   ├── tools.mdx
    │   │   ├── transports.mdx
    │   │   └── auth/
    │   │       ├── bearer.mdx
    │   │       └── oauth.mdx
    │   ├── community/
    │   │   ├── README.md
    │   │   └── showcase.mdx
    │   ├── css/
    │   │   ├── banner.css
    │   │   ├── python-sdk.css
    │   │   ├── style.css
    │   │   └── version-badge.css
    │   ├── deployment/
    │   │   ├── asgi.mdx
    │   │   └── running-server.mdx
    │   ├── getting-started/
    │   │   ├── installation.mdx
    │   │   ├── quickstart.mdx
    │   │   └── welcome.mdx
    │   ├── integrations/
    │   │   ├── anthropic.mdx
    │   │   ├── chatgpt.mdx
    │   │   ├── claude-code.mdx
    │   │   ├── claude-desktop.mdx
    │   │   ├── contrib.mdx
    │   │   ├── eunomia-authorization.mdx
    │   │   ├── gemini.mdx
    │   │   └── openai.mdx
    │   ├── patterns/
    │   │   ├── cli.mdx
    │   │   ├── decorating-methods.mdx
    │   │   ├── http-requests.mdx
    │   │   ├── testing.mdx
    │   │   └── tool-transformation.mdx
    │   ├── python-sdk/
    │   │   ├── fastmcp-cli-__init__.mdx
    │   │   ├── fastmcp-cli-claude.mdx
    │   │   ├── fastmcp-cli-cli.mdx
    │   │   ├── fastmcp-cli-run.mdx
    │   │   ├── fastmcp-client-__init__.mdx
    │   │   ├── fastmcp-client-auth-__init__.mdx
    │   │   ├── fastmcp-client-auth-bearer.mdx
    │   │   ├── fastmcp-client-auth-oauth.mdx
    │   │   ├── fastmcp-client-client.mdx
    │   │   ├── fastmcp-client-logging.mdx
    │   │   ├── fastmcp-client-oauth_callback.mdx
    │   │   ├── fastmcp-client-progress.mdx
    │   │   ├── fastmcp-client-roots.mdx
    │   │   ├── fastmcp-client-sampling.mdx
    │   │   ├── fastmcp-client-transports.mdx
    │   │   ├── fastmcp-exceptions.mdx
    │   │   ├── fastmcp-prompts-__init__.mdx
    │   │   ├── fastmcp-prompts-prompt.mdx
    │   │   ├── fastmcp-prompts-prompt_manager.mdx
    │   │   ├── fastmcp-resources-__init__.mdx
    │   │   ├── fastmcp-resources-resource.mdx
    │   │   ├── fastmcp-resources-resource_manager.mdx
    │   │   ├── fastmcp-resources-template.mdx
    │   │   ├── fastmcp-resources-types.mdx
    │   │   ├── fastmcp-server-__init__.mdx
    │   │   ├── fastmcp-server-auth-__init__.mdx
    │   │   ├── fastmcp-server-auth-auth.mdx
    │   │   ├── fastmcp-server-auth-providers-__init__.mdx
    │   │   ├── fastmcp-server-auth-providers-bearer.mdx
    │   │   ├── fastmcp-server-auth-providers-bearer_env.mdx
    │   │   ├── fastmcp-server-auth-providers-in_memory.mdx
    │   │   ├── fastmcp-server-context.mdx
    │   │   ├── fastmcp-server-dependencies.mdx
    │   │   ├── fastmcp-server-http.mdx
    │   │   ├── fastmcp-server-middleware-__init__.mdx
    │   │   ├── fastmcp-server-middleware-error_handling.mdx
    │   │   ├── fastmcp-server-middleware-logging.mdx
    │   │   ├── fastmcp-server-middleware-middleware.mdx
    │   │   ├── fastmcp-server-middleware-rate_limiting.mdx
    │   │   ├── fastmcp-server-middleware-timing.mdx
    │   │   ├── fastmcp-server-middleware.mdx
    │   │   ├── fastmcp-server-openapi.mdx
    │   │   ├── fastmcp-server-proxy.mdx
    │   │   ├── fastmcp-server-server.mdx
    │   │   ├── fastmcp-settings.mdx
    │   │   ├── fastmcp-tools-__init__.mdx
    │   │   ├── fastmcp-tools-tool.mdx
    │   │   ├── fastmcp-tools-tool_manager.mdx
    │   │   ├── fastmcp-tools-tool_transform.mdx
    │   │   ├── fastmcp-utilities-__init__.mdx
    │   │   ├── fastmcp-utilities-cache.mdx
    │   │   ├── fastmcp-utilities-components.mdx
    │   │   ├── fastmcp-utilities-exceptions.mdx
    │   │   ├── fastmcp-utilities-http.mdx
    │   │   ├── fastmcp-utilities-inspect.mdx
    │   │   ├── fastmcp-utilities-json_schema.mdx
    │   │   ├── fastmcp-utilities-logging.mdx
    │   │   ├── fastmcp-utilities-mcp_config.mdx
    │   │   ├── fastmcp-utilities-openapi.mdx
    │   │   ├── fastmcp-utilities-tests.mdx
    │   │   └── fastmcp-utilities-types.mdx
    │   ├── servers/
    │   │   ├── composition.mdx
    │   │   ├── context.mdx
    │   │   ├── elicitation.mdx
    │   │   ├── logging.mdx
    │   │   ├── middleware.mdx
    │   │   ├── openapi.mdx
    │   │   ├── progress.mdx
    │   │   ├── prompts.mdx
    │   │   ├── proxy.mdx
    │   │   ├── resources.mdx
    │   │   ├── sampling.mdx
    │   │   ├── server.mdx
    │   │   ├── tools.mdx
    │   │   └── auth/
    │   │       └── bearer.mdx
    │   ├── snippets/
    │   │   ├── version-badge.mdx
    │   │   └── youtube-embed.mdx
    │   ├── tutorials/
    │   │   ├── create-mcp-server.mdx
    │   │   ├── mcp.mdx
    │   │   └── rest-api.mdx
    │   └── .cursor/
    │       └── rules/
    │           └── mintlify.mdc
    ├── examples/
    │   ├── complex_inputs.py
    │   ├── config_server.py
    │   ├── desktop.py
    │   ├── echo.py
    │   ├── get_file.py
    │   ├── in_memory_proxy_example.py
    │   ├── memory.py
    │   ├── mount_example.py
    │   ├── sampling.py
    │   ├── screenshot.py
    │   ├── serializer.py
    │   ├── simple_echo.py
    │   ├── tags_example.py
    │   ├── text_me.py
    │   ├── atproto_mcp/
    │   │   ├── README.md
    │   │   ├── demo.py
    │   │   ├── pyproject.toml
    │   │   └── src/
    │   │       └── atproto_mcp/
    │   │           ├── __init__.py
    │   │           ├── __main__.py
    │   │           ├── py.typed
    │   │           ├── server.py
    │   │           ├── settings.py
    │   │           ├── types.py
    │   │           └── _atproto/
    │   │               ├── __init__.py
    │   │               ├── _client.py
    │   │               ├── _posts.py
    │   │               ├── _profile.py
    │   │               ├── _read.py
    │   │               └── _social.py
    │   └── smart_home/
    │       ├── README.md
    │       ├── pyproject.toml
    │       ├── uv.lock
    │       └── src/
    │           └── smart_home/
    │               ├── __init__.py
    │               ├── __main__.py
    │               ├── hub.py
    │               ├── py.typed
    │               ├── settings.py
    │               └── lights/
    │                   ├── __init__.py
    │                   ├── hue_utils.py
    │                   └── server.py
    ├── src/
    │   └── fastmcp/
    │       ├── __init__.py
    │       ├── exceptions.py
    │       ├── py.typed
    │       ├── settings.py
    │       ├── cli/
    │       │   ├── __init__.py
    │       │   ├── claude.py
    │       │   ├── cli.py
    │       │   └── run.py
    │       ├── client/
    │       │   ├── __init__.py
    │       │   ├── client.py
    │       │   ├── elicitation.py
    │       │   ├── logging.py
    │       │   ├── messages.py
    │       │   ├── oauth_callback.py
    │       │   ├── progress.py
    │       │   ├── roots.py
    │       │   ├── sampling.py
    │       │   ├── transports.py
    │       │   └── auth/
    │       │       ├── __init__.py
    │       │       ├── bearer.py
    │       │       └── oauth.py
    │       ├── contrib/
    │       │   ├── README.md
    │       │   ├── bulk_tool_caller/
    │       │   │   ├── README.md
    │       │   │   ├── __init__.py
    │       │   │   ├── bulk_tool_caller.py
    │       │   │   └── example.py
    │       │   ├── component_manager/
    │       │   │   ├── README.md
    │       │   │   ├── __init__.py
    │       │   │   ├── component_manager.py
    │       │   │   ├── component_service.py
    │       │   │   └── example.py
    │       │   └── mcp_mixin/
    │       │       ├── README.md
    │       │       ├── __init__.py
    │       │       ├── example.py
    │       │       └── mcp_mixin.py
    │       ├── prompts/
    │       │   ├── __init__.py
    │       │   ├── prompt.py
    │       │   └── prompt_manager.py
    │       ├── resources/
    │       │   ├── __init__.py
    │       │   ├── resource.py
    │       │   ├── resource_manager.py
    │       │   ├── template.py
    │       │   └── types.py
    │       ├── server/
    │       │   ├── __init__.py
    │       │   ├── context.py
    │       │   ├── dependencies.py
    │       │   ├── elicitation.py
    │       │   ├── http.py
    │       │   ├── low_level.py
    │       │   ├── openapi.py
    │       │   ├── proxy.py
    │       │   ├── server.py
    │       │   ├── auth/
    │       │   │   ├── __init__.py
    │       │   │   ├── auth.py
    │       │   │   └── providers/
    │       │   │       ├── __init__.py
    │       │   │       ├── bearer.py
    │       │   │       ├── bearer_env.py
    │       │   │       └── in_memory.py
    │       │   └── middleware/
    │       │       ├── __init__.py
    │       │       ├── error_handling.py
    │       │       ├── logging.py
    │       │       ├── middleware.py
    │       │       ├── rate_limiting.py
    │       │       └── timing.py
    │       ├── tools/
    │       │   ├── __init__.py
    │       │   ├── tool.py
    │       │   ├── tool_manager.py
    │       │   └── tool_transform.py
    │       └── utilities/
    │           ├── __init__.py
    │           ├── cache.py
    │           ├── components.py
    │           ├── exceptions.py
    │           ├── http.py
    │           ├── inspect.py
    │           ├── json_schema.py
    │           ├── json_schema_type.py
    │           ├── logging.py
    │           ├── mcp_config.py
    │           ├── openapi.py
    │           ├── tests.py
    │           └── types.py
    ├── tests/
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── test_examples.py
    │   ├── auth/
    │   │   ├── __init__.py
    │   │   ├── test_oauth_client.py
    │   │   └── providers/
    │   │       ├── test_bearer.py
    │   │       ├── test_bearer_env.py
    │   │       └── test_token_verifier.py
    │   ├── cli/
    │   │   ├── __init__.py
    │   │   ├── test_cli.py
    │   │   └── test_run.py
    │   ├── client/
    │   │   ├── __init__.py
    │   │   ├── test_client.py
    │   │   ├── test_elicitation.py
    │   │   ├── test_logs.py
    │   │   ├── test_notifications.py
    │   │   ├── test_openapi.py
    │   │   ├── test_progress.py
    │   │   ├── test_roots.py
    │   │   ├── test_sampling.py
    │   │   ├── test_sse.py
    │   │   ├── test_stdio.py
    │   │   └── test_streamable_http.py
    │   ├── contrib/
    │   │   ├── __init__.py
    │   │   ├── test_bulk_tool_caller.py
    │   │   ├── test_component_manager.py
    │   │   └── test_mcp_mixin.py
    │   ├── deprecated/
    │   │   ├── __init__.py
    │   │   ├── test_deprecated.py
    │   │   ├── test_mount_import_arg_order.py
    │   │   ├── test_mount_separators.py
    │   │   ├── test_resource_prefixes.py
    │   │   ├── test_route_type_ignore.py
    │   │   └── test_settings.py
    │   ├── prompts/
    │   │   ├── __init__.py
    │   │   ├── test_prompt.py
    │   │   └── test_prompt_manager.py
    │   ├── resources/
    │   │   ├── __init__.py
    │   │   ├── test_file_resources.py
    │   │   ├── test_function_resources.py
    │   │   ├── test_resource_manager.py
    │   │   ├── test_resource_template.py
    │   │   └── test_resources.py
    │   ├── server/
    │   │   ├── __init__.py
    │   │   ├── test_app_state.py
    │   │   ├── test_auth_integration.py
    │   │   ├── test_context.py
    │   │   ├── test_file_server.py
    │   │   ├── test_import_server.py
    │   │   ├── test_logging.py
    │   │   ├── test_mount.py
    │   │   ├── test_proxy.py
    │   │   ├── test_resource_prefix_formats.py
    │   │   ├── test_run_server.py
    │   │   ├── test_server.py
    │   │   ├── test_server_interactions.py
    │   │   ├── test_tool_annotations.py
    │   │   ├── test_tool_exclude_args.py
    │   │   ├── http/
    │   │   │   ├── __init__.py
    │   │   │   ├── test_auth_setup.py
    │   │   │   ├── test_bearer_auth_backend.py
    │   │   │   ├── test_custom_routes.py
    │   │   │   ├── test_http_dependencies.py
    │   │   │   └── test_http_middleware.py
    │   │   ├── middleware/
    │   │   │   ├── __init__.py
    │   │   │   ├── test_error_handling.py
    │   │   │   ├── test_logging.py
    │   │   │   ├── test_middleware.py
    │   │   │   ├── test_rate_limiting.py
    │   │   │   └── test_timing.py
    │   │   └── openapi/
    │   │       ├── __init__.py
    │   │       ├── test_explode_integration.py
    │   │       ├── test_openapi.py
    │   │       ├── test_openapi_path_parameters.py
    │   │       └── test_route_map_fn.py
    │   ├── test_servers/
    │   │   ├── fastmcp_server.py
    │   │   ├── sse.py
    │   │   └── stdio.py
    │   ├── tools/
    │   │   ├── __init__.py
    │   │   ├── test_tool.py
    │   │   ├── test_tool_manager.py
    │   │   └── test_tool_transform.py
    │   └── utilities/
    │       ├── __init__.py
    │       ├── test_cache.py
    │       ├── test_inspect.py
    │       ├── test_json_schema.py
    │       ├── test_json_schema_type.py
    │       ├── test_logging.py
    │       ├── test_mcp_config.py
    │       ├── test_tests.py
    │       ├── test_typeadapter.py
    │       ├── test_types.py
    │       └── openapi/
    │           ├── __init__.py
    │           ├── conftest.py
    │           ├── test_openapi.py
    │           ├── test_openapi_advanced.py
    │           └── test_openapi_fastapi.py
    ├── .cursor/
    │   └── rules/
    │       └── core-mcp-objects.mdc
    └── .github/
        ├── dependabot.yml
        ├── labeler.yml
        ├── release.yml
        ├── ISSUE_TEMPLATE/
        │   ├── bug.yml
        │   ├── config.yml
        │   └── enhancement.yml
        └── workflows/
            ├── labeler.yml
            ├── publish.yml
            ├── run-static.yml
            └── run-tests.yml


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
FILE: README.md
================================================
<div align="center">

<!-- omit in toc -->
# FastMCP v2 🚀

<strong>The fast, Pythonic way to build MCP servers and clients.</strong>

*FastMCP is made with 💙 by [Prefect](https://www.prefect.io/)*

[![Docs](https://img.shields.io/badge/docs-gofastmcp.com-blue)](https://gofastmcp.com)
[![PyPI - Version](https://img.shields.io/pypi/v/fastmcp.svg)](https://pypi.org/project/fastmcp)
[![Tests](https://github.com/jlowin/fastmcp/actions/workflows/run-tests.yml/badge.svg)](https://github.com/jlowin/fastmcp/actions/workflows/run-tests.yml)
[![License](https://img.shields.io/github/license/jlowin/fastmcp.svg)](https://github.com/jlowin/fastmcp/blob/main/LICENSE)

<a href="https://trendshift.io/repositories/13266" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13266" alt="jlowin%2Ffastmcp | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

> [!Note]
>
> #### Beyond the Protocol
>
> FastMCP is the standard framework for working with the Model Context Protocol. FastMCP 1.0 was incorporated into the [official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) in 2024.
>
> This is FastMCP 2.0, the **actively maintained version** that provides a complete toolkit for working with the MCP ecosystem.
>
> FastMCP 2.0 has a comprehensive set of features that go far beyond the core MCP specification, all in service of providing **the simplest path to production**. These include deployment, auth, clients, server proxying and composition, generating servers from REST APIs, dynamic tool rewriting, built-in testing tools, integrations, and more.
>
> Ready to upgrade or get started? Follow the [installation instructions](https://gofastmcp.com/getting-started/installation), which include steps for upgrading from the official MCP SDK.

---

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) is a new, standardized way to provide context and tools to your LLMs, and FastMCP makes building MCP servers and clients simple and intuitive. Create tools, expose resources, define prompts, and connect components with clean, Pythonic code.

```python
# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

Run the server locally:

```bash
fastmcp run server.py
```

### 📚 Documentation

FastMCP's complete documentation is available at **[gofastmcp.com](https://gofastmcp.com)**, including detailed guides, API references, and advanced patterns. This readme provides only a high-level overview.

Documentation is also available in [llms.txt format](https://llmstxt.org/), which is a simple markdown standard that LLMs can consume easily.

There are two ways to access the LLM-friendly documentation:

- [`llms.txt`](https://gofastmcp.com/llms.txt) is essentially a sitemap, listing all the pages in the documentation.
- [`llms-full.txt`](https://gofastmcp.com/llms-full.txt) contains the entire documentation. Note this may exceed the context window of your LLM.

---

<!-- omit in toc -->
## Table of Contents

- [What is MCP?](#what-is-mcp)
- [Why FastMCP?](#why-fastmcp)
- [Installation](#installation)
- [Core Concepts](#core-concepts)
  - [The `FastMCP` Server](#the-fastmcp-server)
  - [Tools](#tools)
  - [Resources \& Templates](#resources--templates)
  - [Prompts](#prompts)
  - [Context](#context)
  - [MCP Clients](#mcp-clients)
- [Advanced Features](#advanced-features)
  - [Proxy Servers](#proxy-servers)
  - [Composing MCP Servers](#composing-mcp-servers)
  - [OpenAPI \& FastAPI Generation](#openapi--fastapi-generation)
  - [Authentication \& Security](#authentication--security)
- [Running Your Server](#running-your-server)
- [Contributing](#contributing)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Unit Tests](#unit-tests)
  - [Static Checks](#static-checks)
  - [Pull Requests](#pull-requests)

---

## What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) lets you build servers that expose data and functionality to LLM applications in a secure, standardized way. It is often described as "the USB-C port for AI", providing a uniform way to connect LLMs to resources they can use. It may be easier to think of it as an API, but specifically designed for LLM interactions. MCP servers can:

- Expose data through **Resources** (think of these sort of like GET endpoints; they are used to load information into the LLM's context)
- Provide functionality through **Tools** (sort of like POST endpoints; they are used to execute code or otherwise produce a side effect)
- Define interaction patterns through **Prompts** (reusable templates for LLM interactions)
- And more!

FastMCP provides a high-level, Pythonic interface for building, managing, and interacting with these servers.

## Why FastMCP?

The MCP protocol is powerful but implementing it involves a lot of boilerplate - server setup, protocol handlers, content types, error management. FastMCP handles all the complex protocol details and server management, so you can focus on building great tools. It's designed to be high-level and Pythonic; in most cases, decorating a function is all you need.

FastMCP 2.0 has evolved into a comprehensive platform that goes far beyond basic protocol implementation. While 1.0 provided server-building capabilities (and is now part of the official MCP SDK), 2.0 offers a complete ecosystem including client libraries, authentication systems, deployment tools, integrations with major AI platforms, testing frameworks, and production-ready infrastructure patterns.

FastMCP aims to be:

🚀 **Fast:** High-level interface means less code and faster development

🍀 **Simple:** Build MCP servers with minimal boilerplate

🐍 **Pythonic:** Feels natural to Python developers

🔍 **Complete:** A comprehensive platform for all MCP use cases, from dev to prod

## Installation

We recommend installing FastMCP with [uv](https://docs.astral.sh/uv/):

```bash
uv pip install fastmcp
```

For full installation instructions, including verification, upgrading from the official MCPSDK, and developer setup, see the [**Installation Guide**](https://gofastmcp.com/getting-started/installation).

## Core Concepts

These are the building blocks for creating MCP servers and clients with FastMCP.

### The `FastMCP` Server

The central object representing your MCP application. It holds your tools, resources, and prompts, manages connections, and can be configured with settings like authentication.

```python
from fastmcp import FastMCP

# Create a server instance
mcp = FastMCP(name="MyAssistantServer")
```

Learn more in the [**FastMCP Server Documentation**](https://gofastmcp.com/servers/fastmcp).

### Tools

Tools allow LLMs to perform actions by executing your Python functions (sync or async). Ideal for computations, API calls, or side effects (like `POST`/`PUT`). FastMCP handles schema generation from type hints and docstrings. Tools can return various types, including text, JSON-serializable objects, and even images or audio aided by the FastMCP media helper classes.

```python
@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b
```

Learn more in the [**Tools Documentation**](https://gofastmcp.com/servers/tools).

### Resources & Templates

Resources expose read-only data sources (like `GET` requests). Use `@mcp.resource("your://uri")`. Use `{placeholders}` in the URI to create dynamic templates that accept parameters, allowing clients to request specific data subsets.

```python
# Static resource
@mcp.resource("config://version")
def get_version(): 
    return "2.0.1"

# Dynamic resource template
@mcp.resource("users://{user_id}/profile")
def get_profile(user_id: int):
    # Fetch profile for user_id...
    return {"name": f"User {user_id}", "status": "active"}
```

Learn more in the [**Resources & Templates Documentation**](https://gofastmcp.com/servers/resources).

### Prompts

Prompts define reusable message templates to guide LLM interactions. Decorate functions with `@mcp.prompt`. Return strings or `Message` objects.

```python
@mcp.prompt
def summarize_request(text: str) -> str:
    """Generate a prompt asking for a summary."""
    return f"Please summarize the following text:\n\n{text}"
```

Learn more in the [**Prompts Documentation**](https://gofastmcp.com/servers/prompts).

### Context

Access MCP session capabilities within your tools, resources, or prompts by adding a `ctx: Context` parameter. Context provides methods for:

- **Logging:** Log messages to MCP clients with `ctx.info()`, `ctx.error()`, etc.
- **LLM Sampling:** Use `ctx.sample()` to request completions from the client's LLM.
- **HTTP Request:** Use `ctx.http_request()` to make HTTP requests to other servers.
- **Resource Access:** Use `ctx.read_resource()` to access resources on the server
- **Progress Reporting:** Use `ctx.report_progress()` to report progress to the client.
- and more...

To access the context, add a parameter annotated as `Context` to any mcp-decorated function. FastMCP will automatically inject the correct context object when the function is called.

```python
from fastmcp import FastMCP, Context

mcp = FastMCP("My MCP Server")

@mcp.tool
async def process_data(uri: str, ctx: Context):
    # Log a message to the client
    await ctx.info(f"Processing {uri}...")

    # Read a resource from the server
    data = await ctx.read_resource(uri)

    # Ask client LLM to summarize the data
    summary = await ctx.sample(f"Summarize: {data.content[:500]}")

    # Return the summary
    return summary.text
```

Learn more in the [**Context Documentation**](https://gofastmcp.com/servers/context).

### MCP Clients

Interact with *any* MCP server programmatically using the `fastmcp.Client`. It supports various transports (Stdio, SSE, In-Memory) and often auto-detects the correct one. The client can also handle advanced patterns like server-initiated **LLM sampling requests** if you provide an appropriate handler.

Critically, the client allows for efficient **in-memory testing** of your servers by connecting directly to a `FastMCP` server instance via the `FastMCPTransport`, eliminating the need for process management or network calls during tests.

```python
from fastmcp import Client

async def main():
    # Connect via stdio to a local script
    async with Client("my_server.py") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"Result: {result.text}")

    # Connect via SSE
    async with Client("http://localhost:8000/sse") as client:
        # ... use the client
        pass
```

To use clients to test servers, use the following pattern:

```python
from fastmcp import FastMCP, Client

mcp = FastMCP("My MCP Server")

async def main():
    # Connect via in-memory transport
    async with Client(mcp) as client:
        # ... use the client
```

FastMCP also supports connecting to multiple servers through a single unified client using the standard MCP configuration format:

```python
from fastmcp import Client

# Standard MCP configuration with multiple servers
config = {
    "mcpServers": {
        "weather": {"url": "https://weather-api.example.com/mcp"},
        "assistant": {"command": "python", "args": ["./assistant_server.py"]}
    }
}

# Create a client that connects to all servers
client = Client(config)

async def main():
    async with client:
        # Access tools and resources with server prefixes
        forecast = await client.call_tool("weather_get_forecast", {"city": "London"})
        answer = await client.call_tool("assistant_answer_question", {"query": "What is MCP?"})
```

Learn more in the [**Client Documentation**](https://gofastmcp.com/clients/client) and [**Transports Documentation**](https://gofastmcp.com/clients/transports).

## Advanced Features

FastMCP introduces powerful ways to structure and deploy your MCP applications.

### Proxy Servers

Create a FastMCP server that acts as an intermediary for another local or remote MCP server using `FastMCP.as_proxy()`. This is especially useful for bridging transports (e.g., remote SSE to local Stdio) or adding a layer of logic to a server you don't control.

Learn more in the [**Proxying Documentation**](https://gofastmcp.com/patterns/proxy).

### Composing MCP Servers

Build modular applications by mounting multiple `FastMCP` instances onto a parent server using `mcp.mount()` (live link) or `mcp.import_server()` (static copy).

Learn more in the [**Composition Documentation**](https://gofastmcp.com/patterns/composition).

### OpenAPI & FastAPI Generation

Automatically generate FastMCP servers from existing OpenAPI specifications (`FastMCP.from_openapi()`) or FastAPI applications (`FastMCP.from_fastapi()`), instantly bringing your web APIs to the MCP ecosystem.

Learn more: [**OpenAPI Integration**](https://gofastmcp.com/servers/openapi#openapi-integration) | [**FastAPI Integration**](https://gofastmcp.com/deployment/asgi#fastapi-integration).

### Authentication & Security

FastMCP provides built-in authentication support to secure both your MCP servers and clients in production environments. Protect your server endpoints from unauthorized access and authenticate your clients against secured MCP servers using industry-standard protocols.

- **Server Protection**: Secure your FastMCP server endpoints with configurable authentication providers
- **Client Authentication**: Connect to authenticated MCP servers with automatic credential management
- **Production Ready**: Support for common authentication patterns used in enterprise environments

Learn more in the **Authentication Documentation** for [servers](https://gofastmcp.com/servers/auth) and [clients](https://gofastmcp.com/clients/auth).

## Running Your Server

The main way to run a FastMCP server is by calling the `run()` method on your server instance:

```python
# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()  # Default: uses STDIO transport
```

FastMCP supports three transport protocols:

**STDIO (Default)**: Best for local tools and command-line scripts.

```python
mcp.run(transport="stdio")  # Default, so transport argument is optional
```

**Streamable HTTP**: Recommended for web deployments.

```python
mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")
```

**SSE**: For compatibility with existing SSE clients.

```python
mcp.run(transport="sse", host="127.0.0.1", port=8000)
```

See the [**Running Server Documentation**](https://gofastmcp.com/deployment/running-server) for more details.

## Contributing

Contributions are the core of open source! We welcome improvements and features.

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (Recommended for environment management)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/jlowin/fastmcp.git 
   cd fastmcp
   ```

2. Create and sync the environment:

   ```bash
   uv sync
   ```

   This installs all dependencies, including dev tools.

3. Activate the virtual environment (e.g., `source .venv/bin/activate` or via your IDE).

### Unit Tests

FastMCP has a comprehensive unit test suite. All PRs must introduce or update tests as appropriate and pass the full suite.

Run tests using pytest:

```bash
pytest
```

or if you want an overview of the code coverage

```bash
uv run pytest --cov=src --cov=examples --cov-report=html
```

### Static Checks

FastMCP uses `pre-commit` for code formatting, linting, and type-checking. All PRs must pass these checks (they run automatically in CI).

Install the hooks locally:

```bash
uv run pre-commit install
```

The hooks will now run automatically on `git commit`. You can also run them manually at any time:

```bash
pre-commit run --all-files
# or via uv
uv run pre-commit run --all-files
```

### Pull Requests

1. Fork the repository on GitHub.
2. Create a feature branch from `main`.
3. Make your changes, including tests and documentation updates.
4. Ensure tests and pre-commit hooks pass.
5. Commit your changes and push to your fork.
6. Open a pull request against the `main` branch of `jlowin/fastmcp`.

Please open an issue or discussion for questions or suggestions before starting significant work!



================================================
FILE: AGENTS.md
================================================
# AGENTS

> **Audience**: LLM-driven engineering agents

This file provides guidance for autonomous coding agents working inside the **FastMCP** repository.

---

## Repository map

| Path             | Purpose                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------- |
| `src/fastmcp/`   | Library source code (Python ≥ 3.10)                                                      |
| `  └─server/`    | Server implementation, `FastMCP`, auth, networking                                       |
| `  └─client/`    | High‑level client SDK + helpers                                                          |
| `  └─resources/` | MCP resources and resource templates                                                     |
| `  └─prompts/`   | Prompt templates                                                                         |
| `  └─tools/`     | Tool implementations                                                                     |
| `tests/`         | Pytest test‑suite                                                                        |
| `docs/`          | Mintlify‑flavoured Markdown, published to [https://gofastmcp.com](https://gofastmcp.com) |
| `examples/`      | Minimal runnable demos                                                                   |

---

## Mandatory dev workflow

```bash
uv sync                              # install dependencies
uv run pre-commit run --all-files    # Ruff + Prettier + Pyright
uv run pytest                        # run full test suite
```

*Tests must pass* and *lint/typing must be clean* before committing.

### Core MCP objects

There are four major MCP object types:

- Tools (`src/tools/`)
- Resources (`src/resources/`)
- Resource Templates (`src/resources/`)
- Prompts (`src/prompts`)

While these have slightly different semantics and implementations, in general changes that affect interactions with any one (like adding tags, importing, etc.) will need to be adopted, applied, and tested on all others. Be sure to look at not only the object definition but also the related `Manager` (e.g. `ToolManager`, `ResourceManager`, and `PromptManager`). Also note that while resources and resource templates are different objects, they both are handled by the `ResourceManager`.

---

## Code conventions

* **Language:** Python ≥ 3.10
* **Style:** Enforced through pre-commit hooks
* **Type-checking:** Fully typed codebase
* **Tests:** Each feature should have corresponding tests

---

## Development guidelines

1. **Set up** the environment:
   ```bash
   uv sync && uv run pre-commit run --all-files
   ```
2. **Run tests**: `uv run pytest` until they pass.
3. **Iterate**: if a command fails, read the output, fix the code, retry.
4. Make the smallest set of changes that achieve the desired outcome.
5. Always read code before modifying it blindly.
6. Follow established patterns and maintain consistency.



================================================
FILE: CLAUDE.md
================================================
# FastMCP Development Guidelines

## Git

This project uses `pre-commit` to run checks on all commits. If your commit doesn't pass the checks, it will not be created. Do not attempt to amend commits to pass checks.

## Documentation

- Documentation uses the Mintlify framework
- Files must be present in docs.json to be included in the documentation

## Testing and Investigation

### In-Memory Transport - Always Preferred

When testing or investigating FastMCP servers, **always prefer the in-memory transport** unless you specifically need HTTP transport features. Pass a FastMCP server directly to a Client to eliminate separate processes and network complexity.

```python
# Create your FastMCP server
mcp = FastMCP("TestServer")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Pass server directly to client - uses in-memory transport
async with Client(mcp) as client:
    result = await client.call_tool("greet", {"name": "World"})
```

### When to Use HTTP Transport

Only use HTTP transport when testing network-specific features. Prefer StreamableHttp over SSE as it's the modern approach.

```python
# Only when network testing is required
async with Client(transport=StreamableHttpTransport(server_url)) as client:
    result = await client.ping()
```

## Development Workflow

- You must always run pre-commit if you open a PR, because it is run as part of a required check.
- When opening PRs, apply labels appropriately for bugs/breaking changes/enhancements/features. Generally, improvements are enhancements (not features) unless told otherwise.
- NEVER modify files in docs/python-sdk/**, as they are auto-generated.
- Use # type: ignore[attr-defined] in unit tests when accessing an MCP result of indeterminate type instead of asserting its type



================================================
FILE: justfile
================================================
# Build the project
build:
    uv sync

# Run tests
test: build
    uv run --frozen pytest -xvs tests

# Run pyright on all files
typecheck:
    uv run --frozen pyright

# Serve documentation locally
docs:
    cd docs && npx mint@latest dev

# Generate API reference documentation for all modules
api-ref-all:
    uvx --with-editable . --refresh-package mdxify mdxify@latest --all --root-module fastmcp --anchor-name "Python SDK" --exclude fastmcp.contrib

# Generate API reference for specific modules (e.g., just api-ref prefect.flows prefect.tasks)
api-ref *MODULES:
    uvx --with-editable . --refresh-package mdxify mdxify@latest {{MODULES}} --root-module fastmcp --anchor-name "Python SDK"

# Clean up API reference documentation
api-ref-clean:
    rm -rf docs/python-sdk

copy-context:
    uvx --with-editable . --refresh-package copychat copychat@latest src/ docs/ -x changelog.mdx -x python-sdk/ -v


================================================
FILE: LICENSE
================================================
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


================================================
FILE: pyproject.toml
================================================
[project]
name = "fastmcp"
dynamic = ["version"]
description = "The fast, Pythonic way to build MCP servers."
authors = [{ name = "Jeremiah Lowin" }]
dependencies = [
    "python-dotenv>=1.1.0",
    "exceptiongroup>=1.2.2",
    "httpx>=0.28.1",
    "mcp>=1.10.0",
    "openapi-pydantic>=0.5.1",
    "rich>=13.9.4",
    "typer>=0.15.2",
    "authlib>=1.5.2",
    "pydantic[email]>=2.11.7",
]
requires-python = ">=3.10"
readme = "README.md"
license = "Apache-2.0"

keywords = [
    "mcp",
    "mcp server",
    "mcp client",
    "model context protocol",
    "fastmcp",
    "llm",
    "agent",
]
classifiers = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Typing :: Typed",
]

[dependency-groups]
dev = [
    "copychat>=0.5.2",
    "dirty-equals>=0.9.0",
    "fastapi>=0.115.12",
    "ipython>=8.12.3",
    "pdbpp>=0.10.3",
    "pre-commit",
    "pyinstrument>=5.0.2",
    "pyright>=1.1.389",
    "pytest>=8.3.3",
    "pytest-asyncio>=0.23.5",
    "pytest-cov>=6.1.1",
    "pytest-env>=1.1.5",
    "pytest-flakefinder",
    "pytest-httpx>=0.35.0",
    "pytest-report>=0.2.1",
    "pytest-timeout>=2.4.0",
    "pytest-xdist>=3.6.1",
    "ruff",
]

[project.scripts]
fastmcp = "fastmcp.cli:app"

[project.urls]
Homepage = "https://gofastmcp.com"
Repository = "https://github.com/jlowin/fastmcp"
Documentation = "https://gofastmcp.com"

[project.optional-dependencies]
websockets = ["websockets>=15.0.1"]


[build-system]
requires = ["hatchling", "uv-dynamic-versioning>=0.7.0"]
build-backend = "hatchling.build"

[tool.hatch.version]
source = "uv-dynamic-versioning"

[tool.hatch.metadata]
allow-direct-references = true

[tool.uv-dynamic-versioning]
vcs = "git"
style = "pep440"
bump = true
fallback-version = "0.0.0"


[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "session"
asyncio_default_test_loop_scope = "session"
# filterwarnings = ["error::DeprecationWarning"]
timeout = 3
env = [
    "FASTMCP_TEST_MODE=1",
    'D:FASTMCP_LOG_LEVEL=DEBUG',
    'D:FASTMCP_ENABLE_RICH_TRACEBACKS=0',
]

[tool.pyright]
include = ["src", "tests"]
exclude = ["**/node_modules", "**/__pycache__", ".venv", ".git", "dist"]
pythonVersion = "3.10"
pythonPlatform = "Darwin"
typeCheckingMode = "basic"
reportMissingImports = true
reportMissingTypeStubs = false
useLibraryCodeForTypes = true
venvPath = "."
venv = ".venv"
strict = ["src/fastmcp/server/server.py"]

[tool.ruff.lint]
extend-select = ["I", "UP"]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "I001", "RUF013"]
# allow imports not at the top of the file
"src/fastmcp/__init__.py" = ["E402"]



================================================
FILE: uv.lock
================================================
version = 1
revision = 2
requires-python = ">=3.10"
resolution-markers = [
    "python_full_version >= '3.11'",
    "python_full_version < '3.11'",
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anyio"
version = "4.9.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "idna" },
    { name = "sniffio" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/95/7d/4c1bd541d4dffa1b52bd83fb8527089e097a106fc90b467a7313b105f840/anyio-4.9.0.tar.gz", hash = "sha256:673c0c244e15788651a4ff38710fea9675823028a6f08a5eda409e0c9840a028", size = 190949, upload-time = "2025-03-17T00:02:54.77Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a1/ee/48ca1a7c89ffec8b6a0c5d02b89c305671d5ffd8d3c94acf8b8c408575bb/anyio-4.9.0-py3-none-any.whl", hash = "sha256:9f76d541cad6e36af7beb62e978876f3b41e3e04f2c1fbf0884604c0a9c4d93c", size = 100916, upload-time = "2025-03-17T00:02:52.713Z" },
]

[[package]]
name = "asttokens"
version = "3.0.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/4a/e7/82da0a03e7ba5141f05cce0d302e6eed121ae055e0456ca228bf693984bc/asttokens-3.0.0.tar.gz", hash = "sha256:0dcd8baa8d62b0c1d118b399b2ddba3c4aff271d0d7a9e0d4c1681c79035bbc7", size = 61978, upload-time = "2024-11-30T04:30:14.439Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/25/8a/c46dcc25341b5bce5472c718902eb3d38600a903b14fa6aeecef3f21a46f/asttokens-3.0.0-py3-none-any.whl", hash = "sha256:e3078351a059199dd5138cb1c706e6430c05eff2ff136af5eb4790f9d28932e2", size = 26918, upload-time = "2024-11-30T04:30:10.946Z" },
]

[[package]]
name = "attrs"
version = "25.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/5a/b0/1367933a8532ee6ff8d63537de4f1177af4bff9f3e829baf7331f595bb24/attrs-25.3.0.tar.gz", hash = "sha256:75d7cefc7fb576747b2c81b4442d4d4a1ce0900973527c011d1030fd3bf4af1b", size = 812032, upload-time = "2025-03-13T11:10:22.779Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/77/06/bb80f5f86020c4551da315d78b3ab75e8228f89f0162f2c3a819e407941a/attrs-25.3.0-py3-none-any.whl", hash = "sha256:427318ce031701fea540783410126f03899a97ffc6f61596ad581ac2e40e3bc3", size = 63815, upload-time = "2025-03-13T11:10:21.14Z" },
]

[[package]]
name = "authlib"
version = "1.6.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "cryptography" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a2/9d/b1e08d36899c12c8b894a44a5583ee157789f26fc4b176f8e4b6217b56e1/authlib-1.6.0.tar.gz", hash = "sha256:4367d32031b7af175ad3a323d571dc7257b7099d55978087ceae4a0d88cd3210", size = 158371, upload-time = "2025-05-23T00:21:45.011Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/84/29/587c189bbab1ccc8c86a03a5d0e13873df916380ef1be461ebe6acebf48d/authlib-1.6.0-py2.py3-none-any.whl", hash = "sha256:91685589498f79e8655e8a8947431ad6288831d643f11c55c2143ffcc738048d", size = 239981, upload-time = "2025-05-23T00:21:43.075Z" },
]

[[package]]
name = "certifi"
version = "2025.6.15"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/73/f7/f14b46d4bcd21092d7d3ccef689615220d8a08fb25e564b65d20738e672e/certifi-2025.6.15.tar.gz", hash = "sha256:d747aa5a8b9bbbb1bb8c22bb13e22bd1f18e9796defa16bab421f7f7a317323b", size = 158753, upload-time = "2025-06-15T02:45:51.329Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/84/ae/320161bd181fc06471eed047ecce67b693fd7515b16d495d8932db763426/certifi-2025.6.15-py3-none-any.whl", hash = "sha256:2e0c7ce7cb5d8f8634ca55d2ba7e6ec2689a2fd6537d8dec1296a477a4910057", size = 157650, upload-time = "2025-06-15T02:45:49.977Z" },
]

[[package]]
name = "cffi"
version = "1.17.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pycparser" },
]
sdist = { url = "https://files.pythonhosted.org/packages/fc/97/c783634659c2920c3fc70419e3af40972dbaf758daa229a7d6ea6135c90d/cffi-1.17.1.tar.gz", hash = "sha256:1c39c6016c32bc48dd54561950ebd6836e1670f2ae46128f67cf49e789c52824", size = 516621, upload-time = "2024-09-04T20:45:21.852Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/90/07/f44ca684db4e4f08a3fdc6eeb9a0d15dc6883efc7b8c90357fdbf74e186c/cffi-1.17.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:df8b1c11f177bc2313ec4b2d46baec87a5f3e71fc8b45dab2ee7cae86d9aba14", size = 182191, upload-time = "2024-09-04T20:43:30.027Z" },
    { url = "https://files.pythonhosted.org/packages/08/fd/cc2fedbd887223f9f5d170c96e57cbf655df9831a6546c1727ae13fa977a/cffi-1.17.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8f2cdc858323644ab277e9bb925ad72ae0e67f69e804f4898c070998d50b1a67", size = 178592, upload-time = "2024-09-04T20:43:32.108Z" },
    { url = "https://files.pythonhosted.org/packages/de/cc/4635c320081c78d6ffc2cab0a76025b691a91204f4aa317d568ff9280a2d/cffi-1.17.1-cp310-cp310-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:edae79245293e15384b51f88b00613ba9f7198016a5948b5dddf4917d4d26382", size = 426024, upload-time = "2024-09-04T20:43:34.186Z" },
    { url = "https://files.pythonhosted.org/packages/b6/7b/3b2b250f3aab91abe5f8a51ada1b717935fdaec53f790ad4100fe2ec64d1/cffi-1.17.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:45398b671ac6d70e67da8e4224a065cec6a93541bb7aebe1b198a61b58c7b702", size = 448188, upload-time = "2024-09-04T20:43:36.286Z" },
    { url = "https://files.pythonhosted.org/packages/d3/48/1b9283ebbf0ec065148d8de05d647a986c5f22586b18120020452fff8f5d/cffi-1.17.1-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:ad9413ccdeda48c5afdae7e4fa2192157e991ff761e7ab8fdd8926f40b160cc3", size = 455571, upload-time = "2024-09-04T20:43:38.586Z" },
    { url = "https://files.pythonhosted.org/packages/40/87/3b8452525437b40f39ca7ff70276679772ee7e8b394934ff60e63b7b090c/cffi-1.17.1-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5da5719280082ac6bd9aa7becb3938dc9f9cbd57fac7d2871717b1feb0902ab6", size = 436687, upload-time = "2024-09-04T20:43:40.084Z" },
    { url = "https://files.pythonhosted.org/packages/8d/fb/4da72871d177d63649ac449aec2e8a29efe0274035880c7af59101ca2232/cffi-1.17.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2bb1a08b8008b281856e5971307cc386a8e9c5b625ac297e853d36da6efe9c17", size = 446211, upload-time = "2024-09-04T20:43:41.526Z" },
    { url = "https://files.pythonhosted.org/packages/ab/a0/62f00bcb411332106c02b663b26f3545a9ef136f80d5df746c05878f8c4b/cffi-1.17.1-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:045d61c734659cc045141be4bae381a41d89b741f795af1dd018bfb532fd0df8", size = 461325, upload-time = "2024-09-04T20:43:43.117Z" },
    { url = "https://files.pythonhosted.org/packages/36/83/76127035ed2e7e27b0787604d99da630ac3123bfb02d8e80c633f218a11d/cffi-1.17.1-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:6883e737d7d9e4899a8a695e00ec36bd4e5e4f18fabe0aca0efe0a4b44cdb13e", size = 438784, upload-time = "2024-09-04T20:43:45.256Z" },
    { url = "https://files.pythonhosted.org/packages/21/81/a6cd025db2f08ac88b901b745c163d884641909641f9b826e8cb87645942/cffi-1.17.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:6b8b4a92e1c65048ff98cfe1f735ef8f1ceb72e3d5f0c25fdb12087a23da22be", size = 461564, upload-time = "2024-09-04T20:43:46.779Z" },
    { url = "https://files.pythonhosted.org/packages/f8/fe/4d41c2f200c4a457933dbd98d3cf4e911870877bd94d9656cc0fcb390681/cffi-1.17.1-cp310-cp310-win32.whl", hash = "sha256:c9c3d058ebabb74db66e431095118094d06abf53284d9c81f27300d0e0d8bc7c", size = 171804, upload-time = "2024-09-04T20:43:48.186Z" },
    { url = "https://files.pythonhosted.org/packages/d1/b6/0b0f5ab93b0df4acc49cae758c81fe4e5ef26c3ae2e10cc69249dfd8b3ab/cffi-1.17.1-cp310-cp310-win_amd64.whl", hash = "sha256:0f048dcf80db46f0098ccac01132761580d28e28bc0f78ae0d58048063317e15", size = 181299, upload-time = "2024-09-04T20:43:49.812Z" },
    { url = "https://files.pythonhosted.org/packages/6b/f4/927e3a8899e52a27fa57a48607ff7dc91a9ebe97399b357b85a0c7892e00/cffi-1.17.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:a45e3c6913c5b87b3ff120dcdc03f6131fa0065027d0ed7ee6190736a74cd401", size = 182264, upload-time = "2024-09-04T20:43:51.124Z" },
    { url = "https://files.pythonhosted.org/packages/6c/f5/6c3a8efe5f503175aaddcbea6ad0d2c96dad6f5abb205750d1b3df44ef29/cffi-1.17.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:30c5e0cb5ae493c04c8b42916e52ca38079f1b235c2f8ae5f4527b963c401caf", size = 178651, upload-time = "2024-09-04T20:43:52.872Z" },
    { url = "https://files.pythonhosted.org/packages/94/dd/a3f0118e688d1b1a57553da23b16bdade96d2f9bcda4d32e7d2838047ff7/cffi-1.17.1-cp311-cp311-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f75c7ab1f9e4aca5414ed4d8e5c0e303a34f4421f8a0d47a4d019ceff0ab6af4", size = 445259, upload-time = "2024-09-04T20:43:56.123Z" },
    { url = "https://files.pythonhosted.org/packages/2e/ea/70ce63780f096e16ce8588efe039d3c4f91deb1dc01e9c73a287939c79a6/cffi-1.17.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a1ed2dd2972641495a3ec98445e09766f077aee98a1c896dcb4ad0d303628e41", size = 469200, upload-time = "2024-09-04T20:43:57.891Z" },
    { url = "https://files.pythonhosted.org/packages/1c/a0/a4fa9f4f781bda074c3ddd57a572b060fa0df7655d2a4247bbe277200146/cffi-1.17.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:46bf43160c1a35f7ec506d254e5c890f3c03648a4dbac12d624e4490a7046cd1", size = 477235, upload-time = "2024-09-04T20:44:00.18Z" },
    { url = "https://files.pythonhosted.org/packages/62/12/ce8710b5b8affbcdd5c6e367217c242524ad17a02fe5beec3ee339f69f85/cffi-1.17.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:a24ed04c8ffd54b0729c07cee15a81d964e6fee0e3d4d342a27b020d22959dc6", size = 459721, upload-time = "2024-09-04T20:44:01.585Z" },
    { url = "https://files.pythonhosted.org/packages/ff/6b/d45873c5e0242196f042d555526f92aa9e0c32355a1be1ff8c27f077fd37/cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:610faea79c43e44c71e1ec53a554553fa22321b65fae24889706c0a84d4ad86d", size = 467242, upload-time = "2024-09-04T20:44:03.467Z" },
    { url = "https://files.pythonhosted.org/packages/1a/52/d9a0e523a572fbccf2955f5abe883cfa8bcc570d7faeee06336fbd50c9fc/cffi-1.17.1-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:a9b15d491f3ad5d692e11f6b71f7857e7835eb677955c00cc0aefcd0669adaf6", size = 477999, upload-time = "2024-09-04T20:44:05.023Z" },
    { url = "https://files.pythonhosted.org/packages/44/74/f2a2460684a1a2d00ca799ad880d54652841a780c4c97b87754f660c7603/cffi-1.17.1-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:de2ea4b5833625383e464549fec1bc395c1bdeeb5f25c4a3a82b5a8c756ec22f", size = 454242, upload-time = "2024-09-04T20:44:06.444Z" },
    { url = "https://files.pythonhosted.org/packages/f8/4a/34599cac7dfcd888ff54e801afe06a19c17787dfd94495ab0c8d35fe99fb/cffi-1.17.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:fc48c783f9c87e60831201f2cce7f3b2e4846bf4d8728eabe54d60700b318a0b", size = 478604, upload-time = "2024-09-04T20:44:08.206Z" },
    { url = "https://files.pythonhosted.org/packages/34/33/e1b8a1ba29025adbdcda5fb3a36f94c03d771c1b7b12f726ff7fef2ebe36/cffi-1.17.1-cp311-cp311-win32.whl", hash = "sha256:85a950a4ac9c359340d5963966e3e0a94a676bd6245a4b55bc43949eee26a655", size = 171727, upload-time = "2024-09-04T20:44:09.481Z" },
    { url = "https://files.pythonhosted.org/packages/3d/97/50228be003bb2802627d28ec0627837ac0bf35c90cf769812056f235b2d1/cffi-1.17.1-cp311-cp311-win_amd64.whl", hash = "sha256:caaf0640ef5f5517f49bc275eca1406b0ffa6aa184892812030f04c2abf589a0", size = 181400, upload-time = "2024-09-04T20:44:10.873Z" },
    { url = "https://files.pythonhosted.org/packages/5a/84/e94227139ee5fb4d600a7a4927f322e1d4aea6fdc50bd3fca8493caba23f/cffi-1.17.1-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:805b4371bf7197c329fcb3ead37e710d1bca9da5d583f5073b799d5c5bd1eee4", size = 183178, upload-time = "2024-09-04T20:44:12.232Z" },
    { url = "https://files.pythonhosted.org/packages/da/ee/fb72c2b48656111c4ef27f0f91da355e130a923473bf5ee75c5643d00cca/cffi-1.17.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:733e99bc2df47476e3848417c5a4540522f234dfd4ef3ab7fafdf555b082ec0c", size = 178840, upload-time = "2024-09-04T20:44:13.739Z" },
    { url = "https://files.pythonhosted.org/packages/cc/b6/db007700f67d151abadf508cbfd6a1884f57eab90b1bb985c4c8c02b0f28/cffi-1.17.1-cp312-cp312-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:1257bdabf294dceb59f5e70c64a3e2f462c30c7ad68092d01bbbfb1c16b1ba36", size = 454803, upload-time = "2024-09-04T20:44:15.231Z" },
    { url = "https://files.pythonhosted.org/packages/1a/df/f8d151540d8c200eb1c6fba8cd0dfd40904f1b0682ea705c36e6c2e97ab3/cffi-1.17.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:da95af8214998d77a98cc14e3a3bd00aa191526343078b530ceb0bd710fb48a5", size = 478850, upload-time = "2024-09-04T20:44:17.188Z" },
    { url = "https://files.pythonhosted.org/packages/28/c0/b31116332a547fd2677ae5b78a2ef662dfc8023d67f41b2a83f7c2aa78b1/cffi-1.17.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d63afe322132c194cf832bfec0dc69a99fb9bb6bbd550f161a49e9e855cc78ff", size = 485729, upload-time = "2024-09-04T20:44:18.688Z" },
    { url = "https://files.pythonhosted.org/packages/91/2b/9a1ddfa5c7f13cab007a2c9cc295b70fbbda7cb10a286aa6810338e60ea1/cffi-1.17.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f79fc4fc25f1c8698ff97788206bb3c2598949bfe0fef03d299eb1b5356ada99", size = 471256, upload-time = "2024-09-04T20:44:20.248Z" },
    { url = "https://files.pythonhosted.org/packages/b2/d5/da47df7004cb17e4955df6a43d14b3b4ae77737dff8bf7f8f333196717bf/cffi-1.17.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b62ce867176a75d03a665bad002af8e6d54644fad99a3c70905c543130e39d93", size = 479424, upload-time = "2024-09-04T20:44:21.673Z" },
    { url = "https://files.pythonhosted.org/packages/0b/ac/2a28bcf513e93a219c8a4e8e125534f4f6db03e3179ba1c45e949b76212c/cffi-1.17.1-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:386c8bf53c502fff58903061338ce4f4950cbdcb23e2902d86c0f722b786bbe3", size = 484568, upload-time = "2024-09-04T20:44:23.245Z" },
    { url = "https://files.pythonhosted.org/packages/d4/38/ca8a4f639065f14ae0f1d9751e70447a261f1a30fa7547a828ae08142465/cffi-1.17.1-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:4ceb10419a9adf4460ea14cfd6bc43d08701f0835e979bf821052f1805850fe8", size = 488736, upload-time = "2024-09-04T20:44:24.757Z" },
    { url = "https://files.pythonhosted.org/packages/86/c5/28b2d6f799ec0bdecf44dced2ec5ed43e0eb63097b0f58c293583b406582/cffi-1.17.1-cp312-cp312-win32.whl", hash = "sha256:a08d7e755f8ed21095a310a693525137cfe756ce62d066e53f502a83dc550f65", size = 172448, upload-time = "2024-09-04T20:44:26.208Z" },
    { url = "https://files.pythonhosted.org/packages/50/b9/db34c4755a7bd1cb2d1603ac3863f22bcecbd1ba29e5ee841a4bc510b294/cffi-1.17.1-cp312-cp312-win_amd64.whl", hash = "sha256:51392eae71afec0d0c8fb1a53b204dbb3bcabcb3c9b807eedf3e1e6ccf2de903", size = 181976, upload-time = "2024-09-04T20:44:27.578Z" },
    { url = "https://files.pythonhosted.org/packages/8d/f8/dd6c246b148639254dad4d6803eb6a54e8c85c6e11ec9df2cffa87571dbe/cffi-1.17.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:f3a2b4222ce6b60e2e8b337bb9596923045681d71e5a082783484d845390938e", size = 182989, upload-time = "2024-09-04T20:44:28.956Z" },
    { url = "https://files.pythonhosted.org/packages/8b/f1/672d303ddf17c24fc83afd712316fda78dc6fce1cd53011b839483e1ecc8/cffi-1.17.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:0984a4925a435b1da406122d4d7968dd861c1385afe3b45ba82b750f229811e2", size = 178802, upload-time = "2024-09-04T20:44:30.289Z" },
    { url = "https://files.pythonhosted.org/packages/0e/2d/eab2e858a91fdff70533cab61dcff4a1f55ec60425832ddfdc9cd36bc8af/cffi-1.17.1-cp313-cp313-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d01b12eeeb4427d3110de311e1774046ad344f5b1a7403101878976ecd7a10f3", size = 454792, upload-time = "2024-09-04T20:44:32.01Z" },
    { url = "https://files.pythonhosted.org/packages/75/b2/fbaec7c4455c604e29388d55599b99ebcc250a60050610fadde58932b7ee/cffi-1.17.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:706510fe141c86a69c8ddc029c7910003a17353970cff3b904ff0686a5927683", size = 478893, upload-time = "2024-09-04T20:44:33.606Z" },
    { url = "https://files.pythonhosted.org/packages/4f/b7/6e4a2162178bf1935c336d4da8a9352cccab4d3a5d7914065490f08c0690/cffi-1.17.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:de55b766c7aa2e2a3092c51e0483d700341182f08e67c63630d5b6f200bb28e5", size = 485810, upload-time = "2024-09-04T20:44:35.191Z" },
    { url = "https://files.pythonhosted.org/packages/c7/8a/1d0e4a9c26e54746dc08c2c6c037889124d4f59dffd853a659fa545f1b40/cffi-1.17.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:c59d6e989d07460165cc5ad3c61f9fd8f1b4796eacbd81cee78957842b834af4", size = 471200, upload-time = "2024-09-04T20:44:36.743Z" },
    { url = "https://files.pythonhosted.org/packages/26/9f/1aab65a6c0db35f43c4d1b4f580e8df53914310afc10ae0397d29d697af4/cffi-1.17.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:dd398dbc6773384a17fe0d3e7eeb8d1a21c2200473ee6806bb5e6a8e62bb73dd", size = 479447, upload-time = "2024-09-04T20:44:38.492Z" },
    { url = "https://files.pythonhosted.org/packages/5f/e4/fb8b3dd8dc0e98edf1135ff067ae070bb32ef9d509d6cb0f538cd6f7483f/cffi-1.17.1-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:3edc8d958eb099c634dace3c7e16560ae474aa3803a5df240542b305d14e14ed", size = 484358, upload-time = "2024-09-04T20:44:40.046Z" },
    { url = "https://files.pythonhosted.org/packages/f1/47/d7145bf2dc04684935d57d67dff9d6d795b2ba2796806bb109864be3a151/cffi-1.17.1-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:72e72408cad3d5419375fc87d289076ee319835bdfa2caad331e377589aebba9", size = 488469, upload-time = "2024-09-04T20:44:41.616Z" },
    { url = "https://files.pythonhosted.org/packages/bf/ee/f94057fa6426481d663b88637a9a10e859e492c73d0384514a17d78ee205/cffi-1.17.1-cp313-cp313-win32.whl", hash = "sha256:e03eab0a8677fa80d646b5ddece1cbeaf556c313dcfac435ba11f107ba117b5d", size = 172475, upload-time = "2024-09-04T20:44:43.733Z" },
    { url = "https://files.pythonhosted.org/packages/7c/fc/6a8cb64e5f0324877d503c854da15d76c1e50eb722e320b15345c4d0c6de/cffi-1.17.1-cp313-cp313-win_amd64.whl", hash = "sha256:f6a16c31041f09ead72d69f583767292f750d24913dadacf5756b966aacb3f1a", size = 182009, upload-time = "2024-09-04T20:44:45.309Z" },
]

[[package]]
name = "cfgv"
version = "3.4.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/11/74/539e56497d9bd1d484fd863dd69cbbfa653cd2aa27abfe35653494d85e94/cfgv-3.4.0.tar.gz", hash = "sha256:e52591d4c5f5dead8e0f673fb16db7949d2cfb3f7da4582893288f0ded8fe560", size = 7114, upload-time = "2023-08-12T20:38:17.776Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c5/55/51844dd50c4fc7a33b653bfaba4c2456f06955289ca770a5dbd5fd267374/cfgv-3.4.0-py2.py3-none-any.whl", hash = "sha256:b7265b1f29fd3316bfcd2b330d63d024f2bfd8bcb8b0272f8e19a504856c48f9", size = 7249, upload-time = "2023-08-12T20:38:16.269Z" },
]

[[package]]
name = "charset-normalizer"
version = "3.4.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/e4/33/89c2ced2b67d1c2a61c19c6751aa8902d46ce3dacb23600a283619f5a12d/charset_normalizer-3.4.2.tar.gz", hash = "sha256:5baececa9ecba31eff645232d59845c07aa030f0c81ee70184a90d35099a0e63", size = 126367, upload-time = "2025-05-02T08:34:42.01Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/95/28/9901804da60055b406e1a1c5ba7aac1276fb77f1dde635aabfc7fd84b8ab/charset_normalizer-3.4.2-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:7c48ed483eb946e6c04ccbe02c6b4d1d48e51944b6db70f697e089c193404941", size = 201818, upload-time = "2025-05-02T08:31:46.725Z" },
    { url = "https://files.pythonhosted.org/packages/d9/9b/892a8c8af9110935e5adcbb06d9c6fe741b6bb02608c6513983048ba1a18/charset_normalizer-3.4.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b2d318c11350e10662026ad0eb71bb51c7812fc8590825304ae0bdd4ac283acd", size = 144649, upload-time = "2025-05-02T08:31:48.889Z" },
    { url = "https://files.pythonhosted.org/packages/7b/a5/4179abd063ff6414223575e008593861d62abfc22455b5d1a44995b7c101/charset_normalizer-3.4.2-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9cbfacf36cb0ec2897ce0ebc5d08ca44213af24265bd56eca54bee7923c48fd6", size = 155045, upload-time = "2025-05-02T08:31:50.757Z" },
    { url = "https://files.pythonhosted.org/packages/3b/95/bc08c7dfeddd26b4be8c8287b9bb055716f31077c8b0ea1cd09553794665/charset_normalizer-3.4.2-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:18dd2e350387c87dabe711b86f83c9c78af772c748904d372ade190b5c7c9d4d", size = 147356, upload-time = "2025-05-02T08:31:52.634Z" },
    { url = "https://files.pythonhosted.org/packages/a8/2d/7a5b635aa65284bf3eab7653e8b4151ab420ecbae918d3e359d1947b4d61/charset_normalizer-3.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8075c35cd58273fee266c58c0c9b670947c19df5fb98e7b66710e04ad4e9ff86", size = 149471, upload-time = "2025-05-02T08:31:56.207Z" },
    { url = "https://files.pythonhosted.org/packages/ae/38/51fc6ac74251fd331a8cfdb7ec57beba8c23fd5493f1050f71c87ef77ed0/charset_normalizer-3.4.2-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:5bf4545e3b962767e5c06fe1738f951f77d27967cb2caa64c28be7c4563e162c", size = 151317, upload-time = "2025-05-02T08:31:57.613Z" },
    { url = "https://files.pythonhosted.org/packages/b7/17/edee1e32215ee6e9e46c3e482645b46575a44a2d72c7dfd49e49f60ce6bf/charset_normalizer-3.4.2-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:7a6ab32f7210554a96cd9e33abe3ddd86732beeafc7a28e9955cdf22ffadbab0", size = 146368, upload-time = "2025-05-02T08:31:59.468Z" },
    { url = "https://files.pythonhosted.org/packages/26/2c/ea3e66f2b5f21fd00b2825c94cafb8c326ea6240cd80a91eb09e4a285830/charset_normalizer-3.4.2-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:b33de11b92e9f75a2b545d6e9b6f37e398d86c3e9e9653c4864eb7e89c5773ef", size = 154491, upload-time = "2025-05-02T08:32:01.219Z" },
    { url = "https://files.pythonhosted.org/packages/52/47/7be7fa972422ad062e909fd62460d45c3ef4c141805b7078dbab15904ff7/charset_normalizer-3.4.2-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:8755483f3c00d6c9a77f490c17e6ab0c8729e39e6390328e42521ef175380ae6", size = 157695, upload-time = "2025-05-02T08:32:03.045Z" },
    { url = "https://files.pythonhosted.org/packages/2f/42/9f02c194da282b2b340f28e5fb60762de1151387a36842a92b533685c61e/charset_normalizer-3.4.2-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:68a328e5f55ec37c57f19ebb1fdc56a248db2e3e9ad769919a58672958e8f366", size = 154849, upload-time = "2025-05-02T08:32:04.651Z" },
    { url = "https://files.pythonhosted.org/packages/67/44/89cacd6628f31fb0b63201a618049be4be2a7435a31b55b5eb1c3674547a/charset_normalizer-3.4.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:21b2899062867b0e1fde9b724f8aecb1af14f2778d69aacd1a5a1853a597a5db", size = 150091, upload-time = "2025-05-02T08:32:06.719Z" },
    { url = "https://files.pythonhosted.org/packages/1f/79/4b8da9f712bc079c0f16b6d67b099b0b8d808c2292c937f267d816ec5ecc/charset_normalizer-3.4.2-cp310-cp310-win32.whl", hash = "sha256:e8082b26888e2f8b36a042a58307d5b917ef2b1cacab921ad3323ef91901c71a", size = 98445, upload-time = "2025-05-02T08:32:08.66Z" },
    { url = "https://files.pythonhosted.org/packages/7d/d7/96970afb4fb66497a40761cdf7bd4f6fca0fc7bafde3a84f836c1f57a926/charset_normalizer-3.4.2-cp310-cp310-win_amd64.whl", hash = "sha256:f69a27e45c43520f5487f27627059b64aaf160415589230992cec34c5e18a509", size = 105782, upload-time = "2025-05-02T08:32:10.46Z" },
    { url = "https://files.pythonhosted.org/packages/05/85/4c40d00dcc6284a1c1ad5de5e0996b06f39d8232f1031cd23c2f5c07ee86/charset_normalizer-3.4.2-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:be1e352acbe3c78727a16a455126d9ff83ea2dfdcbc83148d2982305a04714c2", size = 198794, upload-time = "2025-05-02T08:32:11.945Z" },
    { url = "https://files.pythonhosted.org/packages/41/d9/7a6c0b9db952598e97e93cbdfcb91bacd89b9b88c7c983250a77c008703c/charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:aa88ca0b1932e93f2d961bf3addbb2db902198dca337d88c89e1559e066e7645", size = 142846, upload-time = "2025-05-02T08:32:13.946Z" },
    { url = "https://files.pythonhosted.org/packages/66/82/a37989cda2ace7e37f36c1a8ed16c58cf48965a79c2142713244bf945c89/charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d524ba3f1581b35c03cb42beebab4a13e6cdad7b36246bd22541fa585a56cccd", size = 153350, upload-time = "2025-05-02T08:32:15.873Z" },
    { url = "https://files.pythonhosted.org/packages/df/68/a576b31b694d07b53807269d05ec3f6f1093e9545e8607121995ba7a8313/charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:28a1005facc94196e1fb3e82a3d442a9d9110b8434fc1ded7a24a2983c9888d8", size = 145657, upload-time = "2025-05-02T08:32:17.283Z" },
    { url = "https://files.pythonhosted.org/packages/92/9b/ad67f03d74554bed3aefd56fe836e1623a50780f7c998d00ca128924a499/charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fdb20a30fe1175ecabed17cbf7812f7b804b8a315a25f24678bcdf120a90077f", size = 147260, upload-time = "2025-05-02T08:32:18.807Z" },
    { url = "https://files.pythonhosted.org/packages/a6/e6/8aebae25e328160b20e31a7e9929b1578bbdc7f42e66f46595a432f8539e/charset_normalizer-3.4.2-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:0f5d9ed7f254402c9e7d35d2f5972c9bbea9040e99cd2861bd77dc68263277c7", size = 149164, upload-time = "2025-05-02T08:32:20.333Z" },
    { url = "https://files.pythonhosted.org/packages/8b/f2/b3c2f07dbcc248805f10e67a0262c93308cfa149a4cd3d1fe01f593e5fd2/charset_normalizer-3.4.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:efd387a49825780ff861998cd959767800d54f8308936b21025326de4b5a42b9", size = 144571, upload-time = "2025-05-02T08:32:21.86Z" },
    { url = "https://files.pythonhosted.org/packages/60/5b/c3f3a94bc345bc211622ea59b4bed9ae63c00920e2e8f11824aa5708e8b7/charset_normalizer-3.4.2-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:f0aa37f3c979cf2546b73e8222bbfa3dc07a641585340179d768068e3455e544", size = 151952, upload-time = "2025-05-02T08:32:23.434Z" },
    { url = "https://files.pythonhosted.org/packages/e2/4d/ff460c8b474122334c2fa394a3f99a04cf11c646da895f81402ae54f5c42/charset_normalizer-3.4.2-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:e70e990b2137b29dc5564715de1e12701815dacc1d056308e2b17e9095372a82", size = 155959, upload-time = "2025-05-02T08:32:24.993Z" },
    { url = "https://files.pythonhosted.org/packages/a2/2b/b964c6a2fda88611a1fe3d4c400d39c66a42d6c169c924818c848f922415/charset_normalizer-3.4.2-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:0c8c57f84ccfc871a48a47321cfa49ae1df56cd1d965a09abe84066f6853b9c0", size = 153030, upload-time = "2025-05-02T08:32:26.435Z" },
    { url = "https://files.pythonhosted.org/packages/59/2e/d3b9811db26a5ebf444bc0fa4f4be5aa6d76fc6e1c0fd537b16c14e849b6/charset_normalizer-3.4.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:6b66f92b17849b85cad91259efc341dce9c1af48e2173bf38a85c6329f1033e5", size = 148015, upload-time = "2025-05-02T08:32:28.376Z" },
    { url = "https://files.pythonhosted.org/packages/90/07/c5fd7c11eafd561bb51220d600a788f1c8d77c5eef37ee49454cc5c35575/charset_normalizer-3.4.2-cp311-cp311-win32.whl", hash = "sha256:daac4765328a919a805fa5e2720f3e94767abd632ae410a9062dff5412bae65a", size = 98106, upload-time = "2025-05-02T08:32:30.281Z" },
    { url = "https://files.pythonhosted.org/packages/a8/05/5e33dbef7e2f773d672b6d79f10ec633d4a71cd96db6673625838a4fd532/charset_normalizer-3.4.2-cp311-cp311-win_amd64.whl", hash = "sha256:e53efc7c7cee4c1e70661e2e112ca46a575f90ed9ae3fef200f2a25e954f4b28", size = 105402, upload-time = "2025-05-02T08:32:32.191Z" },
    { url = "https://files.pythonhosted.org/packages/d7/a4/37f4d6035c89cac7930395a35cc0f1b872e652eaafb76a6075943754f095/charset_normalizer-3.4.2-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:0c29de6a1a95f24b9a1aa7aefd27d2487263f00dfd55a77719b530788f75cff7", size = 199936, upload-time = "2025-05-02T08:32:33.712Z" },
    { url = "https://files.pythonhosted.org/packages/ee/8a/1a5e33b73e0d9287274f899d967907cd0bf9c343e651755d9307e0dbf2b3/charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cddf7bd982eaa998934a91f69d182aec997c6c468898efe6679af88283b498d3", size = 143790, upload-time = "2025-05-02T08:32:35.768Z" },
    { url = "https://files.pythonhosted.org/packages/66/52/59521f1d8e6ab1482164fa21409c5ef44da3e9f653c13ba71becdd98dec3/charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:fcbe676a55d7445b22c10967bceaaf0ee69407fbe0ece4d032b6eb8d4565982a", size = 153924, upload-time = "2025-05-02T08:32:37.284Z" },
    { url = "https://files.pythonhosted.org/packages/86/2d/fb55fdf41964ec782febbf33cb64be480a6b8f16ded2dbe8db27a405c09f/charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:d41c4d287cfc69060fa91cae9683eacffad989f1a10811995fa309df656ec214", size = 146626, upload-time = "2025-05-02T08:32:38.803Z" },
    { url = "https://files.pythonhosted.org/packages/8c/73/6ede2ec59bce19b3edf4209d70004253ec5f4e319f9a2e3f2f15601ed5f7/charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4e594135de17ab3866138f496755f302b72157d115086d100c3f19370839dd3a", size = 148567, upload-time = "2025-05-02T08:32:40.251Z" },
    { url = "https://files.pythonhosted.org/packages/09/14/957d03c6dc343c04904530b6bef4e5efae5ec7d7990a7cbb868e4595ee30/charset_normalizer-3.4.2-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:cf713fe9a71ef6fd5adf7a79670135081cd4431c2943864757f0fa3a65b1fafd", size = 150957, upload-time = "2025-05-02T08:32:41.705Z" },
    { url = "https://files.pythonhosted.org/packages/0d/c8/8174d0e5c10ccebdcb1b53cc959591c4c722a3ad92461a273e86b9f5a302/charset_normalizer-3.4.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:a370b3e078e418187da8c3674eddb9d983ec09445c99a3a263c2011993522981", size = 145408, upload-time = "2025-05-02T08:32:43.709Z" },
    { url = "https://files.pythonhosted.org/packages/58/aa/8904b84bc8084ac19dc52feb4f5952c6df03ffb460a887b42615ee1382e8/charset_normalizer-3.4.2-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:a955b438e62efdf7e0b7b52a64dc5c3396e2634baa62471768a64bc2adb73d5c", size = 153399, upload-time = "2025-05-02T08:32:46.197Z" },
    { url = "https://files.pythonhosted.org/packages/c2/26/89ee1f0e264d201cb65cf054aca6038c03b1a0c6b4ae998070392a3ce605/charset_normalizer-3.4.2-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:7222ffd5e4de8e57e03ce2cef95a4c43c98fcb72ad86909abdfc2c17d227fc1b", size = 156815, upload-time = "2025-05-02T08:32:48.105Z" },
    { url = "https://files.pythonhosted.org/packages/fd/07/68e95b4b345bad3dbbd3a8681737b4338ff2c9df29856a6d6d23ac4c73cb/charset_normalizer-3.4.2-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:bee093bf902e1d8fc0ac143c88902c3dfc8941f7ea1d6a8dd2bcb786d33db03d", size = 154537, upload-time = "2025-05-02T08:32:49.719Z" },
    { url = "https://files.pythonhosted.org/packages/77/1a/5eefc0ce04affb98af07bc05f3bac9094513c0e23b0562d64af46a06aae4/charset_normalizer-3.4.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:dedb8adb91d11846ee08bec4c8236c8549ac721c245678282dcb06b221aab59f", size = 149565, upload-time = "2025-05-02T08:32:51.404Z" },
    { url = "https://files.pythonhosted.org/packages/37/a0/2410e5e6032a174c95e0806b1a6585eb21e12f445ebe239fac441995226a/charset_normalizer-3.4.2-cp312-cp312-win32.whl", hash = "sha256:db4c7bf0e07fc3b7d89ac2a5880a6a8062056801b83ff56d8464b70f65482b6c", size = 98357, upload-time = "2025-05-02T08:32:53.079Z" },
    { url = "https://files.pythonhosted.org/packages/6c/4f/c02d5c493967af3eda9c771ad4d2bbc8df6f99ddbeb37ceea6e8716a32bc/charset_normalizer-3.4.2-cp312-cp312-win_amd64.whl", hash = "sha256:5a9979887252a82fefd3d3ed2a8e3b937a7a809f65dcb1e068b090e165bbe99e", size = 105776, upload-time = "2025-05-02T08:32:54.573Z" },
    { url = "https://files.pythonhosted.org/packages/ea/12/a93df3366ed32db1d907d7593a94f1fe6293903e3e92967bebd6950ed12c/charset_normalizer-3.4.2-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:926ca93accd5d36ccdabd803392ddc3e03e6d4cd1cf17deff3b989ab8e9dbcf0", size = 199622, upload-time = "2025-05-02T08:32:56.363Z" },
    { url = "https://files.pythonhosted.org/packages/04/93/bf204e6f344c39d9937d3c13c8cd5bbfc266472e51fc8c07cb7f64fcd2de/charset_normalizer-3.4.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:eba9904b0f38a143592d9fc0e19e2df0fa2e41c3c3745554761c5f6447eedabf", size = 143435, upload-time = "2025-05-02T08:32:58.551Z" },
    { url = "https://files.pythonhosted.org/packages/22/2a/ea8a2095b0bafa6c5b5a55ffdc2f924455233ee7b91c69b7edfcc9e02284/charset_normalizer-3.4.2-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3fddb7e2c84ac87ac3a947cb4e66d143ca5863ef48e4a5ecb83bd48619e4634e", size = 153653, upload-time = "2025-05-02T08:33:00.342Z" },
    { url = "https://files.pythonhosted.org/packages/b6/57/1b090ff183d13cef485dfbe272e2fe57622a76694061353c59da52c9a659/charset_normalizer-3.4.2-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:98f862da73774290f251b9df8d11161b6cf25b599a66baf087c1ffe340e9bfd1", size = 146231, upload-time = "2025-05-02T08:33:02.081Z" },
    { url = "https://files.pythonhosted.org/packages/e2/28/ffc026b26f441fc67bd21ab7f03b313ab3fe46714a14b516f931abe1a2d8/charset_normalizer-3.4.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6c9379d65defcab82d07b2a9dfbfc2e95bc8fe0ebb1b176a3190230a3ef0e07c", size = 148243, upload-time = "2025-05-02T08:33:04.063Z" },
    { url = "https://files.pythonhosted.org/packages/c0/0f/9abe9bd191629c33e69e47c6ef45ef99773320e9ad8e9cb08b8ab4a8d4cb/charset_normalizer-3.4.2-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e635b87f01ebc977342e2697d05b56632f5f879a4f15955dfe8cef2448b51691", size = 150442, upload-time = "2025-05-02T08:33:06.418Z" },
    { url = "https://files.pythonhosted.org/packages/67/7c/a123bbcedca91d5916c056407f89a7f5e8fdfce12ba825d7d6b9954a1a3c/charset_normalizer-3.4.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:1c95a1e2902a8b722868587c0e1184ad5c55631de5afc0eb96bc4b0d738092c0", size = 145147, upload-time = "2025-05-02T08:33:08.183Z" },
    { url = "https://files.pythonhosted.org/packages/ec/fe/1ac556fa4899d967b83e9893788e86b6af4d83e4726511eaaad035e36595/charset_normalizer-3.4.2-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:ef8de666d6179b009dce7bcb2ad4c4a779f113f12caf8dc77f0162c29d20490b", size = 153057, upload-time = "2025-05-02T08:33:09.986Z" },
    { url = "https://files.pythonhosted.org/packages/2b/ff/acfc0b0a70b19e3e54febdd5301a98b72fa07635e56f24f60502e954c461/charset_normalizer-3.4.2-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:32fc0341d72e0f73f80acb0a2c94216bd704f4f0bce10aedea38f30502b271ff", size = 156454, upload-time = "2025-05-02T08:33:11.814Z" },
    { url = "https://files.pythonhosted.org/packages/92/08/95b458ce9c740d0645feb0e96cea1f5ec946ea9c580a94adfe0b617f3573/charset_normalizer-3.4.2-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:289200a18fa698949d2b39c671c2cc7a24d44096784e76614899a7ccf2574b7b", size = 154174, upload-time = "2025-05-02T08:33:13.707Z" },
    { url = "https://files.pythonhosted.org/packages/78/be/8392efc43487ac051eee6c36d5fbd63032d78f7728cb37aebcc98191f1ff/charset_normalizer-3.4.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4a476b06fbcf359ad25d34a057b7219281286ae2477cc5ff5e3f70a246971148", size = 149166, upload-time = "2025-05-02T08:33:15.458Z" },
    { url = "https://files.pythonhosted.org/packages/44/96/392abd49b094d30b91d9fbda6a69519e95802250b777841cf3bda8fe136c/charset_normalizer-3.4.2-cp313-cp313-win32.whl", hash = "sha256:aaeeb6a479c7667fbe1099af9617c83aaca22182d6cf8c53966491a0f1b7ffb7", size = 98064, upload-time = "2025-05-02T08:33:17.06Z" },
    { url = "https://files.pythonhosted.org/packages/e9/b0/0200da600134e001d91851ddc797809e2fe0ea72de90e09bec5a2fbdaccb/charset_normalizer-3.4.2-cp313-cp313-win_amd64.whl", hash = "sha256:aa6af9e7d59f9c12b33ae4e9450619cf2488e2bbe9b44030905877f0b2324980", size = 105641, upload-time = "2025-05-02T08:33:18.753Z" },
    { url = "https://files.pythonhosted.org/packages/20/94/c5790835a017658cbfabd07f3bfb549140c3ac458cfc196323996b10095a/charset_normalizer-3.4.2-py3-none-any.whl", hash = "sha256:7f56930ab0abd1c45cd15be65cc741c28b1c9a34876ce8c17a2fa107810c0af0", size = 52626, upload-time = "2025-05-02T08:34:40.053Z" },
]

[[package]]
name = "click"
version = "8.2.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/60/6c/8ca2efa64cf75a977a0d7fac081354553ebe483345c734fb6b6515d96bbc/click-8.2.1.tar.gz", hash = "sha256:27c491cc05d968d271d5a1db13e3b5a184636d9d930f148c50b038f0d0646202", size = 286342, upload-time = "2025-05-20T23:19:49.832Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/85/32/10bb5764d90a8eee674e9dc6f4db6a0ab47c8c4d0d83c27f7c39ac415a4d/click-8.2.1-py3-none-any.whl", hash = "sha256:61a3265b914e850b85317d0b3109c7f8cd35a670f963866005d6ef1d5175a12b", size = 102215, upload-time = "2025-05-20T23:19:47.796Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "copychat"
version = "0.7.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "fastmcp" },
    { name = "gitpython" },
    { name = "pathspec" },
    { name = "pyperclip" },
    { name = "rich" },
    { name = "tiktoken" },
    { name = "typer" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d4/77/a72f890207b33eb542e9507a9d167e8ff734080a9d265472d7a774bd46e4/copychat-0.7.2.tar.gz", hash = "sha256:3f8c21039f0f8874fb84d2163e467e2e003ac625d218225800732244c55176fa", size = 95779, upload-time = "2025-06-19T18:20:27.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fb/b7/266a72b4e843c61bffe2082539c7b634bbe42dd47d8110a5c15e3ee8d66a/copychat-0.7.2-py3-none-any.whl", hash = "sha256:ac2dcb86b70abeb5f8483fc6c70695c93c60b4e851a5b57b165edd36f3e15e8c", size = 23920, upload-time = "2025-06-19T18:20:26.405Z" },
]

[[package]]
name = "coverage"
version = "7.9.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/e7/e0/98670a80884f64578f0c22cd70c5e81a6e07b08167721c7487b4d70a7ca0/coverage-7.9.1.tar.gz", hash = "sha256:6cf43c78c4282708a28e466316935ec7489a9c487518a77fa68f716c67909cec", size = 813650, upload-time = "2025-06-13T13:02:28.627Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c1/78/1c1c5ec58f16817c09cbacb39783c3655d54a221b6552f47ff5ac9297603/coverage-7.9.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:cc94d7c5e8423920787c33d811c0be67b7be83c705f001f7180c7b186dcf10ca", size = 212028, upload-time = "2025-06-13T13:00:29.293Z" },
    { url = "https://files.pythonhosted.org/packages/98/db/e91b9076f3a888e3b4ad7972ea3842297a52cc52e73fd1e529856e473510/coverage-7.9.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:16aa0830d0c08a2c40c264cef801db8bc4fc0e1892782e45bcacbd5889270509", size = 212420, upload-time = "2025-06-13T13:00:34.027Z" },
    { url = "https://files.pythonhosted.org/packages/0e/d0/2b3733412954576b0aea0a16c3b6b8fbe95eb975d8bfa10b07359ead4252/coverage-7.9.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cf95981b126f23db63e9dbe4cf65bd71f9a6305696fa5e2262693bc4e2183f5b", size = 241529, upload-time = "2025-06-13T13:00:35.786Z" },
    { url = "https://files.pythonhosted.org/packages/b3/00/5e2e5ae2e750a872226a68e984d4d3f3563cb01d1afb449a17aa819bc2c4/coverage-7.9.1-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f05031cf21699785cd47cb7485f67df619e7bcdae38e0fde40d23d3d0210d3c3", size = 239403, upload-time = "2025-06-13T13:00:37.399Z" },
    { url = "https://files.pythonhosted.org/packages/37/3b/a2c27736035156b0a7c20683afe7df498480c0dfdf503b8c878a21b6d7fb/coverage-7.9.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bb4fbcab8764dc072cb651a4bcda4d11fb5658a1d8d68842a862a6610bd8cfa3", size = 240548, upload-time = "2025-06-13T13:00:39.647Z" },
    { url = "https://files.pythonhosted.org/packages/98/f5/13d5fc074c3c0e0dc80422d9535814abf190f1254d7c3451590dc4f8b18c/coverage-7.9.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:0f16649a7330ec307942ed27d06ee7e7a38417144620bb3d6e9a18ded8a2d3e5", size = 240459, upload-time = "2025-06-13T13:00:40.934Z" },
    { url = "https://files.pythonhosted.org/packages/36/24/24b9676ea06102df824c4a56ffd13dc9da7904478db519efa877d16527d5/coverage-7.9.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:cea0a27a89e6432705fffc178064503508e3c0184b4f061700e771a09de58187", size = 239128, upload-time = "2025-06-13T13:00:42.343Z" },
    { url = "https://files.pythonhosted.org/packages/be/05/242b7a7d491b369ac5fee7908a6e5ba42b3030450f3ad62c645b40c23e0e/coverage-7.9.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:e980b53a959fa53b6f05343afbd1e6f44a23ed6c23c4b4c56c6662bbb40c82ce", size = 239402, upload-time = "2025-06-13T13:00:43.634Z" },
    { url = "https://files.pythonhosted.org/packages/73/e0/4de7f87192fa65c9c8fbaeb75507e124f82396b71de1797da5602898be32/coverage-7.9.1-cp310-cp310-win32.whl", hash = "sha256:70760b4c5560be6ca70d11f8988ee6542b003f982b32f83d5ac0b72476607b70", size = 214518, upload-time = "2025-06-13T13:00:45.622Z" },
    { url = "https://files.pythonhosted.org/packages/d5/ab/5e4e2fe458907d2a65fab62c773671cfc5ac704f1e7a9ddd91996f66e3c2/coverage-7.9.1-cp310-cp310-win_amd64.whl", hash = "sha256:a66e8f628b71f78c0e0342003d53b53101ba4e00ea8dabb799d9dba0abbbcebe", size = 215436, upload-time = "2025-06-13T13:00:47.245Z" },
    { url = "https://files.pythonhosted.org/packages/60/34/fa69372a07d0903a78ac103422ad34db72281c9fc625eba94ac1185da66f/coverage-7.9.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:95c765060e65c692da2d2f51a9499c5e9f5cf5453aeaf1420e3fc847cc060582", size = 212146, upload-time = "2025-06-13T13:00:48.496Z" },
    { url = "https://files.pythonhosted.org/packages/27/f0/da1894915d2767f093f081c42afeba18e760f12fdd7a2f4acbe00564d767/coverage-7.9.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:ba383dc6afd5ec5b7a0d0c23d38895db0e15bcba7fb0fa8901f245267ac30d86", size = 212536, upload-time = "2025-06-13T13:00:51.535Z" },
    { url = "https://files.pythonhosted.org/packages/10/d5/3fc33b06e41e390f88eef111226a24e4504d216ab8e5d1a7089aa5a3c87a/coverage-7.9.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:37ae0383f13cbdcf1e5e7014489b0d71cc0106458878ccde52e8a12ced4298ed", size = 245092, upload-time = "2025-06-13T13:00:52.883Z" },
    { url = "https://files.pythonhosted.org/packages/0a/39/7aa901c14977aba637b78e95800edf77f29f5a380d29768c5b66f258305b/coverage-7.9.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:69aa417a030bf11ec46149636314c24c8d60fadb12fc0ee8f10fda0d918c879d", size = 242806, upload-time = "2025-06-13T13:00:54.571Z" },
    { url = "https://files.pythonhosted.org/packages/43/fc/30e5cfeaf560b1fc1989227adedc11019ce4bb7cce59d65db34fe0c2d963/coverage-7.9.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0a4be2a28656afe279b34d4f91c3e26eccf2f85500d4a4ff0b1f8b54bf807338", size = 244610, upload-time = "2025-06-13T13:00:56.932Z" },
    { url = "https://files.pythonhosted.org/packages/bf/15/cca62b13f39650bc87b2b92bb03bce7f0e79dd0bf2c7529e9fc7393e4d60/coverage-7.9.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:382e7ddd5289f140259b610e5f5c58f713d025cb2f66d0eb17e68d0a94278875", size = 244257, upload-time = "2025-06-13T13:00:58.545Z" },
    { url = "https://files.pythonhosted.org/packages/cd/1a/c0f2abe92c29e1464dbd0ff9d56cb6c88ae2b9e21becdb38bea31fcb2f6c/coverage-7.9.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:e5532482344186c543c37bfad0ee6069e8ae4fc38d073b8bc836fc8f03c9e250", size = 242309, upload-time = "2025-06-13T13:00:59.836Z" },
    { url = "https://files.pythonhosted.org/packages/57/8d/c6fd70848bd9bf88fa90df2af5636589a8126d2170f3aade21ed53f2b67a/coverage-7.9.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:a39d18b3f50cc121d0ce3838d32d58bd1d15dab89c910358ebefc3665712256c", size = 242898, upload-time = "2025-06-13T13:01:02.506Z" },
    { url = "https://files.pythonhosted.org/packages/c2/9e/6ca46c7bff4675f09a66fe2797cd1ad6a24f14c9c7c3b3ebe0470a6e30b8/coverage-7.9.1-cp311-cp311-win32.whl", hash = "sha256:dd24bd8d77c98557880def750782df77ab2b6885a18483dc8588792247174b32", size = 214561, upload-time = "2025-06-13T13:01:04.012Z" },
    { url = "https://files.pythonhosted.org/packages/a1/30/166978c6302010742dabcdc425fa0f938fa5a800908e39aff37a7a876a13/coverage-7.9.1-cp311-cp311-win_amd64.whl", hash = "sha256:6b55ad10a35a21b8015eabddc9ba31eb590f54adc9cd39bcf09ff5349fd52125", size = 215493, upload-time = "2025-06-13T13:01:05.702Z" },
    { url = "https://files.pythonhosted.org/packages/60/07/a6d2342cd80a5be9f0eeab115bc5ebb3917b4a64c2953534273cf9bc7ae6/coverage-7.9.1-cp311-cp311-win_arm64.whl", hash = "sha256:6ad935f0016be24c0e97fc8c40c465f9c4b85cbbe6eac48934c0dc4d2568321e", size = 213869, upload-time = "2025-06-13T13:01:09.345Z" },
    { url = "https://files.pythonhosted.org/packages/68/d9/7f66eb0a8f2fce222de7bdc2046ec41cb31fe33fb55a330037833fb88afc/coverage-7.9.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:a8de12b4b87c20de895f10567639c0797b621b22897b0af3ce4b4e204a743626", size = 212336, upload-time = "2025-06-13T13:01:10.909Z" },
    { url = "https://files.pythonhosted.org/packages/20/20/e07cb920ef3addf20f052ee3d54906e57407b6aeee3227a9c91eea38a665/coverage-7.9.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:5add197315a054e92cee1b5f686a2bcba60c4c3e66ee3de77ace6c867bdee7cb", size = 212571, upload-time = "2025-06-13T13:01:12.518Z" },
    { url = "https://files.pythonhosted.org/packages/78/f8/96f155de7e9e248ca9c8ff1a40a521d944ba48bec65352da9be2463745bf/coverage-7.9.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:600a1d4106fe66f41e5d0136dfbc68fe7200a5cbe85610ddf094f8f22e1b0300", size = 246377, upload-time = "2025-06-13T13:01:14.87Z" },
    { url = "https://files.pythonhosted.org/packages/3e/cf/1d783bd05b7bca5c10ded5f946068909372e94615a4416afadfe3f63492d/coverage-7.9.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:2a876e4c3e5a2a1715a6608906aa5a2e0475b9c0f68343c2ada98110512ab1d8", size = 243394, upload-time = "2025-06-13T13:01:16.23Z" },
    { url = "https://files.pythonhosted.org/packages/02/dd/e7b20afd35b0a1abea09fb3998e1abc9f9bd953bee548f235aebd2b11401/coverage-7.9.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:81f34346dd63010453922c8e628a52ea2d2ccd73cb2487f7700ac531b247c8a5", size = 245586, upload-time = "2025-06-13T13:01:17.532Z" },
    { url = "https://files.pythonhosted.org/packages/4e/38/b30b0006fea9d617d1cb8e43b1bc9a96af11eff42b87eb8c716cf4d37469/coverage-7.9.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:888f8eee13f2377ce86d44f338968eedec3291876b0b8a7289247ba52cb984cd", size = 245396, upload-time = "2025-06-13T13:01:19.164Z" },
    { url = "https://files.pythonhosted.org/packages/31/e4/4d8ec1dc826e16791f3daf1b50943e8e7e1eb70e8efa7abb03936ff48418/coverage-7.9.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:9969ef1e69b8c8e1e70d591f91bbc37fc9a3621e447525d1602801a24ceda898", size = 243577, upload-time = "2025-06-13T13:01:22.433Z" },
    { url = "https://files.pythonhosted.org/packages/25/f4/b0e96c5c38e6e40ef465c4bc7f138863e2909c00e54a331da335faf0d81a/coverage-7.9.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:60c458224331ee3f1a5b472773e4a085cc27a86a0b48205409d364272d67140d", size = 244809, upload-time = "2025-06-13T13:01:24.143Z" },
    { url = "https://files.pythonhosted.org/packages/8a/65/27e0a1fa5e2e5079bdca4521be2f5dabf516f94e29a0defed35ac2382eb2/coverage-7.9.1-cp312-cp312-win32.whl", hash = "sha256:5f646a99a8c2b3ff4c6a6e081f78fad0dde275cd59f8f49dc4eab2e394332e74", size = 214724, upload-time = "2025-06-13T13:01:25.435Z" },
    { url = "https://files.pythonhosted.org/packages/9b/a8/d5b128633fd1a5e0401a4160d02fa15986209a9e47717174f99dc2f7166d/coverage-7.9.1-cp312-cp312-win_amd64.whl", hash = "sha256:30f445f85c353090b83e552dcbbdad3ec84c7967e108c3ae54556ca69955563e", size = 215535, upload-time = "2025-06-13T13:01:27.861Z" },
    { url = "https://files.pythonhosted.org/packages/a3/37/84bba9d2afabc3611f3e4325ee2c6a47cd449b580d4a606b240ce5a6f9bf/coverage-7.9.1-cp312-cp312-win_arm64.whl", hash = "sha256:af41da5dca398d3474129c58cb2b106a5d93bbb196be0d307ac82311ca234342", size = 213904, upload-time = "2025-06-13T13:01:29.202Z" },
    { url = "https://files.pythonhosted.org/packages/d0/a7/a027970c991ca90f24e968999f7d509332daf6b8c3533d68633930aaebac/coverage-7.9.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:31324f18d5969feef7344a932c32428a2d1a3e50b15a6404e97cba1cc9b2c631", size = 212358, upload-time = "2025-06-13T13:01:30.909Z" },
    { url = "https://files.pythonhosted.org/packages/f2/48/6aaed3651ae83b231556750280682528fea8ac7f1232834573472d83e459/coverage-7.9.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:0c804506d624e8a20fb3108764c52e0eef664e29d21692afa375e0dd98dc384f", size = 212620, upload-time = "2025-06-13T13:01:32.256Z" },
    { url = "https://files.pythonhosted.org/packages/6c/2a/f4b613f3b44d8b9f144847c89151992b2b6b79cbc506dee89ad0c35f209d/coverage-7.9.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ef64c27bc40189f36fcc50c3fb8f16ccda73b6a0b80d9bd6e6ce4cffcd810bbd", size = 245788, upload-time = "2025-06-13T13:01:33.948Z" },
    { url = "https://files.pythonhosted.org/packages/04/d2/de4fdc03af5e4e035ef420ed26a703c6ad3d7a07aff2e959eb84e3b19ca8/coverage-7.9.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d4fe2348cc6ec372e25adec0219ee2334a68d2f5222e0cba9c0d613394e12d86", size = 243001, upload-time = "2025-06-13T13:01:35.285Z" },
    { url = "https://files.pythonhosted.org/packages/f5/e8/eed18aa5583b0423ab7f04e34659e51101135c41cd1dcb33ac1d7013a6d6/coverage-7.9.1-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:34ed2186fe52fcc24d4561041979a0dec69adae7bce2ae8d1c49eace13e55c43", size = 244985, upload-time = "2025-06-13T13:01:36.712Z" },
    { url = "https://files.pythonhosted.org/packages/17/f8/ae9e5cce8885728c934eaa58ebfa8281d488ef2afa81c3dbc8ee9e6d80db/coverage-7.9.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:25308bd3d00d5eedd5ae7d4357161f4df743e3c0240fa773ee1b0f75e6c7c0f1", size = 245152, upload-time = "2025-06-13T13:01:39.303Z" },
    { url = "https://files.pythonhosted.org/packages/5a/c8/272c01ae792bb3af9b30fac14d71d63371db227980682836ec388e2c57c0/coverage-7.9.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:73e9439310f65d55a5a1e0564b48e34f5369bee943d72c88378f2d576f5a5751", size = 243123, upload-time = "2025-06-13T13:01:40.727Z" },
    { url = "https://files.pythonhosted.org/packages/8c/d0/2819a1e3086143c094ab446e3bdf07138527a7b88cb235c488e78150ba7a/coverage-7.9.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:37ab6be0859141b53aa89412a82454b482c81cf750de4f29223d52268a86de67", size = 244506, upload-time = "2025-06-13T13:01:42.184Z" },
    { url = "https://files.pythonhosted.org/packages/8b/4e/9f6117b89152df7b6112f65c7a4ed1f2f5ec8e60c4be8f351d91e7acc848/coverage-7.9.1-cp313-cp313-win32.whl", hash = "sha256:64bdd969456e2d02a8b08aa047a92d269c7ac1f47e0c977675d550c9a0863643", size = 214766, upload-time = "2025-06-13T13:01:44.482Z" },
    { url = "https://files.pythonhosted.org/packages/27/0f/4b59f7c93b52c2c4ce7387c5a4e135e49891bb3b7408dcc98fe44033bbe0/coverage-7.9.1-cp313-cp313-win_amd64.whl", hash = "sha256:be9e3f68ca9edb897c2184ad0eee815c635565dbe7a0e7e814dc1f7cbab92c0a", size = 215568, upload-time = "2025-06-13T13:01:45.772Z" },
    { url = "https://files.pythonhosted.org/packages/09/1e/9679826336f8c67b9c39a359352882b24a8a7aee48d4c9cad08d38d7510f/coverage-7.9.1-cp313-cp313-win_arm64.whl", hash = "sha256:1c503289ffef1d5105d91bbb4d62cbe4b14bec4d13ca225f9c73cde9bb46207d", size = 213939, upload-time = "2025-06-13T13:01:47.087Z" },
    { url = "https://files.pythonhosted.org/packages/bb/5b/5c6b4e7a407359a2e3b27bf9c8a7b658127975def62077d441b93a30dbe8/coverage-7.9.1-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0b3496922cb5f4215bf5caaef4cf12364a26b0be82e9ed6d050f3352cf2d7ef0", size = 213079, upload-time = "2025-06-13T13:01:48.554Z" },
    { url = "https://files.pythonhosted.org/packages/a2/22/1e2e07279fd2fd97ae26c01cc2186e2258850e9ec125ae87184225662e89/coverage-7.9.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:9565c3ab1c93310569ec0d86b017f128f027cab0b622b7af288696d7ed43a16d", size = 213299, upload-time = "2025-06-13T13:01:49.997Z" },
    { url = "https://files.pythonhosted.org/packages/14/c0/4c5125a4b69d66b8c85986d3321520f628756cf524af810baab0790c7647/coverage-7.9.1-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2241ad5dbf79ae1d9c08fe52b36d03ca122fb9ac6bca0f34439e99f8327ac89f", size = 256535, upload-time = "2025-06-13T13:01:51.314Z" },
    { url = "https://files.pythonhosted.org/packages/81/8b/e36a04889dda9960be4263e95e777e7b46f1bb4fc32202612c130a20c4da/coverage-7.9.1-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:3bb5838701ca68b10ebc0937dbd0eb81974bac54447c55cd58dea5bca8451029", size = 252756, upload-time = "2025-06-13T13:01:54.403Z" },
    { url = "https://files.pythonhosted.org/packages/98/82/be04eff8083a09a4622ecd0e1f31a2c563dbea3ed848069e7b0445043a70/coverage-7.9.1-cp313-cp313t-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b30a25f814591a8c0c5372c11ac8967f669b97444c47fd794926e175c4047ece", size = 254912, upload-time = "2025-06-13T13:01:56.769Z" },
    { url = "https://files.pythonhosted.org/packages/0f/25/c26610a2c7f018508a5ab958e5b3202d900422cf7cdca7670b6b8ca4e8df/coverage-7.9.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:2d04b16a6062516df97969f1ae7efd0de9c31eb6ebdceaa0d213b21c0ca1a683", size = 256144, upload-time = "2025-06-13T13:01:58.19Z" },
    { url = "https://files.pythonhosted.org/packages/c5/8b/fb9425c4684066c79e863f1e6e7ecebb49e3a64d9f7f7860ef1688c56f4a/coverage-7.9.1-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:7931b9e249edefb07cd6ae10c702788546341d5fe44db5b6108a25da4dca513f", size = 254257, upload-time = "2025-06-13T13:01:59.645Z" },
    { url = "https://files.pythonhosted.org/packages/93/df/27b882f54157fc1131e0e215b0da3b8d608d9b8ef79a045280118a8f98fe/coverage-7.9.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:52e92b01041151bf607ee858e5a56c62d4b70f4dac85b8c8cb7fb8a351ab2c10", size = 255094, upload-time = "2025-06-13T13:02:01.37Z" },
    { url = "https://files.pythonhosted.org/packages/41/5f/cad1c3dbed8b3ee9e16fa832afe365b4e3eeab1fb6edb65ebbf745eabc92/coverage-7.9.1-cp313-cp313t-win32.whl", hash = "sha256:684e2110ed84fd1ca5f40e89aa44adf1729dc85444004111aa01866507adf363", size = 215437, upload-time = "2025-06-13T13:02:02.905Z" },
    { url = "https://files.pythonhosted.org/packages/99/4d/fad293bf081c0e43331ca745ff63673badc20afea2104b431cdd8c278b4c/coverage-7.9.1-cp313-cp313t-win_amd64.whl", hash = "sha256:437c576979e4db840539674e68c84b3cda82bc824dd138d56bead1435f1cb5d7", size = 216605, upload-time = "2025-06-13T13:02:05.638Z" },
    { url = "https://files.pythonhosted.org/packages/1f/56/4ee027d5965fc7fc126d7ec1187529cc30cc7d740846e1ecb5e92d31b224/coverage-7.9.1-cp313-cp313t-win_arm64.whl", hash = "sha256:18a0912944d70aaf5f399e350445738a1a20b50fbea788f640751c2ed9208b6c", size = 214392, upload-time = "2025-06-13T13:02:07.642Z" },
    { url = "https://files.pythonhosted.org/packages/3e/e5/c723545c3fd3204ebde3b4cc4b927dce709d3b6dc577754bb57f63ca4a4a/coverage-7.9.1-pp39.pp310.pp311-none-any.whl", hash = "sha256:db0f04118d1db74db6c9e1cb1898532c7dcc220f1d2718f058601f7c3f499514", size = 204009, upload-time = "2025-06-13T13:02:25.787Z" },
    { url = "https://files.pythonhosted.org/packages/08/b8/7ddd1e8ba9701dea08ce22029917140e6f66a859427406579fd8d0ca7274/coverage-7.9.1-py3-none-any.whl", hash = "sha256:66b974b145aa189516b6bf2d8423e888b742517d37872f6ee4c5be0073bd9a3c", size = 204000, upload-time = "2025-06-13T13:02:27.173Z" },
]

[package.optional-dependencies]
toml = [
    { name = "tomli", marker = "python_full_version <= '3.11'" },
]

[[package]]
name = "cryptography"
version = "45.0.4"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "cffi", marker = "platform_python_implementation != 'PyPy'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/fe/c8/a2a376a8711c1e11708b9c9972e0c3223f5fc682552c82d8db844393d6ce/cryptography-45.0.4.tar.gz", hash = "sha256:7405ade85c83c37682c8fe65554759800a4a8c54b2d96e0f8ad114d31b808d57", size = 744890, upload-time = "2025-06-10T00:03:51.297Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cc/1c/92637793de053832523b410dbe016d3f5c11b41d0cf6eef8787aabb51d41/cryptography-45.0.4-cp311-abi3-macosx_10_9_universal2.whl", hash = "sha256:425a9a6ac2823ee6e46a76a21a4e8342d8fa5c01e08b823c1f19a8b74f096069", size = 7055712, upload-time = "2025-06-10T00:02:38.826Z" },
    { url = "https://files.pythonhosted.org/packages/ba/14/93b69f2af9ba832ad6618a03f8a034a5851dc9a3314336a3d71c252467e1/cryptography-45.0.4-cp311-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:680806cf63baa0039b920f4976f5f31b10e772de42f16310a6839d9f21a26b0d", size = 4205335, upload-time = "2025-06-10T00:02:41.64Z" },
    { url = "https://files.pythonhosted.org/packages/67/30/fae1000228634bf0b647fca80403db5ca9e3933b91dd060570689f0bd0f7/cryptography-45.0.4-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4ca0f52170e821bc8da6fc0cc565b7bb8ff8d90d36b5e9fdd68e8a86bdf72036", size = 4431487, upload-time = "2025-06-10T00:02:43.696Z" },
    { url = "https://files.pythonhosted.org/packages/6d/5a/7dffcf8cdf0cb3c2430de7404b327e3db64735747d641fc492539978caeb/cryptography-45.0.4-cp311-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:f3fe7a5ae34d5a414957cc7f457e2b92076e72938423ac64d215722f6cf49a9e", size = 4208922, upload-time = "2025-06-10T00:02:45.334Z" },
    { url = "https://files.pythonhosted.org/packages/c6/f3/528729726eb6c3060fa3637253430547fbaaea95ab0535ea41baa4a6fbd8/cryptography-45.0.4-cp311-abi3-manylinux_2_28_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:25eb4d4d3e54595dc8adebc6bbd5623588991d86591a78c2548ffb64797341e2", size = 3900433, upload-time = "2025-06-10T00:02:47.359Z" },
    { url = "https://files.pythonhosted.org/packages/d9/4a/67ba2e40f619e04d83c32f7e1d484c1538c0800a17c56a22ff07d092ccc1/cryptography-45.0.4-cp311-abi3-manylinux_2_28_x86_64.whl", hash = "sha256:ce1678a2ccbe696cf3af15a75bb72ee008d7ff183c9228592ede9db467e64f1b", size = 4464163, upload-time = "2025-06-10T00:02:49.412Z" },
    { url = "https://files.pythonhosted.org/packages/7e/9a/b4d5aa83661483ac372464809c4b49b5022dbfe36b12fe9e323ca8512420/cryptography-45.0.4-cp311-abi3-manylinux_2_34_aarch64.whl", hash = "sha256:49fe9155ab32721b9122975e168a6760d8ce4cffe423bcd7ca269ba41b5dfac1", size = 4208687, upload-time = "2025-06-10T00:02:50.976Z" },
    { url = "https://files.pythonhosted.org/packages/db/b7/a84bdcd19d9c02ec5807f2ec2d1456fd8451592c5ee353816c09250e3561/cryptography-45.0.4-cp311-abi3-manylinux_2_34_x86_64.whl", hash = "sha256:2882338b2a6e0bd337052e8b9007ced85c637da19ef9ecaf437744495c8c2999", size = 4463623, upload-time = "2025-06-10T00:02:52.542Z" },
    { url = "https://files.pythonhosted.org/packages/d8/84/69707d502d4d905021cac3fb59a316344e9f078b1da7fb43ecde5e10840a/cryptography-45.0.4-cp311-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:23b9c3ea30c3ed4db59e7b9619272e94891f8a3a5591d0b656a7582631ccf750", size = 4332447, upload-time = "2025-06-10T00:02:54.63Z" },
    { url = "https://files.pythonhosted.org/packages/f3/ee/d4f2ab688e057e90ded24384e34838086a9b09963389a5ba6854b5876598/cryptography-45.0.4-cp311-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:b0a97c927497e3bc36b33987abb99bf17a9a175a19af38a892dc4bbb844d7ee2", size = 4572830, upload-time = "2025-06-10T00:02:56.689Z" },
    { url = "https://files.pythonhosted.org/packages/70/d4/994773a261d7ff98034f72c0e8251fe2755eac45e2265db4c866c1c6829c/cryptography-45.0.4-cp311-abi3-win32.whl", hash = "sha256:e00a6c10a5c53979d6242f123c0a97cff9f3abed7f064fc412c36dc521b5f257", size = 2932769, upload-time = "2025-06-10T00:02:58.467Z" },
    { url = "https://files.pythonhosted.org/packages/5a/42/c80bd0b67e9b769b364963b5252b17778a397cefdd36fa9aa4a5f34c599a/cryptography-45.0.4-cp311-abi3-win_amd64.whl", hash = "sha256:817ee05c6c9f7a69a16200f0c90ab26d23a87701e2a284bd15156783e46dbcc8", size = 3410441, upload-time = "2025-06-10T00:03:00.14Z" },
    { url = "https://files.pythonhosted.org/packages/ce/0b/2488c89f3a30bc821c9d96eeacfcab6ff3accc08a9601ba03339c0fd05e5/cryptography-45.0.4-cp37-abi3-macosx_10_9_universal2.whl", hash = "sha256:964bcc28d867e0f5491a564b7debb3ffdd8717928d315d12e0d7defa9e43b723", size = 7031836, upload-time = "2025-06-10T00:03:01.726Z" },
    { url = "https://files.pythonhosted.org/packages/fe/51/8c584ed426093aac257462ae62d26ad61ef1cbf5b58d8b67e6e13c39960e/cryptography-45.0.4-cp37-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:6a5bf57554e80f75a7db3d4b1dacaa2764611ae166ab42ea9a72bcdb5d577637", size = 4195746, upload-time = "2025-06-10T00:03:03.94Z" },
    { url = "https://files.pythonhosted.org/packages/5c/7d/4b0ca4d7af95a704eef2f8f80a8199ed236aaf185d55385ae1d1610c03c2/cryptography-45.0.4-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:46cf7088bf91bdc9b26f9c55636492c1cce3e7aaf8041bbf0243f5e5325cfb2d", size = 4424456, upload-time = "2025-06-10T00:03:05.589Z" },
    { url = "https://files.pythonhosted.org/packages/1d/45/5fabacbc6e76ff056f84d9f60eeac18819badf0cefc1b6612ee03d4ab678/cryptography-45.0.4-cp37-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:7bedbe4cc930fa4b100fc845ea1ea5788fcd7ae9562e669989c11618ae8d76ee", size = 4198495, upload-time = "2025-06-10T00:03:09.172Z" },
    { url = "https://files.pythonhosted.org/packages/55/b7/ffc9945b290eb0a5d4dab9b7636706e3b5b92f14ee5d9d4449409d010d54/cryptography-45.0.4-cp37-abi3-manylinux_2_28_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:eaa3e28ea2235b33220b949c5a0d6cf79baa80eab2eb5607ca8ab7525331b9ff", size = 3885540, upload-time = "2025-06-10T00:03:10.835Z" },
    { url = "https://files.pythonhosted.org/packages/7f/e3/57b010282346980475e77d414080acdcb3dab9a0be63071efc2041a2c6bd/cryptography-45.0.4-cp37-abi3-manylinux_2_28_x86_64.whl", hash = "sha256:7ef2dde4fa9408475038fc9aadfc1fb2676b174e68356359632e980c661ec8f6", size = 4452052, upload-time = "2025-06-10T00:03:12.448Z" },
    { url = "https://files.pythonhosted.org/packages/37/e6/ddc4ac2558bf2ef517a358df26f45bc774a99bf4653e7ee34b5e749c03e3/cryptography-45.0.4-cp37-abi3-manylinux_2_34_aarch64.whl", hash = "sha256:6a3511ae33f09094185d111160fd192c67aa0a2a8d19b54d36e4c78f651dc5ad", size = 4198024, upload-time = "2025-06-10T00:03:13.976Z" },
    { url = "https://files.pythonhosted.org/packages/3a/c0/85fa358ddb063ec588aed4a6ea1df57dc3e3bc1712d87c8fa162d02a65fc/cryptography-45.0.4-cp37-abi3-manylinux_2_34_x86_64.whl", hash = "sha256:06509dc70dd71fa56eaa138336244e2fbaf2ac164fc9b5e66828fccfd2b680d6", size = 4451442, upload-time = "2025-06-10T00:03:16.248Z" },
    { url = "https://files.pythonhosted.org/packages/33/67/362d6ec1492596e73da24e669a7fbbaeb1c428d6bf49a29f7a12acffd5dc/cryptography-45.0.4-cp37-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:5f31e6b0a5a253f6aa49be67279be4a7e5a4ef259a9f33c69f7d1b1191939872", size = 4325038, upload-time = "2025-06-10T00:03:18.4Z" },
    { url = "https://files.pythonhosted.org/packages/53/75/82a14bf047a96a1b13ebb47fb9811c4f73096cfa2e2b17c86879687f9027/cryptography-45.0.4-cp37-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:944e9ccf67a9594137f942d5b52c8d238b1b4e46c7a0c2891b7ae6e01e7c80a4", size = 4560964, upload-time = "2025-06-10T00:03:20.06Z" },
    { url = "https://files.pythonhosted.org/packages/cd/37/1a3cba4c5a468ebf9b95523a5ef5651244693dc712001e276682c278fc00/cryptography-45.0.4-cp37-abi3-win32.whl", hash = "sha256:c22fe01e53dc65edd1945a2e6f0015e887f84ced233acecb64b4daadb32f5c97", size = 2924557, upload-time = "2025-06-10T00:03:22.563Z" },
    { url = "https://files.pythonhosted.org/packages/2a/4b/3256759723b7e66380397d958ca07c59cfc3fb5c794fb5516758afd05d41/cryptography-45.0.4-cp37-abi3-win_amd64.whl", hash = "sha256:627ba1bc94f6adf0b0a2e35d87020285ead22d9f648c7e75bb64f367375f3b22", size = 3395508, upload-time = "2025-06-10T00:03:24.586Z" },
    { url = "https://files.pythonhosted.org/packages/16/33/b38e9d372afde56906a23839302c19abdac1c505bfb4776c1e4b07c3e145/cryptography-45.0.4-pp310-pypy310_pp73-macosx_10_9_x86_64.whl", hash = "sha256:a77c6fb8d76e9c9f99f2f3437c1a4ac287b34eaf40997cfab1e9bd2be175ac39", size = 3580103, upload-time = "2025-06-10T00:03:26.207Z" },
    { url = "https://files.pythonhosted.org/packages/c4/b9/357f18064ec09d4807800d05a48f92f3b369056a12f995ff79549fbb31f1/cryptography-45.0.4-pp310-pypy310_pp73-manylinux_2_28_aarch64.whl", hash = "sha256:7aad98a25ed8ac917fdd8a9c1e706e5a0956e06c498be1f713b61734333a4507", size = 4143732, upload-time = "2025-06-10T00:03:27.896Z" },
    { url = "https://files.pythonhosted.org/packages/c4/9c/7f7263b03d5db329093617648b9bd55c953de0b245e64e866e560f9aac07/cryptography-45.0.4-pp310-pypy310_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:3530382a43a0e524bc931f187fc69ef4c42828cf7d7f592f7f249f602b5a4ab0", size = 4385424, upload-time = "2025-06-10T00:03:29.992Z" },
    { url = "https://files.pythonhosted.org/packages/a6/5a/6aa9d8d5073d5acc0e04e95b2860ef2684b2bd2899d8795fc443013e263b/cryptography-45.0.4-pp310-pypy310_pp73-manylinux_2_34_aarch64.whl", hash = "sha256:6b613164cb8425e2f8db5849ffb84892e523bf6d26deb8f9bb76ae86181fa12b", size = 4142438, upload-time = "2025-06-10T00:03:31.782Z" },
    { url = "https://files.pythonhosted.org/packages/42/1c/71c638420f2cdd96d9c2b287fec515faf48679b33a2b583d0f1eda3a3375/cryptography-45.0.4-pp310-pypy310_pp73-manylinux_2_34_x86_64.whl", hash = "sha256:96d4819e25bf3b685199b304a0029ce4a3caf98947ce8a066c9137cc78ad2c58", size = 4384622, upload-time = "2025-06-10T00:03:33.491Z" },
    { url = "https://files.pythonhosted.org/packages/ef/ab/e3a055c34e97deadbf0d846e189237d3385dca99e1a7e27384c3b2292041/cryptography-45.0.4-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:b97737a3ffbea79eebb062eb0d67d72307195035332501722a9ca86bab9e3ab2", size = 3328911, upload-time = "2025-06-10T00:03:35.035Z" },
    { url = "https://files.pythonhosted.org/packages/ea/ba/cf442ae99ef363855ed84b39e0fb3c106ac66b7a7703f3c9c9cfe05412cb/cryptography-45.0.4-pp311-pypy311_pp73-macosx_10_9_x86_64.whl", hash = "sha256:4828190fb6c4bcb6ebc6331f01fe66ae838bb3bd58e753b59d4b22eb444b996c", size = 3590512, upload-time = "2025-06-10T00:03:36.982Z" },
    { url = "https://files.pythonhosted.org/packages/28/9a/a7d5bb87d149eb99a5abdc69a41e4e47b8001d767e5f403f78bfaafc7aa7/cryptography-45.0.4-pp311-pypy311_pp73-manylinux_2_28_aarch64.whl", hash = "sha256:03dbff8411206713185b8cebe31bc5c0eb544799a50c09035733716b386e61a4", size = 4146899, upload-time = "2025-06-10T00:03:38.659Z" },
    { url = "https://files.pythonhosted.org/packages/17/11/9361c2c71c42cc5c465cf294c8030e72fb0c87752bacbd7a3675245e3db3/cryptography-45.0.4-pp311-pypy311_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:51dfbd4d26172d31150d84c19bbe06c68ea4b7f11bbc7b3a5e146b367c311349", size = 4388900, upload-time = "2025-06-10T00:03:40.233Z" },
    { url = "https://files.pythonhosted.org/packages/c0/76/f95b83359012ee0e670da3e41c164a0c256aeedd81886f878911581d852f/cryptography-45.0.4-pp311-pypy311_pp73-manylinux_2_34_aarch64.whl", hash = "sha256:0339a692de47084969500ee455e42c58e449461e0ec845a34a6a9b9bf7df7fb8", size = 4146422, upload-time = "2025-06-10T00:03:41.827Z" },
    { url = "https://files.pythonhosted.org/packages/09/ad/5429fcc4def93e577a5407988f89cf15305e64920203d4ac14601a9dc876/cryptography-45.0.4-pp311-pypy311_pp73-manylinux_2_34_x86_64.whl", hash = "sha256:0cf13c77d710131d33e63626bd55ae7c0efb701ebdc2b3a7952b9b23a0412862", size = 4388475, upload-time = "2025-06-10T00:03:43.493Z" },
    { url = "https://files.pythonhosted.org/packages/99/49/0ab9774f64555a1b50102757811508f5ace451cf5dc0a2d074a4b9deca6a/cryptography-45.0.4-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:bbc505d1dc469ac12a0a064214879eac6294038d6b24ae9f71faae1448a9608d", size = 3337594, upload-time = "2025-06-10T00:03:45.523Z" },
]

[[package]]
name = "decorator"
version = "5.2.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/43/fa/6d96a0978d19e17b68d634497769987b16c8f4cd0a7a05048bec693caa6b/decorator-5.2.1.tar.gz", hash = "sha256:65f266143752f734b0a7cc83c46f4618af75b8c5911b00ccb61d0ac9b6da0360", size = 56711, upload-time = "2025-02-24T04:41:34.073Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4e/8c/f3147f5c4b73e7550fe5f9352eaa956ae838d5c51eb58e7a25b9f3e2643b/decorator-5.2.1-py3-none-any.whl", hash = "sha256:d316bb415a2d9e2d2b3abcc4084c6502fc09240e292cd76a76afc106a1c8e04a", size = 9190, upload-time = "2025-02-24T04:41:32.565Z" },
]

[[package]]
name = "dirty-equals"
version = "0.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b0/99/133892f401ced5a27e641a473c547d5fbdb39af8f85dac8a9d633ea3e7a7/dirty_equals-0.9.0.tar.gz", hash = "sha256:17f515970b04ed7900b733c95fd8091f4f85e52f1fb5f268757f25c858eb1f7b", size = 50412, upload-time = "2025-01-11T23:23:40.491Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/77/0c/03cc99bf3b6328604b10829de3460f2b2ad3373200c45665c38508e550c6/dirty_equals-0.9.0-py3-none-any.whl", hash = "sha256:ff4d027f5cfa1b69573af00f7ba9043ea652dbdce3fe5cbe828e478c7346db9c", size = 28226, upload-time = "2025-01-11T23:23:37.489Z" },
]

[[package]]
name = "distlib"
version = "0.3.9"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0d/dd/1bec4c5ddb504ca60fc29472f3d27e8d4da1257a854e1d96742f15c1d02d/distlib-0.3.9.tar.gz", hash = "sha256:a60f20dea646b8a33f3e7772f74dc0b2d0772d2837ee1342a00645c81edf9403", size = 613923, upload-time = "2024-10-09T18:35:47.551Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/91/a1/cf2472db20f7ce4a6be1253a81cfdf85ad9c7885ffbed7047fb72c24cf87/distlib-0.3.9-py2.py3-none-any.whl", hash = "sha256:47f8c22fd27c27e25a65601af709b38e4f0a45ea4fc2e710f65755fa8caaaf87", size = 468973, upload-time = "2024-10-09T18:35:44.272Z" },
]

[[package]]
name = "dnspython"
version = "2.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b5/4a/263763cb2ba3816dd94b08ad3a33d5fdae34ecb856678773cc40a3605829/dnspython-2.7.0.tar.gz", hash = "sha256:ce9c432eda0dc91cf618a5cedf1a4e142651196bbcd2c80e89ed5a907e5cfaf1", size = 345197, upload-time = "2024-10-05T20:14:59.362Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/68/1b/e0a87d256e40e8c888847551b20a017a6b98139178505dc7ffb96f04e954/dnspython-2.7.0-py3-none-any.whl", hash = "sha256:b4c34b7d10b51bcc3a5071e7b8dee77939f1e878477eeecc965e9835f63c6c86", size = 313632, upload-time = "2024-10-05T20:14:57.687Z" },
]

[[package]]
name = "email-validator"
version = "2.2.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "dnspython" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/48/ce/13508a1ec3f8bb981ae4ca79ea40384becc868bfae97fd1c942bb3a001b1/email_validator-2.2.0.tar.gz", hash = "sha256:cb690f344c617a714f22e66ae771445a1ceb46821152df8e165c5f9a364582b7", size = 48967, upload-time = "2024-06-20T11:30:30.034Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d7/ee/bf0adb559ad3c786f12bcbc9296b3f5675f529199bef03e2df281fa1fadb/email_validator-2.2.0-py3-none-any.whl", hash = "sha256:561977c2d73ce3611850a06fa56b414621e0c8faa9d66f2611407d87465da631", size = 33521, upload-time = "2024-06-20T11:30:28.248Z" },
]

[[package]]
name = "exceptiongroup"
version = "1.3.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/0b/9f/a65090624ecf468cdca03533906e7c69ed7588582240cfe7cc9e770b50eb/exceptiongroup-1.3.0.tar.gz", hash = "sha256:b241f5885f560bc56a59ee63ca4c6a8bfa46ae4ad651af316d4e81817bb9fd88", size = 29749, upload-time = "2025-05-10T17:42:51.123Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/36/f4/c6e662dade71f56cd2f3735141b265c3c79293c109549c1e6933b0651ffc/exceptiongroup-1.3.0-py3-none-any.whl", hash = "sha256:4d111e6e0c13d0644cad6ddaa7ed0261a0b36971f6d23e7ec9b4b9097da78a10", size = 16674, upload-time = "2025-05-10T17:42:49.33Z" },
]

[[package]]
name = "execnet"
version = "2.1.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/bb/ff/b4c0dc78fbe20c3e59c0c7334de0c27eb4001a2b2017999af398bf730817/execnet-2.1.1.tar.gz", hash = "sha256:5189b52c6121c24feae288166ab41b32549c7e2348652736540b9e6e7d4e72e3", size = 166524, upload-time = "2024-04-08T09:04:19.245Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/43/09/2aea36ff60d16dd8879bdb2f5b3ee0ba8d08cbbdcdfe870e695ce3784385/execnet-2.1.1-py3-none-any.whl", hash = "sha256:26dee51f1b80cebd6d0ca8e74dd8745419761d3bef34163928cbebbdc4749fdc", size = 40612, upload-time = "2024-04-08T09:04:17.414Z" },
]

[[package]]
name = "executing"
version = "2.2.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/91/50/a9d80c47ff289c611ff12e63f7c5d13942c65d68125160cefd768c73e6e4/executing-2.2.0.tar.gz", hash = "sha256:5d108c028108fe2551d1a7b2e8b713341e2cb4fc0aa7dcf966fa4327a5226755", size = 978693, upload-time = "2025-01-22T15:41:29.403Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7b/8f/c4d9bafc34ad7ad5d8dc16dd1347ee0e507a52c3adb6bfa8887e1c6a26ba/executing-2.2.0-py2.py3-none-any.whl", hash = "sha256:11387150cad388d62750327a53d3339fad4888b39a6fe233c3afbb54ecffd3aa", size = 26702, upload-time = "2025-01-22T15:41:25.929Z" },
]

[[package]]
name = "fancycompleter"
version = "0.11.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pyreadline3", marker = "python_full_version < '3.13' and sys_platform == 'win32'" },
    { name = "pyrepl", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/4e/4c/d11187dee93eff89d082afda79b63c79320ae1347e49485a38f05ad359d0/fancycompleter-0.11.1.tar.gz", hash = "sha256:5b4ad65d76b32b1259251516d0f1cb2d82832b1ff8506697a707284780757f69", size = 341776, upload-time = "2025-05-26T12:59:11.045Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/30/c3/6f0e3896f193528bbd2b4d2122d4be8108a37efab0b8475855556a8c4afa/fancycompleter-0.11.1-py3-none-any.whl", hash = "sha256:44243d7fab37087208ca5acacf8f74c0aa4d733d04d593857873af7513cdf8a6", size = 11207, upload-time = "2025-05-26T12:59:09.857Z" },
]

[[package]]
name = "fastapi"
version = "0.115.13"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pydantic" },
    { name = "starlette" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/20/64/ec0788201b5554e2a87c49af26b77a4d132f807a0fa9675257ac92c6aa0e/fastapi-0.115.13.tar.gz", hash = "sha256:55d1d25c2e1e0a0a50aceb1c8705cd932def273c102bff0b1c1da88b3c6eb307", size = 295680, upload-time = "2025-06-17T11:49:45.575Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/59/4a/e17764385382062b0edbb35a26b7cf76d71e27e456546277a42ba6545c6e/fastapi-0.115.13-py3-none-any.whl", hash = "sha256:0a0cab59afa7bab22f5eb347f8c9864b681558c278395e94035a741fc10cd865", size = 95315, upload-time = "2025-06-17T11:49:44.106Z" },
]

[[package]]
name = "fastmcp"
source = { editable = "." }
dependencies = [
    { name = "authlib" },
    { name = "exceptiongroup" },
    { name = "httpx" },
    { name = "mcp" },
    { name = "openapi-pydantic" },
    { name = "pydantic", extra = ["email"] },
    { name = "python-dotenv" },
    { name = "rich" },
    { name = "typer" },
]

[package.optional-dependencies]
websockets = [
    { name = "websockets" },
]

[package.dev-dependencies]
dev = [
    { name = "copychat" },
    { name = "dirty-equals" },
    { name = "fastapi" },
    { name = "ipython", version = "8.37.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.11'" },
    { name = "ipython", version = "9.3.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.11'" },
    { name = "pdbpp" },
    { name = "pre-commit" },
    { name = "pyinstrument" },
    { name = "pyright" },
    { name = "pytest" },
    { name = "pytest-asyncio" },
    { name = "pytest-cov" },
    { name = "pytest-env" },
    { name = "pytest-flakefinder" },
    { name = "pytest-httpx" },
    { name = "pytest-report" },
    { name = "pytest-timeout" },
    { name = "pytest-xdist" },
    { name = "ruff" },
]

[package.metadata]
requires-dist = [
    { name = "authlib", specifier = ">=1.5.2" },
    { name = "exceptiongroup", specifier = ">=1.2.2" },
    { name = "httpx", specifier = ">=0.28.1" },
    { name = "mcp", specifier = ">=1.10.0" },
    { name = "openapi-pydantic", specifier = ">=0.5.1" },
    { name = "pydantic", extras = ["email"], specifier = ">=2.11.7" },
    { name = "python-dotenv", specifier = ">=1.1.0" },
    { name = "rich", specifier = ">=13.9.4" },
    { name = "typer", specifier = ">=0.15.2" },
    { name = "websockets", marker = "extra == 'websockets'", specifier = ">=15.0.1" },
]
provides-extras = ["websockets"]

[package.metadata.requires-dev]
dev = [
    { name = "copychat", specifier = ">=0.5.2" },
    { name = "dirty-equals", specifier = ">=0.9.0" },
    { name = "fastapi", specifier = ">=0.115.12" },
    { name = "ipython", specifier = ">=8.12.3" },
    { name = "pdbpp", specifier = ">=0.10.3" },
    { name = "pre-commit" },
    { name = "pyinstrument", specifier = ">=5.0.2" },
    { name = "pyright", specifier = ">=1.1.389" },
    { name = "pytest", specifier = ">=8.3.3" },
    { name = "pytest-asyncio", specifier = ">=0.23.5" },
    { name = "pytest-cov", specifier = ">=6.1.1" },
    { name = "pytest-env", specifier = ">=1.1.5" },
    { name = "pytest-flakefinder" },
    { name = "pytest-httpx", specifier = ">=0.35.0" },
    { name = "pytest-report", specifier = ">=0.2.1" },
    { name = "pytest-timeout", specifier = ">=2.4.0" },
    { name = "pytest-xdist", specifier = ">=3.6.1" },
    { name = "ruff" },
]

[[package]]
name = "filelock"
version = "3.18.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0a/10/c23352565a6544bdc5353e0b15fc1c563352101f30e24bf500207a54df9a/filelock-3.18.0.tar.gz", hash = "sha256:adbc88eabb99d2fec8c9c1b229b171f18afa655400173ddc653d5d01501fb9f2", size = 18075, upload-time = "2025-03-14T07:11:40.47Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4d/36/2a115987e2d8c300a974597416d9de88f2444426de9571f4b59b2cca3acc/filelock-3.18.0-py3-none-any.whl", hash = "sha256:c401f4f8377c4464e6db25fff06205fd89bdd83b65eb0488ed1b160f780e21de", size = 16215, upload-time = "2025-03-14T07:11:39.145Z" },
]

[[package]]
name = "gitdb"
version = "4.0.12"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "smmap" },
]
sdist = { url = "https://files.pythonhosted.org/packages/72/94/63b0fc47eb32792c7ba1fe1b694daec9a63620db1e313033d18140c2320a/gitdb-4.0.12.tar.gz", hash = "sha256:5ef71f855d191a3326fcfbc0d5da835f26b13fbcba60c32c21091c349ffdb571", size = 394684, upload-time = "2025-01-02T07:20:46.413Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a0/61/5c78b91c3143ed5c14207f463aecfc8f9dbb5092fb2869baf37c273b2705/gitdb-4.0.12-py3-none-any.whl", hash = "sha256:67073e15955400952c6565cc3e707c554a4eea2e428946f7a4c162fab9bd9bcf", size = 62794, upload-time = "2025-01-02T07:20:43.624Z" },
]

[[package]]
name = "gitpython"
version = "3.1.44"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "gitdb" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c0/89/37df0b71473153574a5cdef8f242de422a0f5d26d7a9e231e6f169b4ad14/gitpython-3.1.44.tar.gz", hash = "sha256:c87e30b26253bf5418b01b0660f818967f3c503193838337fe5e573331249269", size = 214196, upload-time = "2025-01-02T07:32:43.59Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1d/9a/4114a9057db2f1462d5c8f8390ab7383925fe1ac012eaa42402ad65c2963/GitPython-3.1.44-py3-none-any.whl", hash = "sha256:9e0e10cda9bed1ee64bc9a6de50e7e38a9c9943241cd7f585f6df3ed28011110", size = 207599, upload-time = "2025-01-02T07:32:40.731Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[[package]]
name = "httpx-sse"
version = "0.4.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6e/fa/66bd985dd0b7c109a3bcb89272ee0bfb7e2b4d06309ad7b38ff866734b2a/httpx_sse-0.4.1.tar.gz", hash = "sha256:8f44d34414bc7b21bf3602713005c5df4917884f76072479b21f68befa4ea26e", size = 12998, upload-time = "2025-06-24T13:21:05.71Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/25/0a/6269e3473b09aed2dab8aa1a600c70f31f00ae1349bee30658f7e358a159/httpx_sse-0.4.1-py3-none-any.whl", hash = "sha256:cba42174344c3a5b06f255ce65b350880f962d99ead85e776f23c6618a377a37", size = 8054, upload-time = "2025-06-24T13:21:04.772Z" },
]

[[package]]
name = "identify"
version = "2.6.12"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/88/d193a27416618628a5eea64e3223acd800b40749a96ffb322a9b55a49ed1/identify-2.6.12.tar.gz", hash = "sha256:d8de45749f1efb108badef65ee8386f0f7bb19a7f26185f74de6367bffbaf0e6", size = 99254, upload-time = "2025-05-23T20:37:53.3Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7a/cd/18f8da995b658420625f7ef13f037be53ae04ec5ad33f9b718240dcfd48c/identify-2.6.12-py2.py3-none-any.whl", hash = "sha256:ad9672d5a72e0d2ff7c5c8809b62dfa60458626352fb0eb7b55e69bdc45334a2", size = 99145, upload-time = "2025-05-23T20:37:51.495Z" },
]

[[package]]
name = "idna"
version = "3.10"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f1/70/7703c29685631f5a7590aa73f1f1d3fa9a380e654b86af429e0934a32f7d/idna-3.10.tar.gz", hash = "sha256:12f65c9b470abda6dc35cf8e63cc574b1c52b11df2c86030af0ac09b01b13ea9", size = 190490, upload-time = "2024-09-15T18:07:39.745Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/76/c6/c88e154df9c4e1a2a66ccf0005a88dfb2650c1dffb6f5ce603dfbd452ce3/idna-3.10-py3-none-any.whl", hash = "sha256:946d195a0d259cbba61165e88e65941f16e9b36ea6ddb97f00452bae8b1287d3", size = 70442, upload-time = "2024-09-15T18:07:37.964Z" },
]

[[package]]
name = "iniconfig"
version = "2.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f2/97/ebf4da567aa6827c909642694d71c9fcf53e5b504f2d96afea02718862f3/iniconfig-2.1.0.tar.gz", hash = "sha256:3abbd2e30b36733fee78f9c7f7308f2d0050e88f0087fd25c2645f63c773e1c7", size = 4793, upload-time = "2025-03-19T20:09:59.721Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2c/e1/e6716421ea10d38022b952c159d5161ca1193197fb744506875fbb87ea7b/iniconfig-2.1.0-py3-none-any.whl", hash = "sha256:9deba5723312380e77435581c6bf4935c94cbfab9b1ed33ef8d238ea168eb760", size = 6050, upload-time = "2025-03-19T20:10:01.071Z" },
]

[[package]]
name = "ipython"
version = "8.37.0"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version < '3.11'",
]
dependencies = [
    { name = "colorama", marker = "python_full_version < '3.11' and sys_platform == 'win32'" },
    { name = "decorator", marker = "python_full_version < '3.11'" },
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "jedi", marker = "python_full_version < '3.11'" },
    { name = "matplotlib-inline", marker = "python_full_version < '3.11'" },
    { name = "pexpect", marker = "python_full_version < '3.11' and sys_platform != 'emscripten' and sys_platform != 'win32'" },
    { name = "prompt-toolkit", marker = "python_full_version < '3.11'" },
    { name = "pygments", marker = "python_full_version < '3.11'" },
    { name = "stack-data", marker = "python_full_version < '3.11'" },
    { name = "traitlets", marker = "python_full_version < '3.11'" },
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/85/31/10ac88f3357fc276dc8a64e8880c82e80e7459326ae1d0a211b40abf6665/ipython-8.37.0.tar.gz", hash = "sha256:ca815841e1a41a1e6b73a0b08f3038af9b2252564d01fc405356d34033012216", size = 5606088, upload-time = "2025-05-31T16:39:09.613Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/91/d0/274fbf7b0b12643cbbc001ce13e6a5b1607ac4929d1b11c72460152c9fc3/ipython-8.37.0-py3-none-any.whl", hash = "sha256:ed87326596b878932dbcb171e3e698845434d8c61b8d8cd474bf663041a9dcf2", size = 831864, upload-time = "2025-05-31T16:39:06.38Z" },
]

[[package]]
name = "ipython"
version = "9.3.0"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version >= '3.11'",
]
dependencies = [
    { name = "colorama", marker = "python_full_version >= '3.11' and sys_platform == 'win32'" },
    { name = "decorator", marker = "python_full_version >= '3.11'" },
    { name = "ipython-pygments-lexers", marker = "python_full_version >= '3.11'" },
    { name = "jedi", marker = "python_full_version >= '3.11'" },
    { name = "matplotlib-inline", marker = "python_full_version >= '3.11'" },
    { name = "pexpect", marker = "python_full_version >= '3.11' and sys_platform != 'emscripten' and sys_platform != 'win32'" },
    { name = "prompt-toolkit", marker = "python_full_version >= '3.11'" },
    { name = "pygments", marker = "python_full_version >= '3.11'" },
    { name = "stack-data", marker = "python_full_version >= '3.11'" },
    { name = "traitlets", marker = "python_full_version >= '3.11'" },
    { name = "typing-extensions", marker = "python_full_version == '3.11.*'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/dc/09/4c7e06b96fbd203e06567b60fb41b06db606b6a82db6db7b2c85bb72a15c/ipython-9.3.0.tar.gz", hash = "sha256:79eb896f9f23f50ad16c3bc205f686f6e030ad246cc309c6279a242b14afe9d8", size = 4426460, upload-time = "2025-05-31T16:34:55.678Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3c/99/9ed3d52d00f1846679e3aa12e2326ac7044b5e7f90dc822b60115fa533ca/ipython-9.3.0-py3-none-any.whl", hash = "sha256:1a0b6dd9221a1f5dddf725b57ac0cb6fddc7b5f470576231ae9162b9b3455a04", size = 605320, upload-time = "2025-05-31T16:34:52.154Z" },
]

[[package]]
name = "ipython-pygments-lexers"
version = "1.1.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pygments", marker = "python_full_version >= '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ef/4c/5dd1d8af08107f88c7f741ead7a40854b8ac24ddf9ae850afbcf698aa552/ipython_pygments_lexers-1.1.1.tar.gz", hash = "sha256:09c0138009e56b6854f9535736f4171d855c8c08a563a0dcd8022f78355c7e81", size = 8393, upload-time = "2025-01-17T11:24:34.505Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d9/33/1f075bf72b0b747cb3288d011319aaf64083cf2efef8354174e3ed4540e2/ipython_pygments_lexers-1.1.1-py3-none-any.whl", hash = "sha256:a9462224a505ade19a605f71f8fa63c2048833ce50abc86768a0d81d876dc81c", size = 8074, upload-time = "2025-01-17T11:24:33.271Z" },
]

[[package]]
name = "jedi"
version = "0.19.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "parso" },
]
sdist = { url = "https://files.pythonhosted.org/packages/72/3a/79a912fbd4d8dd6fbb02bf69afd3bb72cf0c729bb3063c6f4498603db17a/jedi-0.19.2.tar.gz", hash = "sha256:4770dc3de41bde3966b02eb84fbcf557fb33cce26ad23da12c742fb50ecb11f0", size = 1231287, upload-time = "2024-11-11T01:41:42.873Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c0/5a/9cac0c82afec3d09ccd97c8b6502d48f165f9124db81b4bcb90b4af974ee/jedi-0.19.2-py2.py3-none-any.whl", hash = "sha256:a8ef22bde8490f57fe5c7681a3c83cb58874daf72b4784de3cce5b6ef6edb5b9", size = 1572278, upload-time = "2024-11-11T01:41:40.175Z" },
]

[[package]]
name = "jsonschema"
version = "4.24.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "attrs" },
    { name = "jsonschema-specifications" },
    { name = "referencing" },
    { name = "rpds-py" },
]
sdist = { url = "https://files.pythonhosted.org/packages/bf/d3/1cf5326b923a53515d8f3a2cd442e6d7e94fcc444716e879ea70a0ce3177/jsonschema-4.24.0.tar.gz", hash = "sha256:0b4e8069eb12aedfa881333004bccaec24ecef5a8a6a4b6df142b2cc9599d196", size = 353480, upload-time = "2025-05-26T18:48:10.459Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a2/3d/023389198f69c722d039351050738d6755376c8fd343e91dc493ea485905/jsonschema-4.24.0-py3-none-any.whl", hash = "sha256:a462455f19f5faf404a7902952b6f0e3ce868f3ee09a359b05eca6673bd8412d", size = 88709, upload-time = "2025-05-26T18:48:08.417Z" },
]

[[package]]
name = "jsonschema-specifications"
version = "2025.4.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "referencing" },
]
sdist = { url = "https://files.pythonhosted.org/packages/bf/ce/46fbd9c8119cfc3581ee5643ea49464d168028cfb5caff5fc0596d0cf914/jsonschema_specifications-2025.4.1.tar.gz", hash = "sha256:630159c9f4dbea161a6a2205c3011cc4f18ff381b189fff48bb39b9bf26ae608", size = 15513, upload-time = "2025-04-23T12:34:07.418Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/01/0e/b27cdbaccf30b890c40ed1da9fd4a3593a5cf94dae54fb34f8a4b74fcd3f/jsonschema_specifications-2025.4.1-py3-none-any.whl", hash = "sha256:4653bffbd6584f7de83a67e0d620ef16900b390ddc7939d56684d6c81e33f1af", size = 18437, upload-time = "2025-04-23T12:34:05.422Z" },
]

[[package]]
name = "markdown-it-py"
version = "3.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/38/71/3b932df36c1a044d397a1f92d1cf91ee0a503d91e470cbd670aa66b07ed0/markdown-it-py-3.0.0.tar.gz", hash = "sha256:e3f60a94fa066dc52ec76661e37c851cb232d92f9886b15cb560aaada2df8feb", size = 74596, upload-time = "2023-06-03T06:41:14.443Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/42/d7/1ec15b46af6af88f19b8e5ffea08fa375d433c998b8a7639e76935c14f1f/markdown_it_py-3.0.0-py3-none-any.whl", hash = "sha256:355216845c60bd96232cd8d8c40e8f9765cc86f46880e43a8fd22dc1a1a8cab1", size = 87528, upload-time = "2023-06-03T06:41:11.019Z" },
]

[[package]]
name = "matplotlib-inline"
version = "0.1.7"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "traitlets" },
]
sdist = { url = "https://files.pythonhosted.org/packages/99/5b/a36a337438a14116b16480db471ad061c36c3694df7c2084a0da7ba538b7/matplotlib_inline-0.1.7.tar.gz", hash = "sha256:8423b23ec666be3d16e16b60bdd8ac4e86e840ebd1dd11a30b9f117f2fa0ab90", size = 8159, upload-time = "2024-04-15T13:44:44.803Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8f/8e/9ad090d3553c280a8060fbf6e24dc1c0c29704ee7d1c372f0c174aa59285/matplotlib_inline-0.1.7-py3-none-any.whl", hash = "sha256:df192d39a4ff8f21b1895d72e6a13f5fcc5099f00fa84384e0ea28c2cc0653ca", size = 9899, upload-time = "2024-04-15T13:44:43.265Z" },
]

[[package]]
name = "mcp"
version = "1.10.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "httpx" },
    { name = "httpx-sse" },
    { name = "jsonschema" },
    { name = "pydantic" },
    { name = "pydantic-settings" },
    { name = "python-multipart" },
    { name = "sse-starlette" },
    { name = "starlette" },
    { name = "uvicorn", marker = "sys_platform != 'emscripten'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c8/1a/d90e42be23a7e6dd35c03e35c7c63fe1036f082d3bb88114b66bd0f2467e/mcp-1.10.0.tar.gz", hash = "sha256:91fb1623c3faf14577623d14755d3213db837c5da5dae85069e1b59124cbe0e9", size = 392961, upload-time = "2025-06-26T13:51:19.025Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0f/52/e1c43c4b5153465fd5d3b4b41bf2d4c7731475e9f668f38d68f848c25c9a/mcp-1.10.0-py3-none-any.whl", hash = "sha256:925c45482d75b1b6f11febddf9736d55edf7739c7ea39b583309f6651cbc9e5c", size = 150894, upload-time = "2025-06-26T13:51:17.342Z" },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729, upload-time = "2022-08-14T12:40:10.846Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979, upload-time = "2022-08-14T12:40:09.779Z" },
]

[[package]]
name = "nodeenv"
version = "1.9.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/43/16/fc88b08840de0e0a72a2f9d8c6bae36be573e475a6326ae854bcc549fc45/nodeenv-1.9.1.tar.gz", hash = "sha256:6ec12890a2dab7946721edbfbcd91f3319c6ccc9aec47be7c7e6b7011ee6645f", size = 47437, upload-time = "2024-06-04T18:44:11.171Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d2/1d/1b658dbd2b9fa9c4c9f32accbfc0205d532c8c6194dc0f2a4c0428e7128a/nodeenv-1.9.1-py2.py3-none-any.whl", hash = "sha256:ba11c9782d29c27c70ffbdda2d7415098754709be8a7056d79a737cd901155c9", size = 22314, upload-time = "2024-06-04T18:44:08.352Z" },
]

[[package]]
name = "openapi-pydantic"
version = "0.5.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pydantic" },
]
sdist = { url = "https://files.pythonhosted.org/packages/02/2e/58d83848dd1a79cb92ed8e63f6ba901ca282c5f09d04af9423ec26c56fd7/openapi_pydantic-0.5.1.tar.gz", hash = "sha256:ff6835af6bde7a459fb93eb93bb92b8749b754fc6e51b2f1590a19dc3005ee0d", size = 60892, upload-time = "2025-01-08T19:29:27.083Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/cf/03675d8bd8ecbf4445504d8071adab19f5f993676795708e36402ab38263/openapi_pydantic-0.5.1-py3-none-any.whl", hash = "sha256:a3a09ef4586f5bd760a8df7f43028b60cafb6d9f61de2acba9574766255ab146", size = 96381, upload-time = "2025-01-08T19:29:25.275Z" },
]

[[package]]
name = "packaging"
version = "25.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a1/d4/1fc4078c65507b51b96ca8f8c3ba19e6a61c8253c72794544580a7b6c24d/packaging-25.0.tar.gz", hash = "sha256:d443872c98d677bf60f6a1f2f8c1cb748e8fe762d2bf9d3148b5599295b0fc4f", size = 165727, upload-time = "2025-04-19T11:48:59.673Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/20/12/38679034af332785aac8774540895e234f4d07f7545804097de4b666afd8/packaging-25.0-py3-none-any.whl", hash = "sha256:29572ef2b1f17581046b3a2227d5c611fb25ec70ca1ba8554b24b0e69331a484", size = 66469, upload-time = "2025-04-19T11:48:57.875Z" },
]

[[package]]
name = "parso"
version = "0.8.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/66/94/68e2e17afaa9169cf6412ab0f28623903be73d1b32e208d9e8e541bb086d/parso-0.8.4.tar.gz", hash = "sha256:eb3a7b58240fb99099a345571deecc0f9540ea5f4dd2fe14c2a99d6b281ab92d", size = 400609, upload-time = "2024-04-05T09:43:55.897Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/ac/dac4a63f978e4dcb3c6d3a78c4d8e0192a113d288502a1216950c41b1027/parso-0.8.4-py2.py3-none-any.whl", hash = "sha256:a418670a20291dacd2dddc80c377c5c3791378ee1e8d12bffc35420643d43f18", size = 103650, upload-time = "2024-04-05T09:43:53.299Z" },
]

[[package]]
name = "pathspec"
version = "0.12.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ca/bc/f35b8446f4531a7cb215605d100cd88b7ac6f44ab3fc94870c120ab3adbf/pathspec-0.12.1.tar.gz", hash = "sha256:a482d51503a1ab33b1c67a6c3813a26953dbdc71c31dacaef9a838c4e29f5712", size = 51043, upload-time = "2023-12-10T22:30:45Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cc/20/ff623b09d963f88bfde16306a54e12ee5ea43e9b597108672ff3a408aad6/pathspec-0.12.1-py3-none-any.whl", hash = "sha256:a0d503e138a4c123b27490a4f7beda6a01c6f288df0e4a8b79c7eb0dc7b4cc08", size = 31191, upload-time = "2023-12-10T22:30:43.14Z" },
]

[[package]]
name = "pdbpp"
version = "0.11.6"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "fancycompleter" },
    { name = "pygments" },
]
sdist = { url = "https://files.pythonhosted.org/packages/27/ef/e6ae1a1e1d2cbe0fbf04f22b21d7d58e8e13d24dfcc3b6a4dea18a3ed1e0/pdbpp-0.11.6.tar.gz", hash = "sha256:36a73c5bcf0c3c35034be4cf99e6106e3ee0c8f5e0faafc2cf9be5f1481eb4b7", size = 78178, upload-time = "2025-04-16T10:20:07.008Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c5/e1/77fa5c45fcd95a80b0d793b604c19b71c9fa8d5b27d403eced79f3842828/pdbpp-0.11.6-py3-none-any.whl", hash = "sha256:8e024d36bd2f35a3b19d8732524c696b8b4aef633250d28547198e746cd81ccb", size = 33334, upload-time = "2025-04-16T10:20:05.529Z" },
]

[[package]]
name = "pexpect"
version = "4.9.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "ptyprocess" },
]
sdist = { url = "https://files.pythonhosted.org/packages/42/92/cc564bf6381ff43ce1f4d06852fc19a2f11d180f23dc32d9588bee2f149d/pexpect-4.9.0.tar.gz", hash = "sha256:ee7d41123f3c9911050ea2c2dac107568dc43b2d3b0c7557a33212c398ead30f", size = 166450, upload-time = "2023-11-25T09:07:26.339Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9e/c3/059298687310d527a58bb01f3b1965787ee3b40dce76752eda8b44e9a2c5/pexpect-4.9.0-py2.py3-none-any.whl", hash = "sha256:7236d1e080e4936be2dc3e326cec0af72acf9212a7e1d060210e70a47e253523", size = 63772, upload-time = "2023-11-25T06:56:14.81Z" },
]

[[package]]
name = "platformdirs"
version = "4.3.8"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fe/8b/3c73abc9c759ecd3f1f7ceff6685840859e8070c4d947c93fae71f6a0bf2/platformdirs-4.3.8.tar.gz", hash = "sha256:3d512d96e16bcb959a814c9f348431070822a6496326a4be0911c40b5a74c2bc", size = 21362, upload-time = "2025-05-07T22:47:42.121Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fe/39/979e8e21520d4e47a0bbe349e2713c0aac6f3d853d0e5b34d76206c439aa/platformdirs-4.3.8-py3-none-any.whl", hash = "sha256:ff7059bb7eb1179e2685604f4aaf157cfd9535242bd23742eadc3c13542139b4", size = 18567, upload-time = "2025-05-07T22:47:40.376Z" },
]

[[package]]
name = "pluggy"
version = "1.6.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3", size = 69412, upload-time = "2025-05-15T12:30:07.975Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/54/20/4d324d65cc6d9205fabedc306948156824eb9f0ee1633355a8f7ec5c66bf/pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746", size = 20538, upload-time = "2025-05-15T12:30:06.134Z" },
]

[[package]]
name = "pre-commit"
version = "4.2.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "cfgv" },
    { name = "identify" },
    { name = "nodeenv" },
    { name = "pyyaml" },
    { name = "virtualenv" },
]
sdist = { url = "https://files.pythonhosted.org/packages/08/39/679ca9b26c7bb2999ff122d50faa301e49af82ca9c066ec061cfbc0c6784/pre_commit-4.2.0.tar.gz", hash = "sha256:601283b9757afd87d40c4c4a9b2b5de9637a8ea02eaff7adc2d0fb4e04841146", size = 193424, upload-time = "2025-03-18T21:35:20.987Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/88/74/a88bf1b1efeae488a0c0b7bdf71429c313722d1fc0f377537fbe554e6180/pre_commit-4.2.0-py2.py3-none-any.whl", hash = "sha256:a009ca7205f1eb497d10b845e52c838a98b6cdd2102a6c8e4540e94ee75c58bd", size = 220707, upload-time = "2025-03-18T21:35:19.343Z" },
]

[[package]]
name = "prompt-toolkit"
version = "3.0.51"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "wcwidth" },
]
sdist = { url = "https://files.pythonhosted.org/packages/bb/6e/9d084c929dfe9e3bfe0c6a47e31f78a25c54627d64a66e884a8bf5474f1c/prompt_toolkit-3.0.51.tar.gz", hash = "sha256:931a162e3b27fc90c86f1b48bb1fb2c528c2761475e57c9c06de13311c7b54ed", size = 428940, upload-time = "2025-04-15T09:18:47.731Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ce/4f/5249960887b1fbe561d9ff265496d170b55a735b76724f10ef19f9e40716/prompt_toolkit-3.0.51-py3-none-any.whl", hash = "sha256:52742911fde84e2d423e2f9a4cf1de7d7ac4e51958f648d9540e0fb8db077b07", size = 387810, upload-time = "2025-04-15T09:18:44.753Z" },
]

[[package]]
name = "ptyprocess"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/20/e5/16ff212c1e452235a90aeb09066144d0c5a6a8c0834397e03f5224495c4e/ptyprocess-0.7.0.tar.gz", hash = "sha256:5c5d0a3b48ceee0b48485e0c26037c0acd7d29765ca3fbb5cb3831d347423220", size = 70762, upload-time = "2020-12-28T15:15:30.155Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/22/a6/858897256d0deac81a172289110f31629fc4cee19b6f01283303e18c8db3/ptyprocess-0.7.0-py2.py3-none-any.whl", hash = "sha256:4b41f3967fce3af57cc7e94b888626c18bf37a083e3651ca8feeb66d492fef35", size = 13993, upload-time = "2020-12-28T15:15:28.35Z" },
]

[[package]]
name = "pure-eval"
version = "0.2.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/cd/05/0a34433a064256a578f1783a10da6df098ceaa4a57bbeaa96a6c0352786b/pure_eval-0.2.3.tar.gz", hash = "sha256:5f4e983f40564c576c7c8635ae88db5956bb2229d7e9237d03b3c0b0190eaf42", size = 19752, upload-time = "2024-07-21T12:58:21.801Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8e/37/efad0257dc6e593a18957422533ff0f87ede7c9c6ea010a2177d738fb82f/pure_eval-0.2.3-py3-none-any.whl", hash = "sha256:1db8e35b67b3d218d818ae653e27f06c3aa420901fa7b081ca98cbedc874e0d0", size = 11842, upload-time = "2024-07-21T12:58:20.04Z" },
]

[[package]]
name = "pycparser"
version = "2.22"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1d/b2/31537cf4b1ca988837256c910a668b553fceb8f069bedc4b1c826024b52c/pycparser-2.22.tar.gz", hash = "sha256:491c8be9c040f5390f5bf44a5b07752bd07f56edf992381b05c701439eec10f6", size = 172736, upload-time = "2024-03-30T13:22:22.564Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/13/a3/a812df4e2dd5696d1f351d58b8fe16a405b234ad2886a0dab9183fb78109/pycparser-2.22-py3-none-any.whl", hash = "sha256:c3702b6d3dd8c7abc1afa565d7e63d53a1d0bd86cdc24edd75470f4de499cfcc", size = 117552, upload-time = "2024-03-30T13:22:20.476Z" },
]

[[package]]
name = "pydantic"
version = "2.11.7"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/00/dd/4325abf92c39ba8623b5af936ddb36ffcfe0beae70405d456ab1fb2f5b8c/pydantic-2.11.7.tar.gz", hash = "sha256:d989c3c6cb79469287b1569f7447a17848c998458d49ebe294e975b9baf0f0db", size = 788350, upload-time = "2025-06-14T08:33:17.137Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6a/c0/ec2b1c8712ca690e5d61979dee872603e92b8a32f94cc1b72d53beab008a/pydantic-2.11.7-py3-none-any.whl", hash = "sha256:dde5df002701f6de26248661f6835bbe296a47bf73990135c7d07ce741b9623b", size = 444782, upload-time = "2025-06-14T08:33:14.905Z" },
]

[package.optional-dependencies]
email = [
    { name = "email-validator" },
]

[[package]]
name = "pydantic-core"
version = "2.33.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ad/88/5f2260bdfae97aabf98f1778d43f69574390ad787afb646292a638c923d4/pydantic_core-2.33.2.tar.gz", hash = "sha256:7cb8bc3605c29176e1b105350d2e6474142d7c1bd1d9327c4a9bdb46bf827acc", size = 435195, upload-time = "2025-04-23T18:33:52.104Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e5/92/b31726561b5dae176c2d2c2dc43a9c5bfba5d32f96f8b4c0a600dd492447/pydantic_core-2.33.2-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:2b3d326aaef0c0399d9afffeb6367d5e26ddc24d351dbc9c636840ac355dc5d8", size = 2028817, upload-time = "2025-04-23T18:30:43.919Z" },
    { url = "https://files.pythonhosted.org/packages/a3/44/3f0b95fafdaca04a483c4e685fe437c6891001bf3ce8b2fded82b9ea3aa1/pydantic_core-2.33.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:0e5b2671f05ba48b94cb90ce55d8bdcaaedb8ba00cc5359f6810fc918713983d", size = 1861357, upload-time = "2025-04-23T18:30:46.372Z" },
    { url = "https://files.pythonhosted.org/packages/30/97/e8f13b55766234caae05372826e8e4b3b96e7b248be3157f53237682e43c/pydantic_core-2.33.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0069c9acc3f3981b9ff4cdfaf088e98d83440a4c7ea1bc07460af3d4dc22e72d", size = 1898011, upload-time = "2025-04-23T18:30:47.591Z" },
    { url = "https://files.pythonhosted.org/packages/9b/a3/99c48cf7bafc991cc3ee66fd544c0aae8dc907b752f1dad2d79b1b5a471f/pydantic_core-2.33.2-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:d53b22f2032c42eaaf025f7c40c2e3b94568ae077a606f006d206a463bc69572", size = 1982730, upload-time = "2025-04-23T18:30:49.328Z" },
    { url = "https://files.pythonhosted.org/packages/de/8e/a5b882ec4307010a840fb8b58bd9bf65d1840c92eae7534c7441709bf54b/pydantic_core-2.33.2-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:0405262705a123b7ce9f0b92f123334d67b70fd1f20a9372b907ce1080c7ba02", size = 2136178, upload-time = "2025-04-23T18:30:50.907Z" },
    { url = "https://files.pythonhosted.org/packages/e4/bb/71e35fc3ed05af6834e890edb75968e2802fe98778971ab5cba20a162315/pydantic_core-2.33.2-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4b25d91e288e2c4e0662b8038a28c6a07eaac3e196cfc4ff69de4ea3db992a1b", size = 2736462, upload-time = "2025-04-23T18:30:52.083Z" },
    { url = "https://files.pythonhosted.org/packages/31/0d/c8f7593e6bc7066289bbc366f2235701dcbebcd1ff0ef8e64f6f239fb47d/pydantic_core-2.33.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6bdfe4b3789761f3bcb4b1ddf33355a71079858958e3a552f16d5af19768fef2", size = 2005652, upload-time = "2025-04-23T18:30:53.389Z" },
    { url = "https://files.pythonhosted.org/packages/d2/7a/996d8bd75f3eda405e3dd219ff5ff0a283cd8e34add39d8ef9157e722867/pydantic_core-2.33.2-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:efec8db3266b76ef9607c2c4c419bdb06bf335ae433b80816089ea7585816f6a", size = 2113306, upload-time = "2025-04-23T18:30:54.661Z" },
    { url = "https://files.pythonhosted.org/packages/ff/84/daf2a6fb2db40ffda6578a7e8c5a6e9c8affb251a05c233ae37098118788/pydantic_core-2.33.2-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:031c57d67ca86902726e0fae2214ce6770bbe2f710dc33063187a68744a5ecac", size = 2073720, upload-time = "2025-04-23T18:30:56.11Z" },
    { url = "https://files.pythonhosted.org/packages/77/fb/2258da019f4825128445ae79456a5499c032b55849dbd5bed78c95ccf163/pydantic_core-2.33.2-cp310-cp310-musllinux_1_1_armv7l.whl", hash = "sha256:f8de619080e944347f5f20de29a975c2d815d9ddd8be9b9b7268e2e3ef68605a", size = 2244915, upload-time = "2025-04-23T18:30:57.501Z" },
    { url = "https://files.pythonhosted.org/packages/d8/7a/925ff73756031289468326e355b6fa8316960d0d65f8b5d6b3a3e7866de7/pydantic_core-2.33.2-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:73662edf539e72a9440129f231ed3757faab89630d291b784ca99237fb94db2b", size = 2241884, upload-time = "2025-04-23T18:30:58.867Z" },
    { url = "https://files.pythonhosted.org/packages/0b/b0/249ee6d2646f1cdadcb813805fe76265745c4010cf20a8eba7b0e639d9b2/pydantic_core-2.33.2-cp310-cp310-win32.whl", hash = "sha256:0a39979dcbb70998b0e505fb1556a1d550a0781463ce84ebf915ba293ccb7e22", size = 1910496, upload-time = "2025-04-23T18:31:00.078Z" },
    { url = "https://files.pythonhosted.org/packages/66/ff/172ba8f12a42d4b552917aa65d1f2328990d3ccfc01d5b7c943ec084299f/pydantic_core-2.33.2-cp310-cp310-win_amd64.whl", hash = "sha256:b0379a2b24882fef529ec3b4987cb5d003b9cda32256024e6fe1586ac45fc640", size = 1955019, upload-time = "2025-04-23T18:31:01.335Z" },
    { url = "https://files.pythonhosted.org/packages/3f/8d/71db63483d518cbbf290261a1fc2839d17ff89fce7089e08cad07ccfce67/pydantic_core-2.33.2-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:4c5b0a576fb381edd6d27f0a85915c6daf2f8138dc5c267a57c08a62900758c7", size = 2028584, upload-time = "2025-04-23T18:31:03.106Z" },
    { url = "https://files.pythonhosted.org/packages/24/2f/3cfa7244ae292dd850989f328722d2aef313f74ffc471184dc509e1e4e5a/pydantic_core-2.33.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:e799c050df38a639db758c617ec771fd8fb7a5f8eaaa4b27b101f266b216a246", size = 1855071, upload-time = "2025-04-23T18:31:04.621Z" },
    { url = "https://files.pythonhosted.org/packages/b3/d3/4ae42d33f5e3f50dd467761304be2fa0a9417fbf09735bc2cce003480f2a/pydantic_core-2.33.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:dc46a01bf8d62f227d5ecee74178ffc448ff4e5197c756331f71efcc66dc980f", size = 1897823, upload-time = "2025-04-23T18:31:06.377Z" },
    { url = "https://files.pythonhosted.org/packages/f4/f3/aa5976e8352b7695ff808599794b1fba2a9ae2ee954a3426855935799488/pydantic_core-2.33.2-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:a144d4f717285c6d9234a66778059f33a89096dfb9b39117663fd8413d582dcc", size = 1983792, upload-time = "2025-04-23T18:31:07.93Z" },
    { url = "https://files.pythonhosted.org/packages/d5/7a/cda9b5a23c552037717f2b2a5257e9b2bfe45e687386df9591eff7b46d28/pydantic_core-2.33.2-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:73cf6373c21bc80b2e0dc88444f41ae60b2f070ed02095754eb5a01df12256de", size = 2136338, upload-time = "2025-04-23T18:31:09.283Z" },
    { url = "https://files.pythonhosted.org/packages/2b/9f/b8f9ec8dd1417eb9da784e91e1667d58a2a4a7b7b34cf4af765ef663a7e5/pydantic_core-2.33.2-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3dc625f4aa79713512d1976fe9f0bc99f706a9dee21dfd1810b4bbbf228d0e8a", size = 2730998, upload-time = "2025-04-23T18:31:11.7Z" },
    { url = "https://files.pythonhosted.org/packages/47/bc/cd720e078576bdb8255d5032c5d63ee5c0bf4b7173dd955185a1d658c456/pydantic_core-2.33.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:881b21b5549499972441da4758d662aeea93f1923f953e9cbaff14b8b9565aef", size = 2003200, upload-time = "2025-04-23T18:31:13.536Z" },
    { url = "https://files.pythonhosted.org/packages/ca/22/3602b895ee2cd29d11a2b349372446ae9727c32e78a94b3d588a40fdf187/pydantic_core-2.33.2-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:bdc25f3681f7b78572699569514036afe3c243bc3059d3942624e936ec93450e", size = 2113890, upload-time = "2025-04-23T18:31:15.011Z" },
    { url = "https://files.pythonhosted.org/packages/ff/e6/e3c5908c03cf00d629eb38393a98fccc38ee0ce8ecce32f69fc7d7b558a7/pydantic_core-2.33.2-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:fe5b32187cbc0c862ee201ad66c30cf218e5ed468ec8dc1cf49dec66e160cc4d", size = 2073359, upload-time = "2025-04-23T18:31:16.393Z" },
    { url = "https://files.pythonhosted.org/packages/12/e7/6a36a07c59ebefc8777d1ffdaf5ae71b06b21952582e4b07eba88a421c79/pydantic_core-2.33.2-cp311-cp311-musllinux_1_1_armv7l.whl", hash = "sha256:bc7aee6f634a6f4a95676fcb5d6559a2c2a390330098dba5e5a5f28a2e4ada30", size = 2245883, upload-time = "2025-04-23T18:31:17.892Z" },
    { url = "https://files.pythonhosted.org/packages/16/3f/59b3187aaa6cc0c1e6616e8045b284de2b6a87b027cce2ffcea073adf1d2/pydantic_core-2.33.2-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:235f45e5dbcccf6bd99f9f472858849f73d11120d76ea8707115415f8e5ebebf", size = 2241074, upload-time = "2025-04-23T18:31:19.205Z" },
    { url = "https://files.pythonhosted.org/packages/e0/ed/55532bb88f674d5d8f67ab121a2a13c385df382de2a1677f30ad385f7438/pydantic_core-2.33.2-cp311-cp311-win32.whl", hash = "sha256:6368900c2d3ef09b69cb0b913f9f8263b03786e5b2a387706c5afb66800efd51", size = 1910538, upload-time = "2025-04-23T18:31:20.541Z" },
    { url = "https://files.pythonhosted.org/packages/fe/1b/25b7cccd4519c0b23c2dd636ad39d381abf113085ce4f7bec2b0dc755eb1/pydantic_core-2.33.2-cp311-cp311-win_amd64.whl", hash = "sha256:1e063337ef9e9820c77acc768546325ebe04ee38b08703244c1309cccc4f1bab", size = 1952909, upload-time = "2025-04-23T18:31:22.371Z" },
    { url = "https://files.pythonhosted.org/packages/49/a9/d809358e49126438055884c4366a1f6227f0f84f635a9014e2deb9b9de54/pydantic_core-2.33.2-cp311-cp311-win_arm64.whl", hash = "sha256:6b99022f1d19bc32a4c2a0d544fc9a76e3be90f0b3f4af413f87d38749300e65", size = 1897786, upload-time = "2025-04-23T18:31:24.161Z" },
    { url = "https://files.pythonhosted.org/packages/18/8a/2b41c97f554ec8c71f2a8a5f85cb56a8b0956addfe8b0efb5b3d77e8bdc3/pydantic_core-2.33.2-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:a7ec89dc587667f22b6a0b6579c249fca9026ce7c333fc142ba42411fa243cdc", size = 2009000, upload-time = "2025-04-23T18:31:25.863Z" },
    { url = "https://files.pythonhosted.org/packages/a1/02/6224312aacb3c8ecbaa959897af57181fb6cf3a3d7917fd44d0f2917e6f2/pydantic_core-2.33.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:3c6db6e52c6d70aa0d00d45cdb9b40f0433b96380071ea80b09277dba021ddf7", size = 1847996, upload-time = "2025-04-23T18:31:27.341Z" },
    { url = "https://files.pythonhosted.org/packages/d6/46/6dcdf084a523dbe0a0be59d054734b86a981726f221f4562aed313dbcb49/pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4e61206137cbc65e6d5256e1166f88331d3b6238e082d9f74613b9b765fb9025", size = 1880957, upload-time = "2025-04-23T18:31:28.956Z" },
    { url = "https://files.pythonhosted.org/packages/ec/6b/1ec2c03837ac00886ba8160ce041ce4e325b41d06a034adbef11339ae422/pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:eb8c529b2819c37140eb51b914153063d27ed88e3bdc31b71198a198e921e011", size = 1964199, upload-time = "2025-04-23T18:31:31.025Z" },
    { url = "https://files.pythonhosted.org/packages/2d/1d/6bf34d6adb9debd9136bd197ca72642203ce9aaaa85cfcbfcf20f9696e83/pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:c52b02ad8b4e2cf14ca7b3d918f3eb0ee91e63b3167c32591e57c4317e134f8f", size = 2120296, upload-time = "2025-04-23T18:31:32.514Z" },
    { url = "https://files.pythonhosted.org/packages/e0/94/2bd0aaf5a591e974b32a9f7123f16637776c304471a0ab33cf263cf5591a/pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:96081f1605125ba0855dfda83f6f3df5ec90c61195421ba72223de35ccfb2f88", size = 2676109, upload-time = "2025-04-23T18:31:33.958Z" },
    { url = "https://files.pythonhosted.org/packages/f9/41/4b043778cf9c4285d59742281a769eac371b9e47e35f98ad321349cc5d61/pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8f57a69461af2a5fa6e6bbd7a5f60d3b7e6cebb687f55106933188e79ad155c1", size = 2002028, upload-time = "2025-04-23T18:31:39.095Z" },
    { url = "https://files.pythonhosted.org/packages/cb/d5/7bb781bf2748ce3d03af04d5c969fa1308880e1dca35a9bd94e1a96a922e/pydantic_core-2.33.2-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:572c7e6c8bb4774d2ac88929e3d1f12bc45714ae5ee6d9a788a9fb35e60bb04b", size = 2100044, upload-time = "2025-04-23T18:31:41.034Z" },
    { url = "https://files.pythonhosted.org/packages/fe/36/def5e53e1eb0ad896785702a5bbfd25eed546cdcf4087ad285021a90ed53/pydantic_core-2.33.2-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:db4b41f9bd95fbe5acd76d89920336ba96f03e149097365afe1cb092fceb89a1", size = 2058881, upload-time = "2025-04-23T18:31:42.757Z" },
    { url = "https://files.pythonhosted.org/packages/01/6c/57f8d70b2ee57fc3dc8b9610315949837fa8c11d86927b9bb044f8705419/pydantic_core-2.33.2-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:fa854f5cf7e33842a892e5c73f45327760bc7bc516339fda888c75ae60edaeb6", size = 2227034, upload-time = "2025-04-23T18:31:44.304Z" },
    { url = "https://files.pythonhosted.org/packages/27/b9/9c17f0396a82b3d5cbea4c24d742083422639e7bb1d5bf600e12cb176a13/pydantic_core-2.33.2-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:5f483cfb75ff703095c59e365360cb73e00185e01aaea067cd19acffd2ab20ea", size = 2234187, upload-time = "2025-04-23T18:31:45.891Z" },
    { url = "https://files.pythonhosted.org/packages/b0/6a/adf5734ffd52bf86d865093ad70b2ce543415e0e356f6cacabbc0d9ad910/pydantic_core-2.33.2-cp312-cp312-win32.whl", hash = "sha256:9cb1da0f5a471435a7bc7e439b8a728e8b61e59784b2af70d7c169f8dd8ae290", size = 1892628, upload-time = "2025-04-23T18:31:47.819Z" },
    { url = "https://files.pythonhosted.org/packages/43/e4/5479fecb3606c1368d496a825d8411e126133c41224c1e7238be58b87d7e/pydantic_core-2.33.2-cp312-cp312-win_amd64.whl", hash = "sha256:f941635f2a3d96b2973e867144fde513665c87f13fe0e193c158ac51bfaaa7b2", size = 1955866, upload-time = "2025-04-23T18:31:49.635Z" },
    { url = "https://files.pythonhosted.org/packages/0d/24/8b11e8b3e2be9dd82df4b11408a67c61bb4dc4f8e11b5b0fc888b38118b5/pydantic_core-2.33.2-cp312-cp312-win_arm64.whl", hash = "sha256:cca3868ddfaccfbc4bfb1d608e2ccaaebe0ae628e1416aeb9c4d88c001bb45ab", size = 1888894, upload-time = "2025-04-23T18:31:51.609Z" },
    { url = "https://files.pythonhosted.org/packages/46/8c/99040727b41f56616573a28771b1bfa08a3d3fe74d3d513f01251f79f172/pydantic_core-2.33.2-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:1082dd3e2d7109ad8b7da48e1d4710c8d06c253cbc4a27c1cff4fbcaa97a9e3f", size = 2015688, upload-time = "2025-04-23T18:31:53.175Z" },
    { url = "https://files.pythonhosted.org/packages/3a/cc/5999d1eb705a6cefc31f0b4a90e9f7fc400539b1a1030529700cc1b51838/pydantic_core-2.33.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f517ca031dfc037a9c07e748cefd8d96235088b83b4f4ba8939105d20fa1dcd6", size = 1844808, upload-time = "2025-04-23T18:31:54.79Z" },
    { url = "https://files.pythonhosted.org/packages/6f/5e/a0a7b8885c98889a18b6e376f344da1ef323d270b44edf8174d6bce4d622/pydantic_core-2.33.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0a9f2c9dd19656823cb8250b0724ee9c60a82f3cdf68a080979d13092a3b0fef", size = 1885580, upload-time = "2025-04-23T18:31:57.393Z" },
    { url = "https://files.pythonhosted.org/packages/3b/2a/953581f343c7d11a304581156618c3f592435523dd9d79865903272c256a/pydantic_core-2.33.2-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:2b0a451c263b01acebe51895bfb0e1cc842a5c666efe06cdf13846c7418caa9a", size = 1973859, upload-time = "2025-04-23T18:31:59.065Z" },
    { url = "https://files.pythonhosted.org/packages/e6/55/f1a813904771c03a3f97f676c62cca0c0a4138654107c1b61f19c644868b/pydantic_core-2.33.2-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1ea40a64d23faa25e62a70ad163571c0b342b8bf66d5fa612ac0dec4f069d916", size = 2120810, upload-time = "2025-04-23T18:32:00.78Z" },
    { url = "https://files.pythonhosted.org/packages/aa/c3/053389835a996e18853ba107a63caae0b9deb4a276c6b472931ea9ae6e48/pydantic_core-2.33.2-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:0fb2d542b4d66f9470e8065c5469ec676978d625a8b7a363f07d9a501a9cb36a", size = 2676498, upload-time = "2025-04-23T18:32:02.418Z" },
    { url = "https://files.pythonhosted.org/packages/eb/3c/f4abd740877a35abade05e437245b192f9d0ffb48bbbbd708df33d3cda37/pydantic_core-2.33.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9fdac5d6ffa1b5a83bca06ffe7583f5576555e6c8b3a91fbd25ea7780f825f7d", size = 2000611, upload-time = "2025-04-23T18:32:04.152Z" },
    { url = "https://files.pythonhosted.org/packages/59/a7/63ef2fed1837d1121a894d0ce88439fe3e3b3e48c7543b2a4479eb99c2bd/pydantic_core-2.33.2-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:04a1a413977ab517154eebb2d326da71638271477d6ad87a769102f7c2488c56", size = 2107924, upload-time = "2025-04-23T18:32:06.129Z" },
    { url = "https://files.pythonhosted.org/packages/04/8f/2551964ef045669801675f1cfc3b0d74147f4901c3ffa42be2ddb1f0efc4/pydantic_core-2.33.2-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:c8e7af2f4e0194c22b5b37205bfb293d166a7344a5b0d0eaccebc376546d77d5", size = 2063196, upload-time = "2025-04-23T18:32:08.178Z" },
    { url = "https://files.pythonhosted.org/packages/26/bd/d9602777e77fc6dbb0c7db9ad356e9a985825547dce5ad1d30ee04903918/pydantic_core-2.33.2-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:5c92edd15cd58b3c2d34873597a1e20f13094f59cf88068adb18947df5455b4e", size = 2236389, upload-time = "2025-04-23T18:32:10.242Z" },
    { url = "https://files.pythonhosted.org/packages/42/db/0e950daa7e2230423ab342ae918a794964b053bec24ba8af013fc7c94846/pydantic_core-2.33.2-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:65132b7b4a1c0beded5e057324b7e16e10910c106d43675d9bd87d4f38dde162", size = 2239223, upload-time = "2025-04-23T18:32:12.382Z" },
    { url = "https://files.pythonhosted.org/packages/58/4d/4f937099c545a8a17eb52cb67fe0447fd9a373b348ccfa9a87f141eeb00f/pydantic_core-2.33.2-cp313-cp313-win32.whl", hash = "sha256:52fb90784e0a242bb96ec53f42196a17278855b0f31ac7c3cc6f5c1ec4811849", size = 1900473, upload-time = "2025-04-23T18:32:14.034Z" },
    { url = "https://files.pythonhosted.org/packages/a0/75/4a0a9bac998d78d889def5e4ef2b065acba8cae8c93696906c3a91f310ca/pydantic_core-2.33.2-cp313-cp313-win_amd64.whl", hash = "sha256:c083a3bdd5a93dfe480f1125926afcdbf2917ae714bdb80b36d34318b2bec5d9", size = 1955269, upload-time = "2025-04-23T18:32:15.783Z" },
    { url = "https://files.pythonhosted.org/packages/f9/86/1beda0576969592f1497b4ce8e7bc8cbdf614c352426271b1b10d5f0aa64/pydantic_core-2.33.2-cp313-cp313-win_arm64.whl", hash = "sha256:e80b087132752f6b3d714f041ccf74403799d3b23a72722ea2e6ba2e892555b9", size = 1893921, upload-time = "2025-04-23T18:32:18.473Z" },
    { url = "https://files.pythonhosted.org/packages/a4/7d/e09391c2eebeab681df2b74bfe6c43422fffede8dc74187b2b0bf6fd7571/pydantic_core-2.33.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:61c18fba8e5e9db3ab908620af374db0ac1baa69f0f32df4f61ae23f15e586ac", size = 1806162, upload-time = "2025-04-23T18:32:20.188Z" },
    { url = "https://files.pythonhosted.org/packages/f1/3d/847b6b1fed9f8ed3bb95a9ad04fbd0b212e832d4f0f50ff4d9ee5a9f15cf/pydantic_core-2.33.2-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:95237e53bb015f67b63c91af7518a62a8660376a6a0db19b89acc77a4d6199f5", size = 1981560, upload-time = "2025-04-23T18:32:22.354Z" },
    { url = "https://files.pythonhosted.org/packages/6f/9a/e73262f6c6656262b5fdd723ad90f518f579b7bc8622e43a942eec53c938/pydantic_core-2.33.2-cp313-cp313t-win_amd64.whl", hash = "sha256:c2fc0a768ef76c15ab9238afa6da7f69895bb5d1ee83aeea2e3509af4472d0b9", size = 1935777, upload-time = "2025-04-23T18:32:25.088Z" },
    { url = "https://files.pythonhosted.org/packages/30/68/373d55e58b7e83ce371691f6eaa7175e3a24b956c44628eb25d7da007917/pydantic_core-2.33.2-pp310-pypy310_pp73-macosx_10_12_x86_64.whl", hash = "sha256:5c4aa4e82353f65e548c476b37e64189783aa5384903bfea4f41580f255fddfa", size = 2023982, upload-time = "2025-04-23T18:32:53.14Z" },
    { url = "https://files.pythonhosted.org/packages/a4/16/145f54ac08c96a63d8ed6442f9dec17b2773d19920b627b18d4f10a061ea/pydantic_core-2.33.2-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:d946c8bf0d5c24bf4fe333af284c59a19358aa3ec18cb3dc4370080da1e8ad29", size = 1858412, upload-time = "2025-04-23T18:32:55.52Z" },
    { url = "https://files.pythonhosted.org/packages/41/b1/c6dc6c3e2de4516c0bb2c46f6a373b91b5660312342a0cf5826e38ad82fa/pydantic_core-2.33.2-pp310-pypy310_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:87b31b6846e361ef83fedb187bb5b4372d0da3f7e28d85415efa92d6125d6e6d", size = 1892749, upload-time = "2025-04-23T18:32:57.546Z" },
    { url = "https://files.pythonhosted.org/packages/12/73/8cd57e20afba760b21b742106f9dbdfa6697f1570b189c7457a1af4cd8a0/pydantic_core-2.33.2-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:aa9d91b338f2df0508606f7009fde642391425189bba6d8c653afd80fd6bb64e", size = 2067527, upload-time = "2025-04-23T18:32:59.771Z" },
    { url = "https://files.pythonhosted.org/packages/e3/d5/0bb5d988cc019b3cba4a78f2d4b3854427fc47ee8ec8e9eaabf787da239c/pydantic_core-2.33.2-pp310-pypy310_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2058a32994f1fde4ca0480ab9d1e75a0e8c87c22b53a3ae66554f9af78f2fe8c", size = 2108225, upload-time = "2025-04-23T18:33:04.51Z" },
    { url = "https://files.pythonhosted.org/packages/f1/c5/00c02d1571913d496aabf146106ad8239dc132485ee22efe08085084ff7c/pydantic_core-2.33.2-pp310-pypy310_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:0e03262ab796d986f978f79c943fc5f620381be7287148b8010b4097f79a39ec", size = 2069490, upload-time = "2025-04-23T18:33:06.391Z" },
    { url = "https://files.pythonhosted.org/packages/22/a8/dccc38768274d3ed3a59b5d06f59ccb845778687652daa71df0cab4040d7/pydantic_core-2.33.2-pp310-pypy310_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:1a8695a8d00c73e50bff9dfda4d540b7dee29ff9b8053e38380426a85ef10052", size = 2237525, upload-time = "2025-04-23T18:33:08.44Z" },
    { url = "https://files.pythonhosted.org/packages/d4/e7/4f98c0b125dda7cf7ccd14ba936218397b44f50a56dd8c16a3091df116c3/pydantic_core-2.33.2-pp310-pypy310_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:fa754d1850735a0b0e03bcffd9d4b4343eb417e47196e4485d9cca326073a42c", size = 2238446, upload-time = "2025-04-23T18:33:10.313Z" },
    { url = "https://files.pythonhosted.org/packages/ce/91/2ec36480fdb0b783cd9ef6795753c1dea13882f2e68e73bce76ae8c21e6a/pydantic_core-2.33.2-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:a11c8d26a50bfab49002947d3d237abe4d9e4b5bdc8846a63537b6488e197808", size = 2066678, upload-time = "2025-04-23T18:33:12.224Z" },
    { url = "https://files.pythonhosted.org/packages/7b/27/d4ae6487d73948d6f20dddcd94be4ea43e74349b56eba82e9bdee2d7494c/pydantic_core-2.33.2-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:dd14041875d09cc0f9308e37a6f8b65f5585cf2598a53aa0123df8b129d481f8", size = 2025200, upload-time = "2025-04-23T18:33:14.199Z" },
    { url = "https://files.pythonhosted.org/packages/f1/b8/b3cb95375f05d33801024079b9392a5ab45267a63400bf1866e7ce0f0de4/pydantic_core-2.33.2-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:d87c561733f66531dced0da6e864f44ebf89a8fba55f31407b00c2f7f9449593", size = 1859123, upload-time = "2025-04-23T18:33:16.555Z" },
    { url = "https://files.pythonhosted.org/packages/05/bc/0d0b5adeda59a261cd30a1235a445bf55c7e46ae44aea28f7bd6ed46e091/pydantic_core-2.33.2-pp311-pypy311_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2f82865531efd18d6e07a04a17331af02cb7a651583c418df8266f17a63c6612", size = 1892852, upload-time = "2025-04-23T18:33:18.513Z" },
    { url = "https://files.pythonhosted.org/packages/3e/11/d37bdebbda2e449cb3f519f6ce950927b56d62f0b84fd9cb9e372a26a3d5/pydantic_core-2.33.2-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2bfb5112df54209d820d7bf9317c7a6c9025ea52e49f46b6a2060104bba37de7", size = 2067484, upload-time = "2025-04-23T18:33:20.475Z" },
    { url = "https://files.pythonhosted.org/packages/8c/55/1f95f0a05ce72ecb02a8a8a1c3be0579bbc29b1d5ab68f1378b7bebc5057/pydantic_core-2.33.2-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:64632ff9d614e5eecfb495796ad51b0ed98c453e447a76bcbeeb69615079fc7e", size = 2108896, upload-time = "2025-04-23T18:33:22.501Z" },
    { url = "https://files.pythonhosted.org/packages/53/89/2b2de6c81fa131f423246a9109d7b2a375e83968ad0800d6e57d0574629b/pydantic_core-2.33.2-pp311-pypy311_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:f889f7a40498cc077332c7ab6b4608d296d852182211787d4f3ee377aaae66e8", size = 2069475, upload-time = "2025-04-23T18:33:24.528Z" },
    { url = "https://files.pythonhosted.org/packages/b8/e9/1f7efbe20d0b2b10f6718944b5d8ece9152390904f29a78e68d4e7961159/pydantic_core-2.33.2-pp311-pypy311_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:de4b83bb311557e439b9e186f733f6c645b9417c84e2eb8203f3f820a4b988bf", size = 2239013, upload-time = "2025-04-23T18:33:26.621Z" },
    { url = "https://files.pythonhosted.org/packages/3c/b2/5309c905a93811524a49b4e031e9851a6b00ff0fb668794472ea7746b448/pydantic_core-2.33.2-pp311-pypy311_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:82f68293f055f51b51ea42fafc74b6aad03e70e191799430b90c13d643059ebb", size = 2238715, upload-time = "2025-04-23T18:33:28.656Z" },
    { url = "https://files.pythonhosted.org/packages/32/56/8a7ca5d2cd2cda1d245d34b1c9a942920a718082ae8e54e5f3e5a58b7add/pydantic_core-2.33.2-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:329467cecfb529c925cf2bbd4d60d2c509bc2fb52a20c1045bf09bb70971a9c1", size = 2066757, upload-time = "2025-04-23T18:33:30.645Z" },
]

[[package]]
name = "pydantic-settings"
version = "2.10.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pydantic" },
    { name = "python-dotenv" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/68/85/1ea668bbab3c50071ca613c6ab30047fb36ab0da1b92fa8f17bbc38fd36c/pydantic_settings-2.10.1.tar.gz", hash = "sha256:06f0062169818d0f5524420a360d632d5857b83cffd4d42fe29597807a1614ee", size = 172583, upload-time = "2025-06-24T13:26:46.841Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/58/f0/427018098906416f580e3cf1366d3b1abfb408a0652e9f31600c24a1903c/pydantic_settings-2.10.1-py3-none-any.whl", hash = "sha256:a60952460b99cf661dc25c29c0ef171721f98bfcb52ef8d9ea4c943d7c8cc796", size = 45235, upload-time = "2025-06-24T13:26:45.485Z" },
]

[[package]]
name = "pygments"
version = "2.19.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b0/77/a5b8c569bf593b0140bde72ea885a803b82086995367bf2037de0159d924/pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887", size = 4968631, upload-time = "2025-06-21T13:39:12.283Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c7/21/705964c7812476f378728bdf590ca4b771ec72385c533964653c68e86bdc/pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b", size = 1225217, upload-time = "2025-06-21T13:39:07.939Z" },
]

[[package]]
name = "pyinstrument"
version = "5.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f9/d0/665828770e8fcd5c50880dc83f03811f814d6260bc6a8068dca0a520e68a/pyinstrument-5.0.2.tar.gz", hash = "sha256:e466033ead16a48ffa8bedbd633b90d416fa772b3b22f61226882ace0371f5f3", size = 263930, upload-time = "2025-05-24T15:47:13.358Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9c/25/f64d0be5f574d2df9ddac3e7a381863f92d8ad30170b1a9de0cf805f4318/pyinstrument-5.0.2-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:1aeaf6b39ad40b3f03bea5fa3a9bd453a92aeb721dde29c1597f842ed9c8566a", size = 129638, upload-time = "2025-05-24T15:45:20.113Z" },
    { url = "https://files.pythonhosted.org/packages/6e/b8/bc6657f91a8d2f7cf58b0993aa4e6cf20e027b53aca65c2464a50738d711/pyinstrument-5.0.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:d734bd236d00e0e7f950019c689eaba1c9dd15e355867d8926c8b18b6077b221", size = 122220, upload-time = "2025-05-24T15:45:22.4Z" },
    { url = "https://files.pythonhosted.org/packages/63/5f/9a7edf13333015a9ccfd3fcf5c75ea793fbb30b153aebf6c6ace40a607b2/pyinstrument-5.0.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:520208a9b6c3985473aa9c3f30875ae5e78e77a81081df1d8aeb4fd8b4caf197", size = 146928, upload-time = "2025-05-24T15:45:23.802Z" },
    { url = "https://files.pythonhosted.org/packages/f2/f9/f7d7b28c9038f1a570e96c8eea2a9ffeeb3ee9e75cfc74a370554776f1a6/pyinstrument-5.0.2-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:75e115b759288b8d65a0bf31a34a542ae102c58ef407e0614a43e0c39d261875", size = 157136, upload-time = "2025-05-24T15:45:25.629Z" },
    { url = "https://files.pythonhosted.org/packages/db/ee/aa99f275b3c5f0f32ccd37f77cb64e57597a1f26280aec03a50d2158eab7/pyinstrument-5.0.2-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:091f93e6787c485a7ddf670608c00448e858a056677fc25ce349f8e44d6a9e54", size = 144680, upload-time = "2025-05-24T15:45:27.06Z" },
    { url = "https://files.pythonhosted.org/packages/ae/77/cd7300a5e099c4ad971a647ea8fb9bd081482a9e5751479034e206cd1f69/pyinstrument-5.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:28b07971afa2652cb4f2bdcffaef11aefa32b5384c0cfb32acf9955e96dd8df8", size = 145624, upload-time = "2025-05-24T15:45:28.517Z" },
    { url = "https://files.pythonhosted.org/packages/30/59/1957e2ca2277ecc69e247383527df331002e23940d5b0a79fc5f3b870d60/pyinstrument-5.0.2-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:e1bcb28a21b80eea5986eb5cb3180689b1d489b7c6fddf34e1f4df1f95d467ad", size = 145901, upload-time = "2025-05-24T15:45:30.365Z" },
    { url = "https://files.pythonhosted.org/packages/7e/ae/396ebdf387cde376ac4b70d52f3df07374f2501ac4c09992dadf641cd71f/pyinstrument-5.0.2-cp310-cp310-musllinux_1_2_armv7l.whl", hash = "sha256:80d28162070ff40c6d2ac7dc15b933ba20ef49e891a2e650cd2b91d30cd262b2", size = 145355, upload-time = "2025-05-24T15:45:31.859Z" },
    { url = "https://files.pythonhosted.org/packages/48/5b/fec77476a9b4a316861b29f14cd0962871ad5c54c21e41c540f7c18c950c/pyinstrument-5.0.2-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:c75e52a9bf76f084ba074323835cba4927ab3e572adfc96439698b097e523780", size = 145008, upload-time = "2025-05-24T15:45:33.417Z" },
    { url = "https://files.pythonhosted.org/packages/fd/75/dcd391ca2790b32e41bbd49ad33626e85eb1ce00116b273d5e1d99b3e829/pyinstrument-5.0.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:ccefdd7dd938548ada43c95b24c42ec57e258ac7994a5ec7e4cc934fa4f1743b", size = 145396, upload-time = "2025-05-24T15:45:34.915Z" },
    { url = "https://files.pythonhosted.org/packages/ca/5c/64e026ccf2c7908d10882955993e73ac35a1a77426bde2617973deeda07c/pyinstrument-5.0.2-cp310-cp310-win32.whl", hash = "sha256:6b617fb024c244738aa2f6b8c2a25853eac765360ac91062578bbbcc8e22ebfe", size = 123419, upload-time = "2025-05-24T15:45:36.276Z" },
    { url = "https://files.pythonhosted.org/packages/d5/7c/7d221db96d461c7d28897499bdad55a8ae5ded983f60743bdfbf17438c20/pyinstrument-5.0.2-cp310-cp310-win_amd64.whl", hash = "sha256:6788c8f93c1a6e0ad8d0ccde1631d17eca3839945d0fa4d506cf5d4bd7a26b77", size = 124299, upload-time = "2025-05-24T15:45:37.642Z" },
    { url = "https://files.pythonhosted.org/packages/fc/f2/b3f2416740be762fdfb052b63e1d85591682fa1d2ea6ee1b10db774f6350/pyinstrument-5.0.2-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:0eec7a263cc1ccfb101594e13256115366338fee2a156be4172fe5315f71ec45", size = 129386, upload-time = "2025-05-24T15:45:39.429Z" },
    { url = "https://files.pythonhosted.org/packages/6b/fa/a55b0bf911041b51d2a7a0e8a3feef5ed5ddb48ff0943fc667079955c14c/pyinstrument-5.0.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:ddd5effefb470d7f1886dc16467501b866e3b5883cf74773f13179e718b28393", size = 122100, upload-time = "2025-05-24T15:45:41.253Z" },
    { url = "https://files.pythonhosted.org/packages/a5/e1/c42b94c795bc89d5a486ad7ef349fe3b7a8c3a4e730c09b5fa54af616a6b/pyinstrument-5.0.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6e7458a6aa4048c1703354fc8a4a3c8b59d27b1409aafb707cf339d3c0bc794c", size = 145385, upload-time = "2025-05-24T15:45:43.024Z" },
    { url = "https://files.pythonhosted.org/packages/ff/41/b511141cc336ffeac284cce7d121f05802ffea4ab2c19df8869adda49743/pyinstrument-5.0.2-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:2373dd699711463011ec14e4918427a777f7ab73b31ae374d960725dbd5d5a28", size = 156093, upload-time = "2025-05-24T15:45:44.755Z" },
    { url = "https://files.pythonhosted.org/packages/b2/7e/4a7bc4f1c60d4886efb7397fd5bdcc7e537d01ec7372824cd834fff967a1/pyinstrument-5.0.2-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:38ef498fbe71c2bbd11247b71e722290da93a367d88a5a8e0f66f6cc764c2b60", size = 143136, upload-time = "2025-05-24T15:45:46.469Z" },
    { url = "https://files.pythonhosted.org/packages/d8/69/0ac06cf609153fc5eb30ccc0071ce300a181f422836ca7ce8cd431ac3ab4/pyinstrument-5.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0a58a8a50f0cb3ee1c2e43ffec51bf48f48945e141feed7ccd9194917b97fe5b", size = 144077, upload-time = "2025-05-24T15:45:48.333Z" },
    { url = "https://files.pythonhosted.org/packages/e3/24/12bd82822393f708e5da8f6c0b82def3f0cbe1f4fbd72a082688c583d7fa/pyinstrument-5.0.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:ad2a97c79ecf0e610df292abb5c46d01a4f99778598881d6e918650fa39801b6", size = 144545, upload-time = "2025-05-24T15:45:50.137Z" },
    { url = "https://files.pythonhosted.org/packages/c9/62/40e7511fa46247ca56734d34e2d2eb6b14390c72b155255ecd1b2288d02d/pyinstrument-5.0.2-cp311-cp311-musllinux_1_2_armv7l.whl", hash = "sha256:57ec0277042ee198eb749b76a975fe60f006cd51ea0c7ce3054c937577d19315", size = 144010, upload-time = "2025-05-24T15:45:52.256Z" },
    { url = "https://files.pythonhosted.org/packages/82/77/6d40880dc46a6243951ad7cd50a77f26f6ad126b80d803616934efccf539/pyinstrument-5.0.2-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:73d34047266f27acb67218e331288c0241cf0080fe4b87dfad5596236c71abd7", size = 143746, upload-time = "2025-05-24T15:45:53.702Z" },
    { url = "https://files.pythonhosted.org/packages/9b/a2/08b056d2420199dab877c665ed45bb685863dc5b83d31b2c4311430b2bbd/pyinstrument-5.0.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:cfdc23284a8e2f27637b357c226a15d52b96608d9dde187b68dfe33a947f4908", size = 143928, upload-time = "2025-05-24T15:45:55.103Z" },
    { url = "https://files.pythonhosted.org/packages/39/a1/bab336f70cd5f798d7fa21ec92784b99d3b2df0b5c1736a64fdaa4521004/pyinstrument-5.0.2-cp311-cp311-win32.whl", hash = "sha256:3e6fa135aee6af2c608e912d8d07906bbac3c5e564d94f92721831a957297c26", size = 123395, upload-time = "2025-05-24T15:45:56.469Z" },
    { url = "https://files.pythonhosted.org/packages/f2/15/8a7ac268ffe913aa64bb42ad43315dd0fc3ac493d451a50d4431ecb736c2/pyinstrument-5.0.2-cp311-cp311-win_amd64.whl", hash = "sha256:6317df42a98a8074ccd25af5482312ec59a1f27c05dab408eb3c7b2081242733", size = 124198, upload-time = "2025-05-24T15:45:57.814Z" },
    { url = "https://files.pythonhosted.org/packages/95/36/4afdffbc4fd77dd0155c8943101f175e701ba00cb374c5e84e64790a2a32/pyinstrument-5.0.2-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:d0b680ef269b528d8dcd8151362fba9683b0ac22ffe74cc8161c33b53c65b899", size = 129527, upload-time = "2025-05-24T15:45:59.216Z" },
    { url = "https://files.pythonhosted.org/packages/96/fe/7ea5af73d65f8f22585005f6e2ce1016fb3145a8ecc1ded51f965c2e98cc/pyinstrument-5.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:1c70b50ec90ae793b74733a6fc992723c6ee27c0fcb7d99848239316ded61189", size = 122068, upload-time = "2025-05-24T15:46:01.05Z" },
    { url = "https://files.pythonhosted.org/packages/3f/d2/cf8f3b8fde3f3b6768f8407c681fb57e7b5a5bf5e7450a9fbec15164987b/pyinstrument-5.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3aae5f4f78515009f72393fdb271a15861534a586401383785f823cf8f60aa02", size = 146679, upload-time = "2025-05-24T15:46:02.841Z" },
    { url = "https://files.pythonhosted.org/packages/8d/e2/6c00273778596560c7033cfee34aab07da6009f32c5a4dbcc35b64700e73/pyinstrument-5.0.2-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:3aec8bc3d1c064ff849ca3568d6b0a7cfa0162d590a9d4d250c7118d09518b22", size = 157606, upload-time = "2025-05-24T15:46:04.551Z" },
    { url = "https://files.pythonhosted.org/packages/4c/cc/ec099f566e381f8e5db21d9523dd97b3255047813da57481ab3f45436089/pyinstrument-5.0.2-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:28d87fac2bc0fed802b14a26982440f36c85dc53f303530ff7665a6e470315bb", size = 144317, upload-time = "2025-05-24T15:46:05.996Z" },
    { url = "https://files.pythonhosted.org/packages/37/a7/e2e54bf6d996b3c807534dbc4fe270f373660b89871c63965d3f895c285d/pyinstrument-5.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:3b9caac53c7eda8187ed122d4f7fcc6e3392f04c583d6d70b373351cede2b829", size = 145622, upload-time = "2025-05-24T15:46:07.334Z" },
    { url = "https://files.pythonhosted.org/packages/ef/c6/0b084ddf8d836076e04912ea83ccae0f83bf4897d0168b0fd7684efdc2a4/pyinstrument-5.0.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8124419e8731a7bdbb9f7f885a8956806a4e9ab9dd19294f8a99e74c0bbdd327", size = 145645, upload-time = "2025-05-24T15:46:09.236Z" },
    { url = "https://files.pythonhosted.org/packages/b3/4d/3e542c5986cc30bc86c304492f4696e58dc03d1816d35c5b2cabfac1d01e/pyinstrument-5.0.2-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:9990d9bd05fbb4fa83f24f0a62989b8e0a3ac15ff0fa19b49348c8ef5f9db50a", size = 145619, upload-time = "2025-05-24T15:46:10.643Z" },
    { url = "https://files.pythonhosted.org/packages/a7/a7/1e4664bf5ada1cff56852d10954b1ff5a39dad17b9b98a2f27054a0c0d95/pyinstrument-5.0.2-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:1dc35f3d200866a43d4bc7570799a405f001591c8f19a30eb7a983a717c1e1f7", size = 145049, upload-time = "2025-05-24T15:46:12.019Z" },
    { url = "https://files.pythonhosted.org/packages/fb/59/08a5237c8d1343842ac9ed3c661dce40c450f1750128fd4789ad80539253/pyinstrument-5.0.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:a335a40d0ba1fe3658ef1a5ff2fc7a6870905828014645cb19dab5c1de379447", size = 145451, upload-time = "2025-05-24T15:46:13.49Z" },
    { url = "https://files.pythonhosted.org/packages/53/d0/321b5301e36ac1577dbf73cb49769779c41ebf72ba70a3f6f62d34df902b/pyinstrument-5.0.2-cp312-cp312-win32.whl", hash = "sha256:29e565ce85e03d2541330a8174124c1ecdb073d945962a8eb738d3b1c806ac83", size = 123491, upload-time = "2025-05-24T15:46:15.319Z" },
    { url = "https://files.pythonhosted.org/packages/ae/a6/40f05febe6ab0856b4bfa119113d550d868d94a36b501e6b9fd64379b4ba/pyinstrument-5.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:300b0cc453ffe7661d5f3ceb94cdd98996fd9118f5ff1182b5336489c7d4e45c", size = 124277, upload-time = "2025-05-24T15:46:16.693Z" },
    { url = "https://files.pythonhosted.org/packages/03/88/48654e4b8c6853f218e0506e0609060a54559500b3af5ed6ac752ac4d64f/pyinstrument-5.0.2-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:8141a5f78b927a88de46fb2bbb17e710e41d16e161fca99991635ff7196dbd5d", size = 129528, upload-time = "2025-05-24T15:46:18.108Z" },
    { url = "https://files.pythonhosted.org/packages/92/a7/885418b733350f6c2b1d8fcca322a1eee87216a266ac516d7aefd6757ec8/pyinstrument-5.0.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:12a0095ae408dbbdd429501fd4c6a3ab51d1aeff5f31be36cc3eedc8c4870ede", size = 122072, upload-time = "2025-05-24T15:46:19.513Z" },
    { url = "https://files.pythonhosted.org/packages/a4/d5/dd0b323d2949d1a3ee0531ec6cdd66c3c69c13b9a8739aeec929a0b55fd2/pyinstrument-5.0.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:eca651d840e8e75ae5330abfc5c90f6ea4af3f78f9f0269231328305a5f9c667", size = 146874, upload-time = "2025-05-24T15:46:21.38Z" },
    { url = "https://files.pythonhosted.org/packages/aa/3b/429572b57c9ae2874e86c48db91ddcd5d619bd798f73d7d2e51b28abb08d/pyinstrument-5.0.2-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:89d6ffc5459b19f1c85d4433bb9bbc8925ec04a8d7caf2694218b1f557555f23", size = 155257, upload-time = "2025-05-24T15:46:22.791Z" },
    { url = "https://files.pythonhosted.org/packages/7a/98/03cd22f68607362fd8d1ba72e6367104a9dc32bd4a0dbafc823c4e366f35/pyinstrument-5.0.2-cp313-cp313-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:4c84845ccc5318072708dc5535b6bedd54494e92a68e282e6b97b53c1db65331", size = 144380, upload-time = "2025-05-24T15:46:24.26Z" },
    { url = "https://files.pythonhosted.org/packages/eb/c4/40d7b4be6c9620c4d9bbe9788eb9bac892f386c9bd40f1937464b2b95c09/pyinstrument-5.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6511092384b5729bbbf4b35534120d2969c5fdfd4f39080badedd973676b8725", size = 145794, upload-time = "2025-05-24T15:46:25.751Z" },
    { url = "https://files.pythonhosted.org/packages/05/07/3b2084b78521d5bbbc328ca9527fb54fbf645a5e62f25169b49f7bbb0bc3/pyinstrument-5.0.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:73f08cff7a8d9714be15440046289ab1a70cbc429e09967a3a106ac61538773e", size = 145803, upload-time = "2025-05-24T15:46:27.277Z" },
    { url = "https://files.pythonhosted.org/packages/22/eb/e3ffcc8734e3d9f50b6bb750209c3ad0c4626dcc3754529741499d9f1d5c/pyinstrument-5.0.2-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:3905b510cdab1a8255a23fbdedcba4685245cbf814fd80f5b2005b472161d16e", size = 145763, upload-time = "2025-05-24T15:46:28.656Z" },
    { url = "https://files.pythonhosted.org/packages/c6/34/6b94945a02afced9e486e9a6b20de0edcfec543e4942dea96d745e2148ac/pyinstrument-5.0.2-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:cd693a616166679da529168037c294ff25746c7ae5e8b547811fb25bb26439f5", size = 145208, upload-time = "2025-05-24T15:46:30.125Z" },
    { url = "https://files.pythonhosted.org/packages/99/af/0339bbfe52de9a7df01e5a244a5fec4c228d23b1f422a55318fc6d0b9d91/pyinstrument-5.0.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:83a1659a3bc4123c81fcddfcc86608f37bd6a951da9692766c2251500a77ac06", size = 145591, upload-time = "2025-05-24T15:46:31.556Z" },
    { url = "https://files.pythonhosted.org/packages/c8/f4/76a2c652e203c15cbc7aa3f8341e07d1ea865764b3ed9f9a97b3c4a5eda2/pyinstrument-5.0.2-cp313-cp313-win32.whl", hash = "sha256:386d047db6c043dcc86bac592873234a89eaa258460e1ad8f47a11fcc7b024d5", size = 123490, upload-time = "2025-05-24T15:46:32.951Z" },
    { url = "https://files.pythonhosted.org/packages/e4/63/14f5c6253e8c85c758485c7717f542346a0d4487818afc28721912a1574b/pyinstrument-5.0.2-cp313-cp313-win_amd64.whl", hash = "sha256:971c974c061019fa6177a021882255e639399bc15bf71b0a17979830702ad8d3", size = 124287, upload-time = "2025-05-24T15:46:34.333Z" },
]

[[package]]
name = "pyperclip"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/30/23/2f0a3efc4d6a32f3b63cdff36cd398d9701d26cda58e3ab97ac79fb5e60d/pyperclip-1.9.0.tar.gz", hash = "sha256:b7de0142ddc81bfc5c7507eea19da920b92252b548b96186caf94a5e2527d310", size = 20961, upload-time = "2024-06-18T20:38:48.401Z" }

[[package]]
name = "pyreadline3"
version = "3.5.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0f/49/4cea918a08f02817aabae639e3d0ac046fef9f9180518a3ad394e22da148/pyreadline3-3.5.4.tar.gz", hash = "sha256:8d57d53039a1c75adba8e50dd3d992b28143480816187ea5efbd5c78e6c885b7", size = 99839, upload-time = "2024-09-19T02:40:10.062Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/dc/491b7661614ab97483abf2056be1deee4dc2490ecbf7bff9ab5cdbac86e1/pyreadline3-3.5.4-py3-none-any.whl", hash = "sha256:eaf8e6cc3c49bcccf145fc6067ba8643d1df34d604a1ec0eccbf7a18e6d3fae6", size = 83178, upload-time = "2024-09-19T02:40:08.598Z" },
]

[[package]]
name = "pyrepl"
version = "0.11.3.post1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/92/78/65b9a4a4b15f7f5aae84c3edb9d3adc1acb2acc38eb9d5404cd5cf980927/pyrepl-0.11.3.post1.tar.gz", hash = "sha256:0ca7568c8be919b69f99644d29d31738a5b1a87750d06dd36564bcfad278d402", size = 50954, upload-time = "2025-04-13T12:21:51.403Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2d/45/02a5e2da58a32ff407b14d38690c1d2f8705bd6909320817b444070dcbb0/pyrepl-0.11.3.post1-py3-none-any.whl", hash = "sha256:59fcd67588892731dc6e7aff106c380d303d54324ff028827804a2b056223d92", size = 55613, upload-time = "2025-04-13T12:21:49.464Z" },
]

[[package]]
name = "pyright"
version = "1.1.402"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "nodeenv" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/aa/04/ce0c132d00e20f2d2fb3b3e7c125264ca8b909e693841210534b1ea1752f/pyright-1.1.402.tar.gz", hash = "sha256:85a33c2d40cd4439c66aa946fd4ce71ab2f3f5b8c22ce36a623f59ac22937683", size = 3888207, upload-time = "2025-06-11T08:48:35.759Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fe/37/1a1c62d955e82adae588be8e374c7f77b165b6cb4203f7d581269959abbc/pyright-1.1.402-py3-none-any.whl", hash = "sha256:2c721f11869baac1884e846232800fe021c33f1b4acb3929cff321f7ea4e2982", size = 5624004, upload-time = "2025-06-11T08:48:33.998Z" },
]

[[package]]
name = "pytest"
version = "8.4.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
    { name = "pygments" },
    { name = "tomli", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/08/ba/45911d754e8eba3d5a841a5ce61a65a685ff1798421ac054f85aa8747dfb/pytest-8.4.1.tar.gz", hash = "sha256:7c67fd69174877359ed9371ec3af8a3d2b04741818c51e5e99cc1742251fa93c", size = 1517714, upload-time = "2025-06-18T05:48:06.109Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/29/16/c8a903f4c4dffe7a12843191437d7cd8e32751d5de349d45d3fe69544e87/pytest-8.4.1-py3-none-any.whl", hash = "sha256:539c70ba6fcead8e78eebbf1115e8b589e7565830d7d006a8723f19ac8a0afb7", size = 365474, upload-time = "2025-06-18T05:48:03.955Z" },
]

[[package]]
name = "pytest-asyncio"
version = "1.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d0/d4/14f53324cb1a6381bef29d698987625d80052bb33932d8e7cbf9b337b17c/pytest_asyncio-1.0.0.tar.gz", hash = "sha256:d15463d13f4456e1ead2594520216b225a16f781e144f8fdf6c5bb4667c48b3f", size = 46960, upload-time = "2025-05-26T04:54:40.484Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/30/05/ce271016e351fddc8399e546f6e23761967ee09c8c568bbfbecb0c150171/pytest_asyncio-1.0.0-py3-none-any.whl", hash = "sha256:4f024da9f1ef945e680dc68610b52550e36590a67fd31bb3b4943979a1f90ef3", size = 15976, upload-time = "2025-05-26T04:54:39.035Z" },
]

[[package]]
name = "pytest-cov"
version = "6.2.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "coverage", extra = ["toml"] },
    { name = "pluggy" },
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/18/99/668cade231f434aaa59bbfbf49469068d2ddd945000621d3d165d2e7dd7b/pytest_cov-6.2.1.tar.gz", hash = "sha256:25cc6cc0a5358204b8108ecedc51a9b57b34cc6b8c967cc2c01a4e00d8a67da2", size = 69432, upload-time = "2025-06-12T10:47:47.684Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
]

[[package]]
name = "pytest-env"
version = "1.1.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pytest" },
    { name = "tomli", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/1f/31/27f28431a16b83cab7a636dce59cf397517807d247caa38ee67d65e71ef8/pytest_env-1.1.5.tar.gz", hash = "sha256:91209840aa0e43385073ac464a554ad2947cc2fd663a9debf88d03b01e0cc1cf", size = 8911, upload-time = "2024-09-17T22:39:18.566Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/de/b8/87cfb16045c9d4092cfcf526135d73b88101aac83bc1adcf82dfb5fd3833/pytest_env-1.1.5-py3-none-any.whl", hash = "sha256:ce90cf8772878515c24b31cd97c7fa1f4481cd68d588419fd45f10ecaee6bc30", size = 6141, upload-time = "2024-09-17T22:39:16.942Z" },
]

[[package]]
name = "pytest-flakefinder"
version = "1.1.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ec/53/69c56a93ea057895b5761c5318455804873a6cd9d796d7c55d41c2358125/pytest-flakefinder-1.1.0.tar.gz", hash = "sha256:e2412a1920bdb8e7908783b20b3d57e9dad590cc39a93e8596ffdd493b403e0e", size = 6795, upload-time = "2022-10-26T18:27:54.243Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/33/8b/06787150d0fd0cbd3a8054262b56f91631c7778c1bc91bf4637e47f909ad/pytest_flakefinder-1.1.0-py2.py3-none-any.whl", hash = "sha256:741e0e8eea427052f5b8c89c2b3c3019a50c39a59ce4df6a305a2c2d9ba2bd13", size = 4644, upload-time = "2022-10-26T18:27:52.128Z" },
]

[[package]]
name = "pytest-httpx"
version = "0.35.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "httpx" },
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/1f/89/5b12b7b29e3d0af3a4b9c071ee92fa25a9017453731a38f08ba01c280f4c/pytest_httpx-0.35.0.tar.gz", hash = "sha256:d619ad5d2e67734abfbb224c3d9025d64795d4b8711116b1a13f72a251ae511f", size = 54146, upload-time = "2024-11-28T19:16:54.237Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b0/ed/026d467c1853dd83102411a78126b4842618e86c895f93528b0528c7a620/pytest_httpx-0.35.0-py3-none-any.whl", hash = "sha256:ee11a00ffcea94a5cbff47af2114d34c5b231c326902458deed73f9c459fd744", size = 19442, upload-time = "2024-11-28T19:16:52.787Z" },
]

[[package]]
name = "pytest-report"
version = "0.2.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3b/82/e141da085de0b6dac3f047ae009e136bcedbcfca4ada082a55359d6f735e/pytest-report-0.2.1.tar.gz", hash = "sha256:d382e8db4c52a815d39dae5f21ee5edc0da3ae8ec19a22e55e9be5c60714a39d", size = 3517, upload-time = "2016-05-11T02:08:04.665Z" }

[[package]]
name = "pytest-timeout"
version = "2.4.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ac/82/4c9ecabab13363e72d880f2fb504c5f750433b2b6f16e99f4ec21ada284c/pytest_timeout-2.4.0.tar.gz", hash = "sha256:7e68e90b01f9eff71332b25001f85c75495fc4e3a836701876183c4bcfd0540a", size = 17973, upload-time = "2025-05-05T19:44:34.99Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fa/b6/3127540ecdf1464a00e5a01ee60a1b09175f6913f0644ac748494d9c4b21/pytest_timeout-2.4.0-py3-none-any.whl", hash = "sha256:c42667e5cdadb151aeb5b26d114aff6bdf5a907f176a007a30b940d3d865b5c2", size = 14382, upload-time = "2025-05-05T19:44:33.502Z" },
]

[[package]]
name = "pytest-xdist"
version = "3.7.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "execnet" },
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/49/dc/865845cfe987b21658e871d16e0a24e871e00884c545f246dd8f6f69edda/pytest_xdist-3.7.0.tar.gz", hash = "sha256:f9248c99a7c15b7d2f90715df93610353a485827bc06eefb6566d23f6400f126", size = 87550, upload-time = "2025-05-26T21:18:20.251Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0d/b2/0e802fde6f1c5b2f7ae7e9ad42b83fd4ecebac18a8a8c2f2f14e39dce6e1/pytest_xdist-3.7.0-py3-none-any.whl", hash = "sha256:7d3fbd255998265052435eb9daa4e99b62e6fb9cfb6efd1f858d4d8c0c7f0ca0", size = 46142, upload-time = "2025-05-26T21:18:18.759Z" },
]

[[package]]
name = "python-dotenv"
version = "1.1.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f6/b0/4bc07ccd3572a2f9df7e6782f52b0c6c90dcbb803ac4a167702d7d0dfe1e/python_dotenv-1.1.1.tar.gz", hash = "sha256:a8a6399716257f45be6a007360200409fce5cda2661e3dec71d23dc15f6189ab", size = 41978, upload-time = "2025-06-24T04:21:07.341Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5f/ed/539768cf28c661b5b068d66d96a2f155c4971a5d55684a514c1a0e0dec2f/python_dotenv-1.1.1-py3-none-any.whl", hash = "sha256:31f23644fe2602f88ff55e1f5c79ba497e01224ee7737937930c448e4d0e24dc", size = 20556, upload-time = "2025-06-24T04:21:06.073Z" },
]

[[package]]
name = "python-multipart"
version = "0.0.20"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f3/87/f44d7c9f274c7ee665a29b885ec97089ec5dc034c7f3fafa03da9e39a09e/python_multipart-0.0.20.tar.gz", hash = "sha256:8dd0cab45b8e23064ae09147625994d090fa46f5b0d1e13af944c331a7fa9d13", size = 37158, upload-time = "2024-12-16T19:45:46.972Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/45/58/38b5afbc1a800eeea951b9285d3912613f2603bdf897a4ab0f4bd7f405fc/python_multipart-0.0.20-py3-none-any.whl", hash = "sha256:8a62d3a8335e06589fe01f2a3e178cdcc632f3fbe0d492ad9ee0ec35aab1f104", size = 24546, upload-time = "2024-12-16T19:45:44.423Z" },
]

[[package]]
name = "pyyaml"
version = "6.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/54/ed/79a089b6be93607fa5cdaedf301d7dfb23af5f25c398d5ead2525b063e17/pyyaml-6.0.2.tar.gz", hash = "sha256:d584d9ec91ad65861cc08d42e834324ef890a082e591037abe114850ff7bbc3e", size = 130631, upload-time = "2024-08-06T20:33:50.674Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9b/95/a3fac87cb7158e231b5a6012e438c647e1a87f09f8e0d123acec8ab8bf71/PyYAML-6.0.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:0a9a2848a5b7feac301353437eb7d5957887edbf81d56e903999a75a3d743086", size = 184199, upload-time = "2024-08-06T20:31:40.178Z" },
    { url = "https://files.pythonhosted.org/packages/c7/7a/68bd47624dab8fd4afbfd3c48e3b79efe09098ae941de5b58abcbadff5cb/PyYAML-6.0.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:29717114e51c84ddfba879543fb232a6ed60086602313ca38cce623c1d62cfbf", size = 171758, upload-time = "2024-08-06T20:31:42.173Z" },
    { url = "https://files.pythonhosted.org/packages/49/ee/14c54df452143b9ee9f0f29074d7ca5516a36edb0b4cc40c3f280131656f/PyYAML-6.0.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8824b5a04a04a047e72eea5cec3bc266db09e35de6bdfe34c9436ac5ee27d237", size = 718463, upload-time = "2024-08-06T20:31:44.263Z" },
    { url = "https://files.pythonhosted.org/packages/4d/61/de363a97476e766574650d742205be468921a7b532aa2499fcd886b62530/PyYAML-6.0.2-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7c36280e6fb8385e520936c3cb3b8042851904eba0e58d277dca80a5cfed590b", size = 719280, upload-time = "2024-08-06T20:31:50.199Z" },
    { url = "https://files.pythonhosted.org/packages/6b/4e/1523cb902fd98355e2e9ea5e5eb237cbc5f3ad5f3075fa65087aa0ecb669/PyYAML-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ec031d5d2feb36d1d1a24380e4db6d43695f3748343d99434e6f5f9156aaa2ed", size = 751239, upload-time = "2024-08-06T20:31:52.292Z" },
    { url = "https://files.pythonhosted.org/packages/b7/33/5504b3a9a4464893c32f118a9cc045190a91637b119a9c881da1cf6b7a72/PyYAML-6.0.2-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:936d68689298c36b53b29f23c6dbb74de12b4ac12ca6cfe0e047bedceea56180", size = 695802, upload-time = "2024-08-06T20:31:53.836Z" },
    { url = "https://files.pythonhosted.org/packages/5c/20/8347dcabd41ef3a3cdc4f7b7a2aff3d06598c8779faa189cdbf878b626a4/PyYAML-6.0.2-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:23502f431948090f597378482b4812b0caae32c22213aecf3b55325e049a6c68", size = 720527, upload-time = "2024-08-06T20:31:55.565Z" },
    { url = "https://files.pythonhosted.org/packages/be/aa/5afe99233fb360d0ff37377145a949ae258aaab831bde4792b32650a4378/PyYAML-6.0.2-cp310-cp310-win32.whl", hash = "sha256:2e99c6826ffa974fe6e27cdb5ed0021786b03fc98e5ee3c5bfe1fd5015f42b99", size = 144052, upload-time = "2024-08-06T20:31:56.914Z" },
    { url = "https://files.pythonhosted.org/packages/b5/84/0fa4b06f6d6c958d207620fc60005e241ecedceee58931bb20138e1e5776/PyYAML-6.0.2-cp310-cp310-win_amd64.whl", hash = "sha256:a4d3091415f010369ae4ed1fc6b79def9416358877534caf6a0fdd2146c87a3e", size = 161774, upload-time = "2024-08-06T20:31:58.304Z" },
    { url = "https://files.pythonhosted.org/packages/f8/aa/7af4e81f7acba21a4c6be026da38fd2b872ca46226673c89a758ebdc4fd2/PyYAML-6.0.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:cc1c1159b3d456576af7a3e4d1ba7e6924cb39de8f67111c735f6fc832082774", size = 184612, upload-time = "2024-08-06T20:32:03.408Z" },
    { url = "https://files.pythonhosted.org/packages/8b/62/b9faa998fd185f65c1371643678e4d58254add437edb764a08c5a98fb986/PyYAML-6.0.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1e2120ef853f59c7419231f3bf4e7021f1b936f6ebd222406c3b60212205d2ee", size = 172040, upload-time = "2024-08-06T20:32:04.926Z" },
    { url = "https://files.pythonhosted.org/packages/ad/0c/c804f5f922a9a6563bab712d8dcc70251e8af811fce4524d57c2c0fd49a4/PyYAML-6.0.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5d225db5a45f21e78dd9358e58a98702a0302f2659a3c6cd320564b75b86f47c", size = 736829, upload-time = "2024-08-06T20:32:06.459Z" },
    { url = "https://files.pythonhosted.org/packages/51/16/6af8d6a6b210c8e54f1406a6b9481febf9c64a3109c541567e35a49aa2e7/PyYAML-6.0.2-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5ac9328ec4831237bec75defaf839f7d4564be1e6b25ac710bd1a96321cc8317", size = 764167, upload-time = "2024-08-06T20:32:08.338Z" },
    { url = "https://files.pythonhosted.org/packages/75/e4/2c27590dfc9992f73aabbeb9241ae20220bd9452df27483b6e56d3975cc5/PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3ad2a3decf9aaba3d29c8f537ac4b243e36bef957511b4766cb0057d32b0be85", size = 762952, upload-time = "2024-08-06T20:32:14.124Z" },
    { url = "https://files.pythonhosted.org/packages/9b/97/ecc1abf4a823f5ac61941a9c00fe501b02ac3ab0e373c3857f7d4b83e2b6/PyYAML-6.0.2-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:ff3824dc5261f50c9b0dfb3be22b4567a6f938ccce4587b38952d85fd9e9afe4", size = 735301, upload-time = "2024-08-06T20:32:16.17Z" },
    { url = "https://files.pythonhosted.org/packages/45/73/0f49dacd6e82c9430e46f4a027baa4ca205e8b0a9dce1397f44edc23559d/PyYAML-6.0.2-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:797b4f722ffa07cc8d62053e4cff1486fa6dc094105d13fea7b1de7d8bf71c9e", size = 756638, upload-time = "2024-08-06T20:32:18.555Z" },
    { url = "https://files.pythonhosted.org/packages/22/5f/956f0f9fc65223a58fbc14459bf34b4cc48dec52e00535c79b8db361aabd/PyYAML-6.0.2-cp311-cp311-win32.whl", hash = "sha256:11d8f3dd2b9c1207dcaf2ee0bbbfd5991f571186ec9cc78427ba5bd32afae4b5", size = 143850, upload-time = "2024-08-06T20:32:19.889Z" },
    { url = "https://files.pythonhosted.org/packages/ed/23/8da0bbe2ab9dcdd11f4f4557ccaf95c10b9811b13ecced089d43ce59c3c8/PyYAML-6.0.2-cp311-cp311-win_amd64.whl", hash = "sha256:e10ce637b18caea04431ce14fabcf5c64a1c61ec9c56b071a4b7ca131ca52d44", size = 161980, upload-time = "2024-08-06T20:32:21.273Z" },
    { url = "https://files.pythonhosted.org/packages/86/0c/c581167fc46d6d6d7ddcfb8c843a4de25bdd27e4466938109ca68492292c/PyYAML-6.0.2-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:c70c95198c015b85feafc136515252a261a84561b7b1d51e3384e0655ddf25ab", size = 183873, upload-time = "2024-08-06T20:32:25.131Z" },
    { url = "https://files.pythonhosted.org/packages/a8/0c/38374f5bb272c051e2a69281d71cba6fdb983413e6758b84482905e29a5d/PyYAML-6.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:ce826d6ef20b1bc864f0a68340c8b3287705cae2f8b4b1d932177dcc76721725", size = 173302, upload-time = "2024-08-06T20:32:26.511Z" },
    { url = "https://files.pythonhosted.org/packages/c3/93/9916574aa8c00aa06bbac729972eb1071d002b8e158bd0e83a3b9a20a1f7/PyYAML-6.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1f71ea527786de97d1a0cc0eacd1defc0985dcf6b3f17bb77dcfc8c34bec4dc5", size = 739154, upload-time = "2024-08-06T20:32:28.363Z" },
    { url = "https://files.pythonhosted.org/packages/95/0f/b8938f1cbd09739c6da569d172531567dbcc9789e0029aa070856f123984/PyYAML-6.0.2-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:9b22676e8097e9e22e36d6b7bda33190d0d400f345f23d4065d48f4ca7ae0425", size = 766223, upload-time = "2024-08-06T20:32:30.058Z" },
    { url = "https://files.pythonhosted.org/packages/b9/2b/614b4752f2e127db5cc206abc23a8c19678e92b23c3db30fc86ab731d3bd/PyYAML-6.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:80bab7bfc629882493af4aa31a4cfa43a4c57c83813253626916b8c7ada83476", size = 767542, upload-time = "2024-08-06T20:32:31.881Z" },
    { url = "https://files.pythonhosted.org/packages/d4/00/dd137d5bcc7efea1836d6264f049359861cf548469d18da90cd8216cf05f/PyYAML-6.0.2-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:0833f8694549e586547b576dcfaba4a6b55b9e96098b36cdc7ebefe667dfed48", size = 731164, upload-time = "2024-08-06T20:32:37.083Z" },
    { url = "https://files.pythonhosted.org/packages/c9/1f/4f998c900485e5c0ef43838363ba4a9723ac0ad73a9dc42068b12aaba4e4/PyYAML-6.0.2-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:8b9c7197f7cb2738065c481a0461e50ad02f18c78cd75775628afb4d7137fb3b", size = 756611, upload-time = "2024-08-06T20:32:38.898Z" },
    { url = "https://files.pythonhosted.org/packages/df/d1/f5a275fdb252768b7a11ec63585bc38d0e87c9e05668a139fea92b80634c/PyYAML-6.0.2-cp312-cp312-win32.whl", hash = "sha256:ef6107725bd54b262d6dedcc2af448a266975032bc85ef0172c5f059da6325b4", size = 140591, upload-time = "2024-08-06T20:32:40.241Z" },
    { url = "https://files.pythonhosted.org/packages/0c/e8/4f648c598b17c3d06e8753d7d13d57542b30d56e6c2dedf9c331ae56312e/PyYAML-6.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:7e7401d0de89a9a855c839bc697c079a4af81cf878373abd7dc625847d25cbd8", size = 156338, upload-time = "2024-08-06T20:32:41.93Z" },
    { url = "https://files.pythonhosted.org/packages/ef/e3/3af305b830494fa85d95f6d95ef7fa73f2ee1cc8ef5b495c7c3269fb835f/PyYAML-6.0.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:efdca5630322a10774e8e98e1af481aad470dd62c3170801852d752aa7a783ba", size = 181309, upload-time = "2024-08-06T20:32:43.4Z" },
    { url = "https://files.pythonhosted.org/packages/45/9f/3b1c20a0b7a3200524eb0076cc027a970d320bd3a6592873c85c92a08731/PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:50187695423ffe49e2deacb8cd10510bc361faac997de9efef88badc3bb9e2d1", size = 171679, upload-time = "2024-08-06T20:32:44.801Z" },
    { url = "https://files.pythonhosted.org/packages/7c/9a/337322f27005c33bcb656c655fa78325b730324c78620e8328ae28b64d0c/PyYAML-6.0.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0ffe8360bab4910ef1b9e87fb812d8bc0a308b0d0eef8c8f44e0254ab3b07133", size = 733428, upload-time = "2024-08-06T20:32:46.432Z" },
    { url = "https://files.pythonhosted.org/packages/a3/69/864fbe19e6c18ea3cc196cbe5d392175b4cf3d5d0ac1403ec3f2d237ebb5/PyYAML-6.0.2-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:17e311b6c678207928d649faa7cb0d7b4c26a0ba73d41e99c4fff6b6c3276484", size = 763361, upload-time = "2024-08-06T20:32:51.188Z" },
    { url = "https://files.pythonhosted.org/packages/04/24/b7721e4845c2f162d26f50521b825fb061bc0a5afcf9a386840f23ea19fa/PyYAML-6.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:70b189594dbe54f75ab3a1acec5f1e3faa7e8cf2f1e08d9b561cb41b845f69d5", size = 759523, upload-time = "2024-08-06T20:32:53.019Z" },
    { url = "https://files.pythonhosted.org/packages/2b/b2/e3234f59ba06559c6ff63c4e10baea10e5e7df868092bf9ab40e5b9c56b6/PyYAML-6.0.2-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:41e4e3953a79407c794916fa277a82531dd93aad34e29c2a514c2c0c5fe971cc", size = 726660, upload-time = "2024-08-06T20:32:54.708Z" },
    { url = "https://files.pythonhosted.org/packages/fe/0f/25911a9f080464c59fab9027482f822b86bf0608957a5fcc6eaac85aa515/PyYAML-6.0.2-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:68ccc6023a3400877818152ad9a1033e3db8625d899c72eacb5a668902e4d652", size = 751597, upload-time = "2024-08-06T20:32:56.985Z" },
    { url = "https://files.pythonhosted.org/packages/14/0d/e2c3b43bbce3cf6bd97c840b46088a3031085179e596d4929729d8d68270/PyYAML-6.0.2-cp313-cp313-win32.whl", hash = "sha256:bc2fa7c6b47d6bc618dd7fb02ef6fdedb1090ec036abab80d4681424b84c1183", size = 140527, upload-time = "2024-08-06T20:33:03.001Z" },
    { url = "https://files.pythonhosted.org/packages/fa/de/02b54f42487e3d3c6efb3f89428677074ca7bf43aae402517bc7cca949f3/PyYAML-6.0.2-cp313-cp313-win_amd64.whl", hash = "sha256:8388ee1976c416731879ac16da0aff3f63b286ffdd57cdeb95f3f2e085687563", size = 156446, upload-time = "2024-08-06T20:33:04.33Z" },
]

[[package]]
name = "referencing"
version = "0.36.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "attrs" },
    { name = "rpds-py" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/2f/db/98b5c277be99dd18bfd91dd04e1b759cad18d1a338188c936e92f921c7e2/referencing-0.36.2.tar.gz", hash = "sha256:df2e89862cd09deabbdba16944cc3f10feb6b3e6f18e902f7cc25609a34775aa", size = 74744, upload-time = "2025-01-25T08:48:16.138Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c1/b1/3baf80dc6d2b7bc27a95a67752d0208e410351e3feb4eb78de5f77454d8d/referencing-0.36.2-py3-none-any.whl", hash = "sha256:e8699adbbf8b5c7de96d8ffa0eb5c158b3beafce084968e2ea8bb08c6794dcd0", size = 26775, upload-time = "2025-01-25T08:48:14.241Z" },
]

[[package]]
name = "regex"
version = "2024.11.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/8e/5f/bd69653fbfb76cf8604468d3b4ec4c403197144c7bfe0e6a5fc9e02a07cb/regex-2024.11.6.tar.gz", hash = "sha256:7ab159b063c52a0333c884e4679f8d7a85112ee3078fe3d9004b2dd875585519", size = 399494, upload-time = "2024-11-06T20:12:31.635Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/95/3c/4651f6b130c6842a8f3df82461a8950f923925db8b6961063e82744bddcc/regex-2024.11.6-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:ff590880083d60acc0433f9c3f713c51f7ac6ebb9adf889c79a261ecf541aa91", size = 482674, upload-time = "2024-11-06T20:08:57.575Z" },
    { url = "https://files.pythonhosted.org/packages/15/51/9f35d12da8434b489c7b7bffc205c474a0a9432a889457026e9bc06a297a/regex-2024.11.6-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:658f90550f38270639e83ce492f27d2c8d2cd63805c65a13a14d36ca126753f0", size = 287684, upload-time = "2024-11-06T20:08:59.787Z" },
    { url = "https://files.pythonhosted.org/packages/bd/18/b731f5510d1b8fb63c6b6d3484bfa9a59b84cc578ac8b5172970e05ae07c/regex-2024.11.6-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:164d8b7b3b4bcb2068b97428060b2a53be050085ef94eca7f240e7947f1b080e", size = 284589, upload-time = "2024-11-06T20:09:01.896Z" },
    { url = "https://files.pythonhosted.org/packages/78/a2/6dd36e16341ab95e4c6073426561b9bfdeb1a9c9b63ab1b579c2e96cb105/regex-2024.11.6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d3660c82f209655a06b587d55e723f0b813d3a7db2e32e5e7dc64ac2a9e86fde", size = 782511, upload-time = "2024-11-06T20:09:04.062Z" },
    { url = "https://files.pythonhosted.org/packages/1b/2b/323e72d5d2fd8de0d9baa443e1ed70363ed7e7b2fb526f5950c5cb99c364/regex-2024.11.6-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d22326fcdef5e08c154280b71163ced384b428343ae16a5ab2b3354aed12436e", size = 821149, upload-time = "2024-11-06T20:09:06.237Z" },
    { url = "https://files.pythonhosted.org/packages/90/30/63373b9ea468fbef8a907fd273e5c329b8c9535fee36fc8dba5fecac475d/regex-2024.11.6-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f1ac758ef6aebfc8943560194e9fd0fa18bcb34d89fd8bd2af18183afd8da3a2", size = 809707, upload-time = "2024-11-06T20:09:07.715Z" },
    { url = "https://files.pythonhosted.org/packages/f2/98/26d3830875b53071f1f0ae6d547f1d98e964dd29ad35cbf94439120bb67a/regex-2024.11.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:997d6a487ff00807ba810e0f8332c18b4eb8d29463cfb7c820dc4b6e7562d0cf", size = 781702, upload-time = "2024-11-06T20:09:10.101Z" },
    { url = "https://files.pythonhosted.org/packages/87/55/eb2a068334274db86208ab9d5599ffa63631b9f0f67ed70ea7c82a69bbc8/regex-2024.11.6-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:02a02d2bb04fec86ad61f3ea7f49c015a0681bf76abb9857f945d26159d2968c", size = 771976, upload-time = "2024-11-06T20:09:11.566Z" },
    { url = "https://files.pythonhosted.org/packages/74/c0/be707bcfe98254d8f9d2cff55d216e946f4ea48ad2fd8cf1428f8c5332ba/regex-2024.11.6-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:f02f93b92358ee3f78660e43b4b0091229260c5d5c408d17d60bf26b6c900e86", size = 697397, upload-time = "2024-11-06T20:09:13.119Z" },
    { url = "https://files.pythonhosted.org/packages/49/dc/bb45572ceb49e0f6509f7596e4ba7031f6819ecb26bc7610979af5a77f45/regex-2024.11.6-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:06eb1be98df10e81ebaded73fcd51989dcf534e3c753466e4b60c4697a003b67", size = 768726, upload-time = "2024-11-06T20:09:14.85Z" },
    { url = "https://files.pythonhosted.org/packages/5a/db/f43fd75dc4c0c2d96d0881967897926942e935d700863666f3c844a72ce6/regex-2024.11.6-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:040df6fe1a5504eb0f04f048e6d09cd7c7110fef851d7c567a6b6e09942feb7d", size = 775098, upload-time = "2024-11-06T20:09:16.504Z" },
    { url = "https://files.pythonhosted.org/packages/99/d7/f94154db29ab5a89d69ff893159b19ada89e76b915c1293e98603d39838c/regex-2024.11.6-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:fdabbfc59f2c6edba2a6622c647b716e34e8e3867e0ab975412c5c2f79b82da2", size = 839325, upload-time = "2024-11-06T20:09:18.698Z" },
    { url = "https://files.pythonhosted.org/packages/f7/17/3cbfab1f23356fbbf07708220ab438a7efa1e0f34195bf857433f79f1788/regex-2024.11.6-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:8447d2d39b5abe381419319f942de20b7ecd60ce86f16a23b0698f22e1b70008", size = 843277, upload-time = "2024-11-06T20:09:21.725Z" },
    { url = "https://files.pythonhosted.org/packages/7e/f2/48b393b51900456155de3ad001900f94298965e1cad1c772b87f9cfea011/regex-2024.11.6-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:da8f5fc57d1933de22a9e23eec290a0d8a5927a5370d24bda9a6abe50683fe62", size = 773197, upload-time = "2024-11-06T20:09:24.092Z" },
    { url = "https://files.pythonhosted.org/packages/45/3f/ef9589aba93e084cd3f8471fded352826dcae8489b650d0b9b27bc5bba8a/regex-2024.11.6-cp310-cp310-win32.whl", hash = "sha256:b489578720afb782f6ccf2840920f3a32e31ba28a4b162e13900c3e6bd3f930e", size = 261714, upload-time = "2024-11-06T20:09:26.36Z" },
    { url = "https://files.pythonhosted.org/packages/42/7e/5f1b92c8468290c465fd50c5318da64319133231415a8aa6ea5ab995a815/regex-2024.11.6-cp310-cp310-win_amd64.whl", hash = "sha256:5071b2093e793357c9d8b2929dfc13ac5f0a6c650559503bb81189d0a3814519", size = 274042, upload-time = "2024-11-06T20:09:28.762Z" },
    { url = "https://files.pythonhosted.org/packages/58/58/7e4d9493a66c88a7da6d205768119f51af0f684fe7be7bac8328e217a52c/regex-2024.11.6-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:5478c6962ad548b54a591778e93cd7c456a7a29f8eca9c49e4f9a806dcc5d638", size = 482669, upload-time = "2024-11-06T20:09:31.064Z" },
    { url = "https://files.pythonhosted.org/packages/34/4c/8f8e631fcdc2ff978609eaeef1d6994bf2f028b59d9ac67640ed051f1218/regex-2024.11.6-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:2c89a8cc122b25ce6945f0423dc1352cb9593c68abd19223eebbd4e56612c5b7", size = 287684, upload-time = "2024-11-06T20:09:32.915Z" },
    { url = "https://files.pythonhosted.org/packages/c5/1b/f0e4d13e6adf866ce9b069e191f303a30ab1277e037037a365c3aad5cc9c/regex-2024.11.6-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:94d87b689cdd831934fa3ce16cc15cd65748e6d689f5d2b8f4f4df2065c9fa20", size = 284589, upload-time = "2024-11-06T20:09:35.504Z" },
    { url = "https://files.pythonhosted.org/packages/25/4d/ab21047f446693887f25510887e6820b93f791992994f6498b0318904d4a/regex-2024.11.6-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1062b39a0a2b75a9c694f7a08e7183a80c63c0d62b301418ffd9c35f55aaa114", size = 792121, upload-time = "2024-11-06T20:09:37.701Z" },
    { url = "https://files.pythonhosted.org/packages/45/ee/c867e15cd894985cb32b731d89576c41a4642a57850c162490ea34b78c3b/regex-2024.11.6-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:167ed4852351d8a750da48712c3930b031f6efdaa0f22fa1933716bfcd6bf4a3", size = 831275, upload-time = "2024-11-06T20:09:40.371Z" },
    { url = "https://files.pythonhosted.org/packages/b3/12/b0f480726cf1c60f6536fa5e1c95275a77624f3ac8fdccf79e6727499e28/regex-2024.11.6-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2d548dafee61f06ebdb584080621f3e0c23fff312f0de1afc776e2a2ba99a74f", size = 818257, upload-time = "2024-11-06T20:09:43.059Z" },
    { url = "https://files.pythonhosted.org/packages/bf/ce/0d0e61429f603bac433910d99ef1a02ce45a8967ffbe3cbee48599e62d88/regex-2024.11.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f2a19f302cd1ce5dd01a9099aaa19cae6173306d1302a43b627f62e21cf18ac0", size = 792727, upload-time = "2024-11-06T20:09:48.19Z" },
    { url = "https://files.pythonhosted.org/packages/e4/c1/243c83c53d4a419c1556f43777ccb552bccdf79d08fda3980e4e77dd9137/regex-2024.11.6-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:bec9931dfb61ddd8ef2ebc05646293812cb6b16b60cf7c9511a832b6f1854b55", size = 780667, upload-time = "2024-11-06T20:09:49.828Z" },
    { url = "https://files.pythonhosted.org/packages/c5/f4/75eb0dd4ce4b37f04928987f1d22547ddaf6c4bae697623c1b05da67a8aa/regex-2024.11.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:9714398225f299aa85267fd222f7142fcb5c769e73d7733344efc46f2ef5cf89", size = 776963, upload-time = "2024-11-06T20:09:51.819Z" },
    { url = "https://files.pythonhosted.org/packages/16/5d/95c568574e630e141a69ff8a254c2f188b4398e813c40d49228c9bbd9875/regex-2024.11.6-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:202eb32e89f60fc147a41e55cb086db2a3f8cb82f9a9a88440dcfc5d37faae8d", size = 784700, upload-time = "2024-11-06T20:09:53.982Z" },
    { url = "https://files.pythonhosted.org/packages/8e/b5/f8495c7917f15cc6fee1e7f395e324ec3e00ab3c665a7dc9d27562fd5290/regex-2024.11.6-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:4181b814e56078e9b00427ca358ec44333765f5ca1b45597ec7446d3a1ef6e34", size = 848592, upload-time = "2024-11-06T20:09:56.222Z" },
    { url = "https://files.pythonhosted.org/packages/1c/80/6dd7118e8cb212c3c60b191b932dc57db93fb2e36fb9e0e92f72a5909af9/regex-2024.11.6-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:068376da5a7e4da51968ce4c122a7cd31afaaec4fccc7856c92f63876e57b51d", size = 852929, upload-time = "2024-11-06T20:09:58.642Z" },
    { url = "https://files.pythonhosted.org/packages/11/9b/5a05d2040297d2d254baf95eeeb6df83554e5e1df03bc1a6687fc4ba1f66/regex-2024.11.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:ac10f2c4184420d881a3475fb2c6f4d95d53a8d50209a2500723d831036f7c45", size = 781213, upload-time = "2024-11-06T20:10:00.867Z" },
    { url = "https://files.pythonhosted.org/packages/26/b7/b14e2440156ab39e0177506c08c18accaf2b8932e39fb092074de733d868/regex-2024.11.6-cp311-cp311-win32.whl", hash = "sha256:c36f9b6f5f8649bb251a5f3f66564438977b7ef8386a52460ae77e6070d309d9", size = 261734, upload-time = "2024-11-06T20:10:03.361Z" },
    { url = "https://files.pythonhosted.org/packages/80/32/763a6cc01d21fb3819227a1cc3f60fd251c13c37c27a73b8ff4315433a8e/regex-2024.11.6-cp311-cp311-win_amd64.whl", hash = "sha256:02e28184be537f0e75c1f9b2f8847dc51e08e6e171c6bde130b2687e0c33cf60", size = 274052, upload-time = "2024-11-06T20:10:05.179Z" },
    { url = "https://files.pythonhosted.org/packages/ba/30/9a87ce8336b172cc232a0db89a3af97929d06c11ceaa19d97d84fa90a8f8/regex-2024.11.6-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:52fb28f528778f184f870b7cf8f225f5eef0a8f6e3778529bdd40c7b3920796a", size = 483781, upload-time = "2024-11-06T20:10:07.07Z" },
    { url = "https://files.pythonhosted.org/packages/01/e8/00008ad4ff4be8b1844786ba6636035f7ef926db5686e4c0f98093612add/regex-2024.11.6-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:fdd6028445d2460f33136c55eeb1f601ab06d74cb3347132e1c24250187500d9", size = 288455, upload-time = "2024-11-06T20:10:09.117Z" },
    { url = "https://files.pythonhosted.org/packages/60/85/cebcc0aff603ea0a201667b203f13ba75d9fc8668fab917ac5b2de3967bc/regex-2024.11.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:805e6b60c54bf766b251e94526ebad60b7de0c70f70a4e6210ee2891acb70bf2", size = 284759, upload-time = "2024-11-06T20:10:11.155Z" },
    { url = "https://files.pythonhosted.org/packages/94/2b/701a4b0585cb05472a4da28ee28fdfe155f3638f5e1ec92306d924e5faf0/regex-2024.11.6-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b85c2530be953a890eaffde05485238f07029600e8f098cdf1848d414a8b45e4", size = 794976, upload-time = "2024-11-06T20:10:13.24Z" },
    { url = "https://files.pythonhosted.org/packages/4b/bf/fa87e563bf5fee75db8915f7352e1887b1249126a1be4813837f5dbec965/regex-2024.11.6-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:bb26437975da7dc36b7efad18aa9dd4ea569d2357ae6b783bf1118dabd9ea577", size = 833077, upload-time = "2024-11-06T20:10:15.37Z" },
    { url = "https://files.pythonhosted.org/packages/a1/56/7295e6bad94b047f4d0834e4779491b81216583c00c288252ef625c01d23/regex-2024.11.6-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:abfa5080c374a76a251ba60683242bc17eeb2c9818d0d30117b4486be10c59d3", size = 823160, upload-time = "2024-11-06T20:10:19.027Z" },
    { url = "https://files.pythonhosted.org/packages/fb/13/e3b075031a738c9598c51cfbc4c7879e26729c53aa9cca59211c44235314/regex-2024.11.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:70b7fa6606c2881c1db9479b0eaa11ed5dfa11c8d60a474ff0e095099f39d98e", size = 796896, upload-time = "2024-11-06T20:10:21.85Z" },
    { url = "https://files.pythonhosted.org/packages/24/56/0b3f1b66d592be6efec23a795b37732682520b47c53da5a32c33ed7d84e3/regex-2024.11.6-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:0c32f75920cf99fe6b6c539c399a4a128452eaf1af27f39bce8909c9a3fd8cbe", size = 783997, upload-time = "2024-11-06T20:10:24.329Z" },
    { url = "https://files.pythonhosted.org/packages/f9/a1/eb378dada8b91c0e4c5f08ffb56f25fcae47bf52ad18f9b2f33b83e6d498/regex-2024.11.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:982e6d21414e78e1f51cf595d7f321dcd14de1f2881c5dc6a6e23bbbbd68435e", size = 781725, upload-time = "2024-11-06T20:10:28.067Z" },
    { url = "https://files.pythonhosted.org/packages/83/f2/033e7dec0cfd6dda93390089864732a3409246ffe8b042e9554afa9bff4e/regex-2024.11.6-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:a7c2155f790e2fb448faed6dd241386719802296ec588a8b9051c1f5c481bc29", size = 789481, upload-time = "2024-11-06T20:10:31.612Z" },
    { url = "https://files.pythonhosted.org/packages/83/23/15d4552ea28990a74e7696780c438aadd73a20318c47e527b47a4a5a596d/regex-2024.11.6-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:149f5008d286636e48cd0b1dd65018548944e495b0265b45e1bffecce1ef7f39", size = 852896, upload-time = "2024-11-06T20:10:34.054Z" },
    { url = "https://files.pythonhosted.org/packages/e3/39/ed4416bc90deedbfdada2568b2cb0bc1fdb98efe11f5378d9892b2a88f8f/regex-2024.11.6-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:e5364a4502efca094731680e80009632ad6624084aff9a23ce8c8c6820de3e51", size = 860138, upload-time = "2024-11-06T20:10:36.142Z" },
    { url = "https://files.pythonhosted.org/packages/93/2d/dd56bb76bd8e95bbce684326302f287455b56242a4f9c61f1bc76e28360e/regex-2024.11.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:0a86e7eeca091c09e021db8eb72d54751e527fa47b8d5787caf96d9831bd02ad", size = 787692, upload-time = "2024-11-06T20:10:38.394Z" },
    { url = "https://files.pythonhosted.org/packages/0b/55/31877a249ab7a5156758246b9c59539abbeba22461b7d8adc9e8475ff73e/regex-2024.11.6-cp312-cp312-win32.whl", hash = "sha256:32f9a4c643baad4efa81d549c2aadefaeba12249b2adc5af541759237eee1c54", size = 262135, upload-time = "2024-11-06T20:10:40.367Z" },
    { url = "https://files.pythonhosted.org/packages/38/ec/ad2d7de49a600cdb8dd78434a1aeffe28b9d6fc42eb36afab4a27ad23384/regex-2024.11.6-cp312-cp312-win_amd64.whl", hash = "sha256:a93c194e2df18f7d264092dc8539b8ffb86b45b899ab976aa15d48214138e81b", size = 273567, upload-time = "2024-11-06T20:10:43.467Z" },
    { url = "https://files.pythonhosted.org/packages/90/73/bcb0e36614601016552fa9344544a3a2ae1809dc1401b100eab02e772e1f/regex-2024.11.6-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:a6ba92c0bcdf96cbf43a12c717eae4bc98325ca3730f6b130ffa2e3c3c723d84", size = 483525, upload-time = "2024-11-06T20:10:45.19Z" },
    { url = "https://files.pythonhosted.org/packages/0f/3f/f1a082a46b31e25291d830b369b6b0c5576a6f7fb89d3053a354c24b8a83/regex-2024.11.6-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:525eab0b789891ac3be914d36893bdf972d483fe66551f79d3e27146191a37d4", size = 288324, upload-time = "2024-11-06T20:10:47.177Z" },
    { url = "https://files.pythonhosted.org/packages/09/c9/4e68181a4a652fb3ef5099e077faf4fd2a694ea6e0f806a7737aff9e758a/regex-2024.11.6-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:086a27a0b4ca227941700e0b31425e7a28ef1ae8e5e05a33826e17e47fbfdba0", size = 284617, upload-time = "2024-11-06T20:10:49.312Z" },
    { url = "https://files.pythonhosted.org/packages/fc/fd/37868b75eaf63843165f1d2122ca6cb94bfc0271e4428cf58c0616786dce/regex-2024.11.6-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:bde01f35767c4a7899b7eb6e823b125a64de314a8ee9791367c9a34d56af18d0", size = 795023, upload-time = "2024-11-06T20:10:51.102Z" },
    { url = "https://files.pythonhosted.org/packages/c4/7c/d4cd9c528502a3dedb5c13c146e7a7a539a3853dc20209c8e75d9ba9d1b2/regex-2024.11.6-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:b583904576650166b3d920d2bcce13971f6f9e9a396c673187f49811b2769dc7", size = 833072, upload-time = "2024-11-06T20:10:52.926Z" },
    { url = "https://files.pythonhosted.org/packages/4f/db/46f563a08f969159c5a0f0e722260568425363bea43bb7ae370becb66a67/regex-2024.11.6-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:1c4de13f06a0d54fa0d5ab1b7138bfa0d883220965a29616e3ea61b35d5f5fc7", size = 823130, upload-time = "2024-11-06T20:10:54.828Z" },
    { url = "https://files.pythonhosted.org/packages/db/60/1eeca2074f5b87df394fccaa432ae3fc06c9c9bfa97c5051aed70e6e00c2/regex-2024.11.6-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3cde6e9f2580eb1665965ce9bf17ff4952f34f5b126beb509fee8f4e994f143c", size = 796857, upload-time = "2024-11-06T20:10:56.634Z" },
    { url = "https://files.pythonhosted.org/packages/10/db/ac718a08fcee981554d2f7bb8402f1faa7e868c1345c16ab1ebec54b0d7b/regex-2024.11.6-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:0d7f453dca13f40a02b79636a339c5b62b670141e63efd511d3f8f73fba162b3", size = 784006, upload-time = "2024-11-06T20:10:59.369Z" },
    { url = "https://files.pythonhosted.org/packages/c2/41/7da3fe70216cea93144bf12da2b87367590bcf07db97604edeea55dac9ad/regex-2024.11.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:59dfe1ed21aea057a65c6b586afd2a945de04fc7db3de0a6e3ed5397ad491b07", size = 781650, upload-time = "2024-11-06T20:11:02.042Z" },
    { url = "https://files.pythonhosted.org/packages/a7/d5/880921ee4eec393a4752e6ab9f0fe28009435417c3102fc413f3fe81c4e5/regex-2024.11.6-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:b97c1e0bd37c5cd7902e65f410779d39eeda155800b65fc4d04cc432efa9bc6e", size = 789545, upload-time = "2024-11-06T20:11:03.933Z" },
    { url = "https://files.pythonhosted.org/packages/dc/96/53770115e507081122beca8899ab7f5ae28ae790bfcc82b5e38976df6a77/regex-2024.11.6-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:f9d1e379028e0fc2ae3654bac3cbbef81bf3fd571272a42d56c24007979bafb6", size = 853045, upload-time = "2024-11-06T20:11:06.497Z" },
    { url = "https://files.pythonhosted.org/packages/31/d3/1372add5251cc2d44b451bd94f43b2ec78e15a6e82bff6a290ef9fd8f00a/regex-2024.11.6-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:13291b39131e2d002a7940fb176e120bec5145f3aeb7621be6534e46251912c4", size = 860182, upload-time = "2024-11-06T20:11:09.06Z" },
    { url = "https://files.pythonhosted.org/packages/ed/e3/c446a64984ea9f69982ba1a69d4658d5014bc7a0ea468a07e1a1265db6e2/regex-2024.11.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4f51f88c126370dcec4908576c5a627220da6c09d0bff31cfa89f2523843316d", size = 787733, upload-time = "2024-11-06T20:11:11.256Z" },
    { url = "https://files.pythonhosted.org/packages/2b/f1/e40c8373e3480e4f29f2692bd21b3e05f296d3afebc7e5dcf21b9756ca1c/regex-2024.11.6-cp313-cp313-win32.whl", hash = "sha256:63b13cfd72e9601125027202cad74995ab26921d8cd935c25f09c630436348ff", size = 262122, upload-time = "2024-11-06T20:11:13.161Z" },
    { url = "https://files.pythonhosted.org/packages/45/94/bc295babb3062a731f52621cdc992d123111282e291abaf23faa413443ea/regex-2024.11.6-cp313-cp313-win_amd64.whl", hash = "sha256:2b3361af3198667e99927da8b84c1b010752fa4b1115ee30beaa332cabc3ef1a", size = 273545, upload-time = "2024-11-06T20:11:15Z" },
]

[[package]]
name = "requests"
version = "2.32.4"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/e1/0a/929373653770d8a0d7ea76c37de6e41f11eb07559b103b1c02cafb3f7cf8/requests-2.32.4.tar.gz", hash = "sha256:27d0316682c8a29834d3264820024b62a36942083d52caf2f14c0591336d3422", size = 135258, upload-time = "2025-06-09T16:43:07.34Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7c/e4/56027c4a6b4ae70ca9de302488c5ca95ad4a39e190093d6c1a8ace08341b/requests-2.32.4-py3-none-any.whl", hash = "sha256:27babd3cda2a6d50b30443204ee89830707d396671944c998b5975b031ac2b2c", size = 64847, upload-time = "2025-06-09T16:43:05.728Z" },
]

[[package]]
name = "rich"
version = "14.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a1/53/830aa4c3066a8ab0ae9a9955976fb770fe9c6102117c8ec4ab3ea62d89e8/rich-14.0.0.tar.gz", hash = "sha256:82f1bc23a6a21ebca4ae0c45af9bdbc492ed20231dcb63f297d6d1021a9d5725", size = 224078, upload-time = "2025-03-30T14:15:14.23Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0d/9b/63f4c7ebc259242c89b3acafdb37b41d1185c07ff0011164674e9076b491/rich-14.0.0-py3-none-any.whl", hash = "sha256:1c9491e1951aac09caffd42f448ee3d04e58923ffe14993f6e83068dc395d7e0", size = 243229, upload-time = "2025-03-30T14:15:12.283Z" },
]

[[package]]
name = "rpds-py"
version = "0.25.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/8c/a6/60184b7fc00dd3ca80ac635dd5b8577d444c57e8e8742cecabfacb829921/rpds_py-0.25.1.tar.gz", hash = "sha256:8960b6dac09b62dac26e75d7e2c4a22efb835d827a7278c34f72b2b84fa160e3", size = 27304, upload-time = "2025-05-21T12:46:12.502Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cb/09/e1158988e50905b7f8306487a576b52d32aa9a87f79f7ab24ee8db8b6c05/rpds_py-0.25.1-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:f4ad628b5174d5315761b67f212774a32f5bad5e61396d38108bd801c0a8f5d9", size = 373140, upload-time = "2025-05-21T12:42:38.834Z" },
    { url = "https://files.pythonhosted.org/packages/e0/4b/a284321fb3c45c02fc74187171504702b2934bfe16abab89713eedfe672e/rpds_py-0.25.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8c742af695f7525e559c16f1562cf2323db0e3f0fbdcabdf6865b095256b2d40", size = 358860, upload-time = "2025-05-21T12:42:41.394Z" },
    { url = "https://files.pythonhosted.org/packages/4e/46/8ac9811150c75edeae9fc6fa0e70376c19bc80f8e1f7716981433905912b/rpds_py-0.25.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:605ffe7769e24b1800b4d024d24034405d9404f0bc2f55b6db3362cd34145a6f", size = 386179, upload-time = "2025-05-21T12:42:43.213Z" },
    { url = "https://files.pythonhosted.org/packages/f3/ec/87eb42d83e859bce91dcf763eb9f2ab117142a49c9c3d17285440edb5b69/rpds_py-0.25.1-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ccc6f3ddef93243538be76f8e47045b4aad7a66a212cd3a0f23e34469473d36b", size = 400282, upload-time = "2025-05-21T12:42:44.92Z" },
    { url = "https://files.pythonhosted.org/packages/68/c8/2a38e0707d7919c8c78e1d582ab15cf1255b380bcb086ca265b73ed6db23/rpds_py-0.25.1-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f70316f760174ca04492b5ab01be631a8ae30cadab1d1081035136ba12738cfa", size = 521824, upload-time = "2025-05-21T12:42:46.856Z" },
    { url = "https://files.pythonhosted.org/packages/5e/2c/6a92790243569784dde84d144bfd12bd45102f4a1c897d76375076d730ab/rpds_py-0.25.1-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e1dafef8df605fdb46edcc0bf1573dea0d6d7b01ba87f85cd04dc855b2b4479e", size = 411644, upload-time = "2025-05-21T12:42:48.838Z" },
    { url = "https://files.pythonhosted.org/packages/eb/76/66b523ffc84cf47db56efe13ae7cf368dee2bacdec9d89b9baca5e2e6301/rpds_py-0.25.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0701942049095741a8aeb298a31b203e735d1c61f4423511d2b1a41dcd8a16da", size = 386955, upload-time = "2025-05-21T12:42:50.835Z" },
    { url = "https://files.pythonhosted.org/packages/b6/b9/a362d7522feaa24dc2b79847c6175daa1c642817f4a19dcd5c91d3e2c316/rpds_py-0.25.1-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:e87798852ae0b37c88babb7f7bbbb3e3fecc562a1c340195b44c7e24d403e380", size = 421039, upload-time = "2025-05-21T12:42:52.348Z" },
    { url = "https://files.pythonhosted.org/packages/0f/c4/b5b6f70b4d719b6584716889fd3413102acf9729540ee76708d56a76fa97/rpds_py-0.25.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:3bcce0edc1488906c2d4c75c94c70a0417e83920dd4c88fec1078c94843a6ce9", size = 563290, upload-time = "2025-05-21T12:42:54.404Z" },
    { url = "https://files.pythonhosted.org/packages/87/a3/2e6e816615c12a8f8662c9d8583a12eb54c52557521ef218cbe3095a8afa/rpds_py-0.25.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:e2f6a2347d3440ae789505693a02836383426249d5293541cd712e07e7aecf54", size = 592089, upload-time = "2025-05-21T12:42:55.976Z" },
    { url = "https://files.pythonhosted.org/packages/c0/08/9b8e1050e36ce266135994e2c7ec06e1841f1c64da739daeb8afe9cb77a4/rpds_py-0.25.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:4fd52d3455a0aa997734f3835cbc4c9f32571345143960e7d7ebfe7b5fbfa3b2", size = 558400, upload-time = "2025-05-21T12:42:58.032Z" },
    { url = "https://files.pythonhosted.org/packages/f2/df/b40b8215560b8584baccd839ff5c1056f3c57120d79ac41bd26df196da7e/rpds_py-0.25.1-cp310-cp310-win32.whl", hash = "sha256:3f0b1798cae2bbbc9b9db44ee068c556d4737911ad53a4e5093d09d04b3bbc24", size = 219741, upload-time = "2025-05-21T12:42:59.479Z" },
    { url = "https://files.pythonhosted.org/packages/10/99/e4c58be18cf5d8b40b8acb4122bc895486230b08f978831b16a3916bd24d/rpds_py-0.25.1-cp310-cp310-win_amd64.whl", hash = "sha256:3ebd879ab996537fc510a2be58c59915b5dd63bccb06d1ef514fee787e05984a", size = 231553, upload-time = "2025-05-21T12:43:01.425Z" },
    { url = "https://files.pythonhosted.org/packages/95/e1/df13fe3ddbbea43567e07437f097863b20c99318ae1f58a0fe389f763738/rpds_py-0.25.1-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:5f048bbf18b1f9120685c6d6bb70cc1a52c8cc11bdd04e643d28d3be0baf666d", size = 373341, upload-time = "2025-05-21T12:43:02.978Z" },
    { url = "https://files.pythonhosted.org/packages/7a/58/deef4d30fcbcbfef3b6d82d17c64490d5c94585a2310544ce8e2d3024f83/rpds_py-0.25.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4fbb0dbba559959fcb5d0735a0f87cdbca9e95dac87982e9b95c0f8f7ad10255", size = 359111, upload-time = "2025-05-21T12:43:05.128Z" },
    { url = "https://files.pythonhosted.org/packages/bb/7e/39f1f4431b03e96ebaf159e29a0f82a77259d8f38b2dd474721eb3a8ac9b/rpds_py-0.25.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d4ca54b9cf9d80b4016a67a0193ebe0bcf29f6b0a96f09db942087e294d3d4c2", size = 386112, upload-time = "2025-05-21T12:43:07.13Z" },
    { url = "https://files.pythonhosted.org/packages/db/e7/847068a48d63aec2ae695a1646089620b3b03f8ccf9f02c122ebaf778f3c/rpds_py-0.25.1-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:1ee3e26eb83d39b886d2cb6e06ea701bba82ef30a0de044d34626ede51ec98b0", size = 400362, upload-time = "2025-05-21T12:43:08.693Z" },
    { url = "https://files.pythonhosted.org/packages/3b/3d/9441d5db4343d0cee759a7ab4d67420a476cebb032081763de934719727b/rpds_py-0.25.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:89706d0683c73a26f76a5315d893c051324d771196ae8b13e6ffa1ffaf5e574f", size = 522214, upload-time = "2025-05-21T12:43:10.694Z" },
    { url = "https://files.pythonhosted.org/packages/a2/ec/2cc5b30d95f9f1a432c79c7a2f65d85e52812a8f6cbf8768724571710786/rpds_py-0.25.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:c2013ee878c76269c7b557a9a9c042335d732e89d482606990b70a839635feb7", size = 411491, upload-time = "2025-05-21T12:43:12.739Z" },
    { url = "https://files.pythonhosted.org/packages/dc/6c/44695c1f035077a017dd472b6a3253553780837af2fac9b6ac25f6a5cb4d/rpds_py-0.25.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:45e484db65e5380804afbec784522de84fa95e6bb92ef1bd3325d33d13efaebd", size = 386978, upload-time = "2025-05-21T12:43:14.25Z" },
    { url = "https://files.pythonhosted.org/packages/b1/74/b4357090bb1096db5392157b4e7ed8bb2417dc7799200fcbaee633a032c9/rpds_py-0.25.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:48d64155d02127c249695abb87d39f0faf410733428d499867606be138161d65", size = 420662, upload-time = "2025-05-21T12:43:15.8Z" },
    { url = "https://files.pythonhosted.org/packages/26/dd/8cadbebf47b96e59dfe8b35868e5c38a42272699324e95ed522da09d3a40/rpds_py-0.25.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:048893e902132fd6548a2e661fb38bf4896a89eea95ac5816cf443524a85556f", size = 563385, upload-time = "2025-05-21T12:43:17.78Z" },
    { url = "https://files.pythonhosted.org/packages/c3/ea/92960bb7f0e7a57a5ab233662f12152085c7dc0d5468534c65991a3d48c9/rpds_py-0.25.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:0317177b1e8691ab5879f4f33f4b6dc55ad3b344399e23df2e499de7b10a548d", size = 592047, upload-time = "2025-05-21T12:43:19.457Z" },
    { url = "https://files.pythonhosted.org/packages/61/ad/71aabc93df0d05dabcb4b0c749277881f8e74548582d96aa1bf24379493a/rpds_py-0.25.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:bffcf57826d77a4151962bf1701374e0fc87f536e56ec46f1abdd6a903354042", size = 557863, upload-time = "2025-05-21T12:43:21.69Z" },
    { url = "https://files.pythonhosted.org/packages/93/0f/89df0067c41f122b90b76f3660028a466eb287cbe38efec3ea70e637ca78/rpds_py-0.25.1-cp311-cp311-win32.whl", hash = "sha256:cda776f1967cb304816173b30994faaf2fd5bcb37e73118a47964a02c348e1bc", size = 219627, upload-time = "2025-05-21T12:43:23.311Z" },
    { url = "https://files.pythonhosted.org/packages/7c/8d/93b1a4c1baa903d0229374d9e7aa3466d751f1d65e268c52e6039c6e338e/rpds_py-0.25.1-cp311-cp311-win_amd64.whl", hash = "sha256:dc3c1ff0abc91444cd20ec643d0f805df9a3661fcacf9c95000329f3ddf268a4", size = 231603, upload-time = "2025-05-21T12:43:25.145Z" },
    { url = "https://files.pythonhosted.org/packages/cb/11/392605e5247bead2f23e6888e77229fbd714ac241ebbebb39a1e822c8815/rpds_py-0.25.1-cp311-cp311-win_arm64.whl", hash = "sha256:5a3ddb74b0985c4387719fc536faced33cadf2172769540c62e2a94b7b9be1c4", size = 223967, upload-time = "2025-05-21T12:43:26.566Z" },
    { url = "https://files.pythonhosted.org/packages/7f/81/28ab0408391b1dc57393653b6a0cf2014cc282cc2909e4615e63e58262be/rpds_py-0.25.1-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:b5ffe453cde61f73fea9430223c81d29e2fbf412a6073951102146c84e19e34c", size = 364647, upload-time = "2025-05-21T12:43:28.559Z" },
    { url = "https://files.pythonhosted.org/packages/2c/9a/7797f04cad0d5e56310e1238434f71fc6939d0bc517192a18bb99a72a95f/rpds_py-0.25.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:115874ae5e2fdcfc16b2aedc95b5eef4aebe91b28e7e21951eda8a5dc0d3461b", size = 350454, upload-time = "2025-05-21T12:43:30.615Z" },
    { url = "https://files.pythonhosted.org/packages/69/3c/93d2ef941b04898011e5d6eaa56a1acf46a3b4c9f4b3ad1bbcbafa0bee1f/rpds_py-0.25.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a714bf6e5e81b0e570d01f56e0c89c6375101b8463999ead3a93a5d2a4af91fa", size = 389665, upload-time = "2025-05-21T12:43:32.629Z" },
    { url = "https://files.pythonhosted.org/packages/c1/57/ad0e31e928751dde8903a11102559628d24173428a0f85e25e187defb2c1/rpds_py-0.25.1-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:35634369325906bcd01577da4c19e3b9541a15e99f31e91a02d010816b49bfda", size = 403873, upload-time = "2025-05-21T12:43:34.576Z" },
    { url = "https://files.pythonhosted.org/packages/16/ad/c0c652fa9bba778b4f54980a02962748479dc09632e1fd34e5282cf2556c/rpds_py-0.25.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d4cb2b3ddc16710548801c6fcc0cfcdeeff9dafbc983f77265877793f2660309", size = 525866, upload-time = "2025-05-21T12:43:36.123Z" },
    { url = "https://files.pythonhosted.org/packages/2a/39/3e1839bc527e6fcf48d5fec4770070f872cdee6c6fbc9b259932f4e88a38/rpds_py-0.25.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:9ceca1cf097ed77e1a51f1dbc8d174d10cb5931c188a4505ff9f3e119dfe519b", size = 416886, upload-time = "2025-05-21T12:43:38.034Z" },
    { url = "https://files.pythonhosted.org/packages/7a/95/dd6b91cd4560da41df9d7030a038298a67d24f8ca38e150562644c829c48/rpds_py-0.25.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2c2cd1a4b0c2b8c5e31ffff50d09f39906fe351389ba143c195566056c13a7ea", size = 390666, upload-time = "2025-05-21T12:43:40.065Z" },
    { url = "https://files.pythonhosted.org/packages/64/48/1be88a820e7494ce0a15c2d390ccb7c52212370badabf128e6a7bb4cb802/rpds_py-0.25.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:1de336a4b164c9188cb23f3703adb74a7623ab32d20090d0e9bf499a2203ad65", size = 425109, upload-time = "2025-05-21T12:43:42.263Z" },
    { url = "https://files.pythonhosted.org/packages/cf/07/3e2a17927ef6d7720b9949ec1b37d1e963b829ad0387f7af18d923d5cfa5/rpds_py-0.25.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:9fca84a15333e925dd59ce01da0ffe2ffe0d6e5d29a9eeba2148916d1824948c", size = 567244, upload-time = "2025-05-21T12:43:43.846Z" },
    { url = "https://files.pythonhosted.org/packages/d2/e5/76cf010998deccc4f95305d827847e2eae9c568099c06b405cf96384762b/rpds_py-0.25.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:88ec04afe0c59fa64e2f6ea0dd9657e04fc83e38de90f6de201954b4d4eb59bd", size = 596023, upload-time = "2025-05-21T12:43:45.932Z" },
    { url = "https://files.pythonhosted.org/packages/52/9a/df55efd84403736ba37a5a6377b70aad0fd1cb469a9109ee8a1e21299a1c/rpds_py-0.25.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:a8bd2f19e312ce3e1d2c635618e8a8d8132892bb746a7cf74780a489f0f6cdcb", size = 561634, upload-time = "2025-05-21T12:43:48.263Z" },
    { url = "https://files.pythonhosted.org/packages/ab/aa/dc3620dd8db84454aaf9374bd318f1aa02578bba5e567f5bf6b79492aca4/rpds_py-0.25.1-cp312-cp312-win32.whl", hash = "sha256:e5e2f7280d8d0d3ef06f3ec1b4fd598d386cc6f0721e54f09109a8132182fbfe", size = 222713, upload-time = "2025-05-21T12:43:49.897Z" },
    { url = "https://files.pythonhosted.org/packages/a3/7f/7cef485269a50ed5b4e9bae145f512d2a111ca638ae70cc101f661b4defd/rpds_py-0.25.1-cp312-cp312-win_amd64.whl", hash = "sha256:db58483f71c5db67d643857404da360dce3573031586034b7d59f245144cc192", size = 235280, upload-time = "2025-05-21T12:43:51.893Z" },
    { url = "https://files.pythonhosted.org/packages/99/f2/c2d64f6564f32af913bf5f3f7ae41c7c263c5ae4c4e8f1a17af8af66cd46/rpds_py-0.25.1-cp312-cp312-win_arm64.whl", hash = "sha256:6d50841c425d16faf3206ddbba44c21aa3310a0cebc3c1cdfc3e3f4f9f6f5728", size = 225399, upload-time = "2025-05-21T12:43:53.351Z" },
    { url = "https://files.pythonhosted.org/packages/2b/da/323848a2b62abe6a0fec16ebe199dc6889c5d0a332458da8985b2980dffe/rpds_py-0.25.1-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:659d87430a8c8c704d52d094f5ba6fa72ef13b4d385b7e542a08fc240cb4a559", size = 364498, upload-time = "2025-05-21T12:43:54.841Z" },
    { url = "https://files.pythonhosted.org/packages/1f/b4/4d3820f731c80fd0cd823b3e95b9963fec681ae45ba35b5281a42382c67d/rpds_py-0.25.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:68f6f060f0bbdfb0245267da014d3a6da9be127fe3e8cc4a68c6f833f8a23bb1", size = 350083, upload-time = "2025-05-21T12:43:56.428Z" },
    { url = "https://files.pythonhosted.org/packages/d5/b1/3a8ee1c9d480e8493619a437dec685d005f706b69253286f50f498cbdbcf/rpds_py-0.25.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:083a9513a33e0b92cf6e7a6366036c6bb43ea595332c1ab5c8ae329e4bcc0a9c", size = 389023, upload-time = "2025-05-21T12:43:57.995Z" },
    { url = "https://files.pythonhosted.org/packages/3b/31/17293edcfc934dc62c3bf74a0cb449ecd549531f956b72287203e6880b87/rpds_py-0.25.1-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:816568614ecb22b18a010c7a12559c19f6fe993526af88e95a76d5a60b8b75fb", size = 403283, upload-time = "2025-05-21T12:43:59.546Z" },
    { url = "https://files.pythonhosted.org/packages/d1/ca/e0f0bc1a75a8925024f343258c8ecbd8828f8997ea2ac71e02f67b6f5299/rpds_py-0.25.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3c6564c0947a7f52e4792983f8e6cf9bac140438ebf81f527a21d944f2fd0a40", size = 524634, upload-time = "2025-05-21T12:44:01.087Z" },
    { url = "https://files.pythonhosted.org/packages/3e/03/5d0be919037178fff33a6672ffc0afa04ea1cfcb61afd4119d1b5280ff0f/rpds_py-0.25.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5c4a128527fe415d73cf1f70a9a688d06130d5810be69f3b553bf7b45e8acf79", size = 416233, upload-time = "2025-05-21T12:44:02.604Z" },
    { url = "https://files.pythonhosted.org/packages/05/7c/8abb70f9017a231c6c961a8941403ed6557664c0913e1bf413cbdc039e75/rpds_py-0.25.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a49e1d7a4978ed554f095430b89ecc23f42014a50ac385eb0c4d163ce213c325", size = 390375, upload-time = "2025-05-21T12:44:04.162Z" },
    { url = "https://files.pythonhosted.org/packages/7a/ac/a87f339f0e066b9535074a9f403b9313fd3892d4a164d5d5f5875ac9f29f/rpds_py-0.25.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d74ec9bc0e2feb81d3f16946b005748119c0f52a153f6db6a29e8cd68636f295", size = 424537, upload-time = "2025-05-21T12:44:06.175Z" },
    { url = "https://files.pythonhosted.org/packages/1f/8f/8d5c1567eaf8c8afe98a838dd24de5013ce6e8f53a01bd47fe8bb06b5533/rpds_py-0.25.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:3af5b4cc10fa41e5bc64e5c198a1b2d2864337f8fcbb9a67e747e34002ce812b", size = 566425, upload-time = "2025-05-21T12:44:08.242Z" },
    { url = "https://files.pythonhosted.org/packages/95/33/03016a6be5663b389c8ab0bbbcca68d9e96af14faeff0a04affcb587e776/rpds_py-0.25.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:79dc317a5f1c51fd9c6a0c4f48209c6b8526d0524a6904fc1076476e79b00f98", size = 595197, upload-time = "2025-05-21T12:44:10.449Z" },
    { url = "https://files.pythonhosted.org/packages/33/8d/da9f4d3e208c82fda311bff0cf0a19579afceb77cf456e46c559a1c075ba/rpds_py-0.25.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:1521031351865e0181bc585147624d66b3b00a84109b57fcb7a779c3ec3772cd", size = 561244, upload-time = "2025-05-21T12:44:12.387Z" },
    { url = "https://files.pythonhosted.org/packages/e2/b3/39d5dcf7c5f742ecd6dbc88f6f84ae54184b92f5f387a4053be2107b17f1/rpds_py-0.25.1-cp313-cp313-win32.whl", hash = "sha256:5d473be2b13600b93a5675d78f59e63b51b1ba2d0476893415dfbb5477e65b31", size = 222254, upload-time = "2025-05-21T12:44:14.261Z" },
    { url = "https://files.pythonhosted.org/packages/5f/19/2d6772c8eeb8302c5f834e6d0dfd83935a884e7c5ce16340c7eaf89ce925/rpds_py-0.25.1-cp313-cp313-win_amd64.whl", hash = "sha256:a7b74e92a3b212390bdce1d93da9f6488c3878c1d434c5e751cbc202c5e09500", size = 234741, upload-time = "2025-05-21T12:44:16.236Z" },
    { url = "https://files.pythonhosted.org/packages/5b/5a/145ada26cfaf86018d0eb304fe55eafdd4f0b6b84530246bb4a7c4fb5c4b/rpds_py-0.25.1-cp313-cp313-win_arm64.whl", hash = "sha256:dd326a81afe332ede08eb39ab75b301d5676802cdffd3a8f287a5f0b694dc3f5", size = 224830, upload-time = "2025-05-21T12:44:17.749Z" },
    { url = "https://files.pythonhosted.org/packages/4b/ca/d435844829c384fd2c22754ff65889c5c556a675d2ed9eb0e148435c6690/rpds_py-0.25.1-cp313-cp313t-macosx_10_12_x86_64.whl", hash = "sha256:a58d1ed49a94d4183483a3ce0af22f20318d4a1434acee255d683ad90bf78129", size = 359668, upload-time = "2025-05-21T12:44:19.322Z" },
    { url = "https://files.pythonhosted.org/packages/1f/01/b056f21db3a09f89410d493d2f6614d87bb162499f98b649d1dbd2a81988/rpds_py-0.25.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:f251bf23deb8332823aef1da169d5d89fa84c89f67bdfb566c49dea1fccfd50d", size = 345649, upload-time = "2025-05-21T12:44:20.962Z" },
    { url = "https://files.pythonhosted.org/packages/e0/0f/e0d00dc991e3d40e03ca36383b44995126c36b3eafa0ccbbd19664709c88/rpds_py-0.25.1-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8dbd586bfa270c1103ece2109314dd423df1fa3d9719928b5d09e4840cec0d72", size = 384776, upload-time = "2025-05-21T12:44:22.516Z" },
    { url = "https://files.pythonhosted.org/packages/9f/a2/59374837f105f2ca79bde3c3cd1065b2f8c01678900924949f6392eab66d/rpds_py-0.25.1-cp313-cp313t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:6d273f136e912aa101a9274c3145dcbddbe4bac560e77e6d5b3c9f6e0ed06d34", size = 395131, upload-time = "2025-05-21T12:44:24.147Z" },
    { url = "https://files.pythonhosted.org/packages/9c/dc/48e8d84887627a0fe0bac53f0b4631e90976fd5d35fff8be66b8e4f3916b/rpds_py-0.25.1-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:666fa7b1bd0a3810a7f18f6d3a25ccd8866291fbbc3c9b912b917a6715874bb9", size = 520942, upload-time = "2025-05-21T12:44:25.915Z" },
    { url = "https://files.pythonhosted.org/packages/7c/f5/ee056966aeae401913d37befeeab57a4a43a4f00099e0a20297f17b8f00c/rpds_py-0.25.1-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:921954d7fbf3fccc7de8f717799304b14b6d9a45bbeec5a8d7408ccbf531faf5", size = 411330, upload-time = "2025-05-21T12:44:27.638Z" },
    { url = "https://files.pythonhosted.org/packages/ab/74/b2cffb46a097cefe5d17f94ede7a174184b9d158a0aeb195f39f2c0361e8/rpds_py-0.25.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f3d86373ff19ca0441ebeb696ef64cb58b8b5cbacffcda5a0ec2f3911732a194", size = 387339, upload-time = "2025-05-21T12:44:29.292Z" },
    { url = "https://files.pythonhosted.org/packages/7f/9a/0ff0b375dcb5161c2b7054e7d0b7575f1680127505945f5cabaac890bc07/rpds_py-0.25.1-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:c8980cde3bb8575e7c956a530f2c217c1d6aac453474bf3ea0f9c89868b531b6", size = 418077, upload-time = "2025-05-21T12:44:30.877Z" },
    { url = "https://files.pythonhosted.org/packages/0d/a1/fda629bf20d6b698ae84c7c840cfb0e9e4200f664fc96e1f456f00e4ad6e/rpds_py-0.25.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:8eb8c84ecea987a2523e057c0d950bcb3f789696c0499290b8d7b3107a719d78", size = 562441, upload-time = "2025-05-21T12:44:32.541Z" },
    { url = "https://files.pythonhosted.org/packages/20/15/ce4b5257f654132f326f4acd87268e1006cc071e2c59794c5bdf4bebbb51/rpds_py-0.25.1-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:e43a005671a9ed5a650f3bc39e4dbccd6d4326b24fb5ea8be5f3a43a6f576c72", size = 590750, upload-time = "2025-05-21T12:44:34.557Z" },
    { url = "https://files.pythonhosted.org/packages/fb/ab/e04bf58a8d375aeedb5268edcc835c6a660ebf79d4384d8e0889439448b0/rpds_py-0.25.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:58f77c60956501a4a627749a6dcb78dac522f249dd96b5c9f1c6af29bfacfb66", size = 558891, upload-time = "2025-05-21T12:44:37.358Z" },
    { url = "https://files.pythonhosted.org/packages/90/82/cb8c6028a6ef6cd2b7991e2e4ced01c854b6236ecf51e81b64b569c43d73/rpds_py-0.25.1-cp313-cp313t-win32.whl", hash = "sha256:2cb9e5b5e26fc02c8a4345048cd9998c2aca7c2712bd1b36da0c72ee969a3523", size = 218718, upload-time = "2025-05-21T12:44:38.969Z" },
    { url = "https://files.pythonhosted.org/packages/b6/97/5a4b59697111c89477d20ba8a44df9ca16b41e737fa569d5ae8bff99e650/rpds_py-0.25.1-cp313-cp313t-win_amd64.whl", hash = "sha256:401ca1c4a20cc0510d3435d89c069fe0a9ae2ee6495135ac46bdd49ec0495763", size = 232218, upload-time = "2025-05-21T12:44:40.512Z" },
    { url = "https://files.pythonhosted.org/packages/78/ff/566ce53529b12b4f10c0a348d316bd766970b7060b4fd50f888be3b3b281/rpds_py-0.25.1-pp310-pypy310_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b24bf3cd93d5b6ecfbedec73b15f143596c88ee249fa98cefa9a9dc9d92c6f28", size = 373931, upload-time = "2025-05-21T12:45:05.01Z" },
    { url = "https://files.pythonhosted.org/packages/83/5d/deba18503f7c7878e26aa696e97f051175788e19d5336b3b0e76d3ef9256/rpds_py-0.25.1-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:0eb90e94f43e5085623932b68840b6f379f26db7b5c2e6bcef3179bd83c9330f", size = 359074, upload-time = "2025-05-21T12:45:06.714Z" },
    { url = "https://files.pythonhosted.org/packages/0d/74/313415c5627644eb114df49c56a27edba4d40cfd7c92bd90212b3604ca84/rpds_py-0.25.1-pp310-pypy310_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d50e4864498a9ab639d6d8854b25e80642bd362ff104312d9770b05d66e5fb13", size = 387255, upload-time = "2025-05-21T12:45:08.669Z" },
    { url = "https://files.pythonhosted.org/packages/8c/c8/c723298ed6338963d94e05c0f12793acc9b91d04ed7c4ba7508e534b7385/rpds_py-0.25.1-pp310-pypy310_pp73-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:7c9409b47ba0650544b0bb3c188243b83654dfe55dcc173a86832314e1a6a35d", size = 400714, upload-time = "2025-05-21T12:45:10.39Z" },
    { url = "https://files.pythonhosted.org/packages/33/8a/51f1f6aa653c2e110ed482ef2ae94140d56c910378752a1b483af11019ee/rpds_py-0.25.1-pp310-pypy310_pp73-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:796ad874c89127c91970652a4ee8b00d56368b7e00d3477f4415fe78164c8000", size = 523105, upload-time = "2025-05-21T12:45:12.273Z" },
    { url = "https://files.pythonhosted.org/packages/c7/a4/7873d15c088ad3bff36910b29ceb0f178e4b3232c2adbe9198de68a41e63/rpds_py-0.25.1-pp310-pypy310_pp73-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:85608eb70a659bf4c1142b2781083d4b7c0c4e2c90eff11856a9754e965b2540", size = 411499, upload-time = "2025-05-21T12:45:13.95Z" },
    { url = "https://files.pythonhosted.org/packages/90/f3/0ce1437befe1410766d11d08239333ac1b2d940f8a64234ce48a7714669c/rpds_py-0.25.1-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c4feb9211d15d9160bc85fa72fed46432cdc143eb9cf6d5ca377335a921ac37b", size = 387918, upload-time = "2025-05-21T12:45:15.649Z" },
    { url = "https://files.pythonhosted.org/packages/94/d4/5551247988b2a3566afb8a9dba3f1d4a3eea47793fd83000276c1a6c726e/rpds_py-0.25.1-pp310-pypy310_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:ccfa689b9246c48947d31dd9d8b16d89a0ecc8e0e26ea5253068efb6c542b76e", size = 421705, upload-time = "2025-05-21T12:45:17.788Z" },
    { url = "https://files.pythonhosted.org/packages/b0/25/5960f28f847bf736cc7ee3c545a7e1d2f3b5edaf82c96fb616c2f5ed52d0/rpds_py-0.25.1-pp310-pypy310_pp73-musllinux_1_2_aarch64.whl", hash = "sha256:3c5b317ecbd8226887994852e85de562f7177add602514d4ac40f87de3ae45a8", size = 564489, upload-time = "2025-05-21T12:45:19.466Z" },
    { url = "https://files.pythonhosted.org/packages/02/66/1c99884a0d44e8c2904d3c4ec302f995292d5dde892c3bf7685ac1930146/rpds_py-0.25.1-pp310-pypy310_pp73-musllinux_1_2_i686.whl", hash = "sha256:454601988aab2c6e8fd49e7634c65476b2b919647626208e376afcd22019eeb8", size = 592557, upload-time = "2025-05-21T12:45:21.362Z" },
    { url = "https://files.pythonhosted.org/packages/55/ae/4aeac84ebeffeac14abb05b3bb1d2f728d00adb55d3fb7b51c9fa772e760/rpds_py-0.25.1-pp310-pypy310_pp73-musllinux_1_2_x86_64.whl", hash = "sha256:1c0c434a53714358532d13539272db75a5ed9df75a4a090a753ac7173ec14e11", size = 558691, upload-time = "2025-05-21T12:45:23.084Z" },
    { url = "https://files.pythonhosted.org/packages/41/b3/728a08ff6f5e06fe3bb9af2e770e9d5fd20141af45cff8dfc62da4b2d0b3/rpds_py-0.25.1-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:f73ce1512e04fbe2bc97836e89830d6b4314c171587a99688082d090f934d20a", size = 231651, upload-time = "2025-05-21T12:45:24.72Z" },
    { url = "https://files.pythonhosted.org/packages/49/74/48f3df0715a585cbf5d34919c9c757a4c92c1a9eba059f2d334e72471f70/rpds_py-0.25.1-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:ee86d81551ec68a5c25373c5643d343150cc54672b5e9a0cafc93c1870a53954", size = 374208, upload-time = "2025-05-21T12:45:26.306Z" },
    { url = "https://files.pythonhosted.org/packages/55/b0/9b01bb11ce01ec03d05e627249cc2c06039d6aa24ea5a22a39c312167c10/rpds_py-0.25.1-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:89c24300cd4a8e4a51e55c31a8ff3918e6651b241ee8876a42cc2b2a078533ba", size = 359262, upload-time = "2025-05-21T12:45:28.322Z" },
    { url = "https://files.pythonhosted.org/packages/a9/eb/5395621618f723ebd5116c53282052943a726dba111b49cd2071f785b665/rpds_py-0.25.1-pp311-pypy311_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:771c16060ff4e79584dc48902a91ba79fd93eade3aa3a12d6d2a4aadaf7d542b", size = 387366, upload-time = "2025-05-21T12:45:30.42Z" },
    { url = "https://files.pythonhosted.org/packages/68/73/3d51442bdb246db619d75039a50ea1cf8b5b4ee250c3e5cd5c3af5981cd4/rpds_py-0.25.1-pp311-pypy311_pp73-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:785ffacd0ee61c3e60bdfde93baa6d7c10d86f15655bd706c89da08068dc5038", size = 400759, upload-time = "2025-05-21T12:45:32.516Z" },
    { url = "https://files.pythonhosted.org/packages/b7/4c/3a32d5955d7e6cb117314597bc0f2224efc798428318b13073efe306512a/rpds_py-0.25.1-pp311-pypy311_pp73-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:2a40046a529cc15cef88ac5ab589f83f739e2d332cb4d7399072242400ed68c9", size = 523128, upload-time = "2025-05-21T12:45:34.396Z" },
    { url = "https://files.pythonhosted.org/packages/be/95/1ffccd3b0bb901ae60b1dd4b1be2ab98bb4eb834cd9b15199888f5702f7b/rpds_py-0.25.1-pp311-pypy311_pp73-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:85fc223d9c76cabe5d0bff82214459189720dc135db45f9f66aa7cffbf9ff6c1", size = 411597, upload-time = "2025-05-21T12:45:36.164Z" },
    { url = "https://files.pythonhosted.org/packages/ef/6d/6e6cd310180689db8b0d2de7f7d1eabf3fb013f239e156ae0d5a1a85c27f/rpds_py-0.25.1-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b0be9965f93c222fb9b4cc254235b3b2b215796c03ef5ee64f995b1b69af0762", size = 388053, upload-time = "2025-05-21T12:45:38.45Z" },
    { url = "https://files.pythonhosted.org/packages/4a/87/ec4186b1fe6365ced6fa470960e68fc7804bafbe7c0cf5a36237aa240efa/rpds_py-0.25.1-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:8378fa4a940f3fb509c081e06cb7f7f2adae8cf46ef258b0e0ed7519facd573e", size = 421821, upload-time = "2025-05-21T12:45:40.732Z" },
    { url = "https://files.pythonhosted.org/packages/7a/60/84f821f6bf4e0e710acc5039d91f8f594fae0d93fc368704920d8971680d/rpds_py-0.25.1-pp311-pypy311_pp73-musllinux_1_2_aarch64.whl", hash = "sha256:33358883a4490287e67a2c391dfaea4d9359860281db3292b6886bf0be3d8692", size = 564534, upload-time = "2025-05-21T12:45:42.672Z" },
    { url = "https://files.pythonhosted.org/packages/41/3a/bc654eb15d3b38f9330fe0f545016ba154d89cdabc6177b0295910cd0ebe/rpds_py-0.25.1-pp311-pypy311_pp73-musllinux_1_2_i686.whl", hash = "sha256:1d1fadd539298e70cac2f2cb36f5b8a65f742b9b9f1014dd4ea1f7785e2470bf", size = 592674, upload-time = "2025-05-21T12:45:44.533Z" },
    { url = "https://files.pythonhosted.org/packages/2e/ba/31239736f29e4dfc7a58a45955c5db852864c306131fd6320aea214d5437/rpds_py-0.25.1-pp311-pypy311_pp73-musllinux_1_2_x86_64.whl", hash = "sha256:9a46c2fb2545e21181445515960006e85d22025bd2fe6db23e76daec6eb689fe", size = 558781, upload-time = "2025-05-21T12:45:46.281Z" },
]

[[package]]
name = "ruff"
version = "0.12.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/24/90/5255432602c0b196a0da6720f6f76b93eb50baef46d3c9b0025e2f9acbf3/ruff-0.12.0.tar.gz", hash = "sha256:4d047db3662418d4a848a3fdbfaf17488b34b62f527ed6f10cb8afd78135bc5c", size = 4376101, upload-time = "2025-06-17T15:19:26.217Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e6/fd/b46bb20e14b11ff49dbc74c61de352e0dc07fb650189513631f6fb5fc69f/ruff-0.12.0-py3-none-linux_armv6l.whl", hash = "sha256:5652a9ecdb308a1754d96a68827755f28d5dfb416b06f60fd9e13f26191a8848", size = 10311554, upload-time = "2025-06-17T15:18:45.792Z" },
    { url = "https://files.pythonhosted.org/packages/e7/d3/021dde5a988fa3e25d2468d1dadeea0ae89dc4bc67d0140c6e68818a12a1/ruff-0.12.0-py3-none-macosx_10_12_x86_64.whl", hash = "sha256:05ed0c914fabc602fc1f3b42c53aa219e5736cb030cdd85640c32dbc73da74a6", size = 11118435, upload-time = "2025-06-17T15:18:49.064Z" },
    { url = "https://files.pythonhosted.org/packages/07/a2/01a5acf495265c667686ec418f19fd5c32bcc326d4c79ac28824aecd6a32/ruff-0.12.0-py3-none-macosx_11_0_arm64.whl", hash = "sha256:07a7aa9b69ac3fcfda3c507916d5d1bca10821fe3797d46bad10f2c6de1edda0", size = 10466010, upload-time = "2025-06-17T15:18:51.341Z" },
    { url = "https://files.pythonhosted.org/packages/4c/57/7caf31dd947d72e7aa06c60ecb19c135cad871a0a8a251723088132ce801/ruff-0.12.0-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e7731c3eec50af71597243bace7ec6104616ca56dda2b99c89935fe926bdcd48", size = 10661366, upload-time = "2025-06-17T15:18:53.29Z" },
    { url = "https://files.pythonhosted.org/packages/e9/ba/aa393b972a782b4bc9ea121e0e358a18981980856190d7d2b6187f63e03a/ruff-0.12.0-py3-none-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:952d0630eae628250ab1c70a7fffb641b03e6b4a2d3f3ec6c1d19b4ab6c6c807", size = 10173492, upload-time = "2025-06-17T15:18:55.262Z" },
    { url = "https://files.pythonhosted.org/packages/d7/50/9349ee777614bc3062fc6b038503a59b2034d09dd259daf8192f56c06720/ruff-0.12.0-py3-none-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c021f04ea06966b02614d442e94071781c424ab8e02ec7af2f037b4c1e01cc82", size = 11761739, upload-time = "2025-06-17T15:18:58.906Z" },
    { url = "https://files.pythonhosted.org/packages/04/8f/ad459de67c70ec112e2ba7206841c8f4eb340a03ee6a5cabc159fe558b8e/ruff-0.12.0-py3-none-manylinux_2_17_ppc64.manylinux2014_ppc64.whl", hash = "sha256:7d235618283718ee2fe14db07f954f9b2423700919dc688eacf3f8797a11315c", size = 12537098, upload-time = "2025-06-17T15:19:01.316Z" },
    { url = "https://files.pythonhosted.org/packages/ed/50/15ad9c80ebd3c4819f5bd8883e57329f538704ed57bac680d95cb6627527/ruff-0.12.0-py3-none-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:0c0758038f81beec8cc52ca22de9685b8ae7f7cc18c013ec2050012862cc9165", size = 12154122, upload-time = "2025-06-17T15:19:03.727Z" },
    { url = "https://files.pythonhosted.org/packages/76/e6/79b91e41bc8cc3e78ee95c87093c6cacfa275c786e53c9b11b9358026b3d/ruff-0.12.0-py3-none-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:139b3d28027987b78fc8d6cfb61165447bdf3740e650b7c480744873688808c2", size = 11363374, upload-time = "2025-06-17T15:19:05.875Z" },
    { url = "https://files.pythonhosted.org/packages/db/c3/82b292ff8a561850934549aa9dc39e2c4e783ab3c21debe55a495ddf7827/ruff-0.12.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:68853e8517b17bba004152aebd9dd77d5213e503a5f2789395b25f26acac0da4", size = 11587647, upload-time = "2025-06-17T15:19:08.246Z" },
    { url = "https://files.pythonhosted.org/packages/2b/42/d5760d742669f285909de1bbf50289baccb647b53e99b8a3b4f7ce1b2001/ruff-0.12.0-py3-none-musllinux_1_2_aarch64.whl", hash = "sha256:3a9512af224b9ac4757f7010843771da6b2b0935a9e5e76bb407caa901a1a514", size = 10527284, upload-time = "2025-06-17T15:19:10.37Z" },
    { url = "https://files.pythonhosted.org/packages/19/f6/fcee9935f25a8a8bba4adbae62495c39ef281256693962c2159e8b284c5f/ruff-0.12.0-py3-none-musllinux_1_2_armv7l.whl", hash = "sha256:b08df3d96db798e5beb488d4df03011874aff919a97dcc2dd8539bb2be5d6a88", size = 10158609, upload-time = "2025-06-17T15:19:12.286Z" },
    { url = "https://files.pythonhosted.org/packages/37/fb/057febf0eea07b9384787bfe197e8b3384aa05faa0d6bd844b94ceb29945/ruff-0.12.0-py3-none-musllinux_1_2_i686.whl", hash = "sha256:6a315992297a7435a66259073681bb0d8647a826b7a6de45c6934b2ca3a9ed51", size = 11141462, upload-time = "2025-06-17T15:19:15.195Z" },
    { url = "https://files.pythonhosted.org/packages/10/7c/1be8571011585914b9d23c95b15d07eec2d2303e94a03df58294bc9274d4/ruff-0.12.0-py3-none-musllinux_1_2_x86_64.whl", hash = "sha256:1e55e44e770e061f55a7dbc6e9aed47feea07731d809a3710feda2262d2d4d8a", size = 11641616, upload-time = "2025-06-17T15:19:17.6Z" },
    { url = "https://files.pythonhosted.org/packages/6a/ef/b960ab4818f90ff59e571d03c3f992828d4683561095e80f9ef31f3d58b7/ruff-0.12.0-py3-none-win32.whl", hash = "sha256:7162a4c816f8d1555eb195c46ae0bd819834d2a3f18f98cc63819a7b46f474fb", size = 10525289, upload-time = "2025-06-17T15:19:19.688Z" },
    { url = "https://files.pythonhosted.org/packages/34/93/8b16034d493ef958a500f17cda3496c63a537ce9d5a6479feec9558f1695/ruff-0.12.0-py3-none-win_amd64.whl", hash = "sha256:d00b7a157b8fb6d3827b49d3324da34a1e3f93492c1f97b08e222ad7e9b291e0", size = 11598311, upload-time = "2025-06-17T15:19:21.785Z" },
    { url = "https://files.pythonhosted.org/packages/d0/33/4d3e79e4a84533d6cd526bfb42c020a23256ae5e4265d858bd1287831f7d/ruff-0.12.0-py3-none-win_arm64.whl", hash = "sha256:8cd24580405ad8c1cc64d61725bca091d6b6da7eb3d36f72cc605467069d7e8b", size = 10724946, upload-time = "2025-06-17T15:19:23.952Z" },
]

[[package]]
name = "shellingham"
version = "1.5.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/58/15/8b3609fd3830ef7b27b655beb4b4e9c62313a4e8da8c676e142cc210d58e/shellingham-1.5.4.tar.gz", hash = "sha256:8dbca0739d487e5bd35ab3ca4b36e11c4078f3a234bfce294b0a0291363404de", size = 10310, upload-time = "2023-10-24T04:13:40.426Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e0/f9/0595336914c5619e5f28a1fb793285925a8cd4b432c9da0a987836c7f822/shellingham-1.5.4-py2.py3-none-any.whl", hash = "sha256:7ecfff8f2fd72616f7481040475a65b2bf8af90a56c89140852d1120324e8686", size = 9755, upload-time = "2023-10-24T04:13:38.866Z" },
]

[[package]]
name = "smmap"
version = "5.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/44/cd/a040c4b3119bbe532e5b0732286f805445375489fceaec1f48306068ee3b/smmap-5.0.2.tar.gz", hash = "sha256:26ea65a03958fa0c8a1c7e8c7a58fdc77221b8910f6be2131affade476898ad5", size = 22329, upload-time = "2025-01-02T07:14:40.909Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/be/d09147ad1ec7934636ad912901c5fd7667e1c858e19d355237db0d0cd5e4/smmap-5.0.2-py3-none-any.whl", hash = "sha256:b30115f0def7d7531d22a0fb6502488d879e75b260a9db4d0819cfb25403af5e", size = 24303, upload-time = "2025-01-02T07:14:38.724Z" },
]

[[package]]
name = "sniffio"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/87/a6771e1546d97e7e041b6ae58d80074f81b7d5121207425c964ddf5cfdbd/sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc", size = 20372, upload-time = "2024-02-25T23:20:04.057Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2", size = 10235, upload-time = "2024-02-25T23:20:01.196Z" },
]

[[package]]
name = "sse-starlette"
version = "2.3.6"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
]
sdist = { url = "https://files.pythonhosted.org/packages/8c/f4/989bc70cb8091eda43a9034ef969b25145291f3601703b82766e5172dfed/sse_starlette-2.3.6.tar.gz", hash = "sha256:0382336f7d4ec30160cf9ca0518962905e1b69b72d6c1c995131e0a703b436e3", size = 18284, upload-time = "2025-05-30T13:34:12.914Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/81/05/78850ac6e79af5b9508f8841b0f26aa9fd329a1ba00bf65453c2d312bcc8/sse_starlette-2.3.6-py3-none-any.whl", hash = "sha256:d49a8285b182f6e2228e2609c350398b2ca2c36216c2675d875f81e93548f760", size = 10606, upload-time = "2025-05-30T13:34:11.703Z" },
]

[[package]]
name = "stack-data"
version = "0.6.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "asttokens" },
    { name = "executing" },
    { name = "pure-eval" },
]
sdist = { url = "https://files.pythonhosted.org/packages/28/e3/55dcc2cfbc3ca9c29519eb6884dd1415ecb53b0e934862d3559ddcb7e20b/stack_data-0.6.3.tar.gz", hash = "sha256:836a778de4fec4dcd1dcd89ed8abff8a221f58308462e1c4aa2a3cf30148f0b9", size = 44707, upload-time = "2023-09-30T13:58:05.479Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f1/7b/ce1eafaf1a76852e2ec9b22edecf1daa58175c090266e9f6c64afcd81d91/stack_data-0.6.3-py3-none-any.whl", hash = "sha256:d5558e0c25a4cb0853cddad3d77da9891a08cb85dd9f9f91b9f8cd66e511e695", size = 24521, upload-time = "2023-09-30T13:58:03.53Z" },
]

[[package]]
name = "starlette"
version = "0.46.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ce/20/08dfcd9c983f6a6f4a1000d934b9e6d626cff8d2eeb77a89a68eef20a2b7/starlette-0.46.2.tar.gz", hash = "sha256:7f7361f34eed179294600af672f565727419830b54b7b084efe44bb82d2fccd5", size = 2580846, upload-time = "2025-04-13T13:56:17.942Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8b/0c/9d30a4ebeb6db2b25a841afbb80f6ef9a854fc3b41be131d249a977b4959/starlette-0.46.2-py3-none-any.whl", hash = "sha256:595633ce89f8ffa71a015caed34a5b2dc1c0cdb3f0f1fbd1e69339cf2abeec35", size = 72037, upload-time = "2025-04-13T13:56:16.21Z" },
]

[[package]]
name = "tiktoken"
version = "0.9.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "regex" },
    { name = "requests" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ea/cf/756fedf6981e82897f2d570dd25fa597eb3f4459068ae0572d7e888cfd6f/tiktoken-0.9.0.tar.gz", hash = "sha256:d02a5ca6a938e0490e1ff957bc48c8b078c88cb83977be1625b1fd8aac792c5d", size = 35991, upload-time = "2025-02-14T06:03:01.003Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/64/f3/50ec5709fad61641e4411eb1b9ac55b99801d71f1993c29853f256c726c9/tiktoken-0.9.0-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:586c16358138b96ea804c034b8acf3f5d3f0258bd2bc3b0227af4af5d622e382", size = 1065770, upload-time = "2025-02-14T06:02:01.251Z" },
    { url = "https://files.pythonhosted.org/packages/d6/f8/5a9560a422cf1755b6e0a9a436e14090eeb878d8ec0f80e0cd3d45b78bf4/tiktoken-0.9.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:d9c59ccc528c6c5dd51820b3474402f69d9a9e1d656226848ad68a8d5b2e5108", size = 1009314, upload-time = "2025-02-14T06:02:02.869Z" },
    { url = "https://files.pythonhosted.org/packages/bc/20/3ed4cfff8f809cb902900ae686069e029db74567ee10d017cb254df1d598/tiktoken-0.9.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f0968d5beeafbca2a72c595e8385a1a1f8af58feaebb02b227229b69ca5357fd", size = 1143140, upload-time = "2025-02-14T06:02:04.165Z" },
    { url = "https://files.pythonhosted.org/packages/f1/95/cc2c6d79df8f113bdc6c99cdec985a878768120d87d839a34da4bd3ff90a/tiktoken-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:92a5fb085a6a3b7350b8fc838baf493317ca0e17bd95e8642f95fc69ecfed1de", size = 1197860, upload-time = "2025-02-14T06:02:06.268Z" },
    { url = "https://files.pythonhosted.org/packages/c7/6c/9c1a4cc51573e8867c9381db1814223c09ebb4716779c7f845d48688b9c8/tiktoken-0.9.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:15a2752dea63d93b0332fb0ddb05dd909371ededa145fe6a3242f46724fa7990", size = 1259661, upload-time = "2025-02-14T06:02:08.889Z" },
    { url = "https://files.pythonhosted.org/packages/cd/4c/22eb8e9856a2b1808d0a002d171e534eac03f96dbe1161978d7389a59498/tiktoken-0.9.0-cp310-cp310-win_amd64.whl", hash = "sha256:26113fec3bd7a352e4b33dbaf1bd8948de2507e30bd95a44e2b1156647bc01b4", size = 894026, upload-time = "2025-02-14T06:02:12.841Z" },
    { url = "https://files.pythonhosted.org/packages/4d/ae/4613a59a2a48e761c5161237fc850eb470b4bb93696db89da51b79a871f1/tiktoken-0.9.0-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:f32cc56168eac4851109e9b5d327637f15fd662aa30dd79f964b7c39fbadd26e", size = 1065987, upload-time = "2025-02-14T06:02:14.174Z" },
    { url = "https://files.pythonhosted.org/packages/3f/86/55d9d1f5b5a7e1164d0f1538a85529b5fcba2b105f92db3622e5d7de6522/tiktoken-0.9.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:45556bc41241e5294063508caf901bf92ba52d8ef9222023f83d2483a3055348", size = 1009155, upload-time = "2025-02-14T06:02:15.384Z" },
    { url = "https://files.pythonhosted.org/packages/03/58/01fb6240df083b7c1916d1dcb024e2b761213c95d576e9f780dfb5625a76/tiktoken-0.9.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:03935988a91d6d3216e2ec7c645afbb3d870b37bcb67ada1943ec48678e7ee33", size = 1142898, upload-time = "2025-02-14T06:02:16.666Z" },
    { url = "https://files.pythonhosted.org/packages/b1/73/41591c525680cd460a6becf56c9b17468d3711b1df242c53d2c7b2183d16/tiktoken-0.9.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8b3d80aad8d2c6b9238fc1a5524542087c52b860b10cbf952429ffb714bc1136", size = 1197535, upload-time = "2025-02-14T06:02:18.595Z" },
    { url = "https://files.pythonhosted.org/packages/7d/7c/1069f25521c8f01a1a182f362e5c8e0337907fae91b368b7da9c3e39b810/tiktoken-0.9.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:b2a21133be05dc116b1d0372af051cd2c6aa1d2188250c9b553f9fa49301b336", size = 1259548, upload-time = "2025-02-14T06:02:20.729Z" },
    { url = "https://files.pythonhosted.org/packages/6f/07/c67ad1724b8e14e2b4c8cca04b15da158733ac60136879131db05dda7c30/tiktoken-0.9.0-cp311-cp311-win_amd64.whl", hash = "sha256:11a20e67fdf58b0e2dea7b8654a288e481bb4fc0289d3ad21291f8d0849915fb", size = 893895, upload-time = "2025-02-14T06:02:22.67Z" },
    { url = "https://files.pythonhosted.org/packages/cf/e5/21ff33ecfa2101c1bb0f9b6df750553bd873b7fb532ce2cb276ff40b197f/tiktoken-0.9.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:e88f121c1c22b726649ce67c089b90ddda8b9662545a8aeb03cfef15967ddd03", size = 1065073, upload-time = "2025-02-14T06:02:24.768Z" },
    { url = "https://files.pythonhosted.org/packages/8e/03/a95e7b4863ee9ceec1c55983e4cc9558bcfd8f4f80e19c4f8a99642f697d/tiktoken-0.9.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:a6600660f2f72369acb13a57fb3e212434ed38b045fd8cc6cdd74947b4b5d210", size = 1008075, upload-time = "2025-02-14T06:02:26.92Z" },
    { url = "https://files.pythonhosted.org/packages/40/10/1305bb02a561595088235a513ec73e50b32e74364fef4de519da69bc8010/tiktoken-0.9.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:95e811743b5dfa74f4b227927ed86cbc57cad4df859cb3b643be797914e41794", size = 1140754, upload-time = "2025-02-14T06:02:28.124Z" },
    { url = "https://files.pythonhosted.org/packages/1b/40/da42522018ca496432ffd02793c3a72a739ac04c3794a4914570c9bb2925/tiktoken-0.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:99376e1370d59bcf6935c933cb9ba64adc29033b7e73f5f7569f3aad86552b22", size = 1196678, upload-time = "2025-02-14T06:02:29.845Z" },
    { url = "https://files.pythonhosted.org/packages/5c/41/1e59dddaae270ba20187ceb8aa52c75b24ffc09f547233991d5fd822838b/tiktoken-0.9.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:badb947c32739fb6ddde173e14885fb3de4d32ab9d8c591cbd013c22b4c31dd2", size = 1259283, upload-time = "2025-02-14T06:02:33.838Z" },
    { url = "https://files.pythonhosted.org/packages/5b/64/b16003419a1d7728d0d8c0d56a4c24325e7b10a21a9dd1fc0f7115c02f0a/tiktoken-0.9.0-cp312-cp312-win_amd64.whl", hash = "sha256:5a62d7a25225bafed786a524c1b9f0910a1128f4232615bf3f8257a73aaa3b16", size = 894897, upload-time = "2025-02-14T06:02:36.265Z" },
    { url = "https://files.pythonhosted.org/packages/7a/11/09d936d37f49f4f494ffe660af44acd2d99eb2429d60a57c71318af214e0/tiktoken-0.9.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:2b0e8e05a26eda1249e824156d537015480af7ae222ccb798e5234ae0285dbdb", size = 1064919, upload-time = "2025-02-14T06:02:37.494Z" },
    { url = "https://files.pythonhosted.org/packages/80/0e/f38ba35713edb8d4197ae602e80837d574244ced7fb1b6070b31c29816e0/tiktoken-0.9.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:27d457f096f87685195eea0165a1807fae87b97b2161fe8c9b1df5bd74ca6f63", size = 1007877, upload-time = "2025-02-14T06:02:39.516Z" },
    { url = "https://files.pythonhosted.org/packages/fe/82/9197f77421e2a01373e27a79dd36efdd99e6b4115746ecc553318ecafbf0/tiktoken-0.9.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2cf8ded49cddf825390e36dd1ad35cd49589e8161fdcb52aa25f0583e90a3e01", size = 1140095, upload-time = "2025-02-14T06:02:41.791Z" },
    { url = "https://files.pythonhosted.org/packages/f2/bb/4513da71cac187383541facd0291c4572b03ec23c561de5811781bbd988f/tiktoken-0.9.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:cc156cb314119a8bb9748257a2eaebd5cc0753b6cb491d26694ed42fc7cb3139", size = 1195649, upload-time = "2025-02-14T06:02:43Z" },
    { url = "https://files.pythonhosted.org/packages/fa/5c/74e4c137530dd8504e97e3a41729b1103a4ac29036cbfd3250b11fd29451/tiktoken-0.9.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:cd69372e8c9dd761f0ab873112aba55a0e3e506332dd9f7522ca466e817b1b7a", size = 1258465, upload-time = "2025-02-14T06:02:45.046Z" },
    { url = "https://files.pythonhosted.org/packages/de/a8/8f499c179ec900783ffe133e9aab10044481679bb9aad78436d239eee716/tiktoken-0.9.0-cp313-cp313-win_amd64.whl", hash = "sha256:5ea0edb6f83dc56d794723286215918c1cde03712cbbafa0348b33448faf5b95", size = 894669, upload-time = "2025-02-14T06:02:47.341Z" },
]

[[package]]
name = "tomli"
version = "2.2.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/18/87/302344fed471e44a87289cf4967697d07e532f2421fdaf868a303cbae4ff/tomli-2.2.1.tar.gz", hash = "sha256:cd45e1dc79c835ce60f7404ec8119f2eb06d38b1deba146f07ced3bbc44505ff", size = 17175, upload-time = "2024-11-27T22:38:36.873Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/43/ca/75707e6efa2b37c77dadb324ae7d9571cb424e61ea73fad7c56c2d14527f/tomli-2.2.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:678e4fa69e4575eb77d103de3df8a895e1591b48e740211bd1067378c69e8249", size = 131077, upload-time = "2024-11-27T22:37:54.956Z" },
    { url = "https://files.pythonhosted.org/packages/c7/16/51ae563a8615d472fdbffc43a3f3d46588c264ac4f024f63f01283becfbb/tomli-2.2.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:023aa114dd824ade0100497eb2318602af309e5a55595f76b626d6d9f3b7b0a6", size = 123429, upload-time = "2024-11-27T22:37:56.698Z" },
    { url = "https://files.pythonhosted.org/packages/f1/dd/4f6cd1e7b160041db83c694abc78e100473c15d54620083dbd5aae7b990e/tomli-2.2.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ece47d672db52ac607a3d9599a9d48dcb2f2f735c6c2d1f34130085bb12b112a", size = 226067, upload-time = "2024-11-27T22:37:57.63Z" },
    { url = "https://files.pythonhosted.org/packages/a9/6b/c54ede5dc70d648cc6361eaf429304b02f2871a345bbdd51e993d6cdf550/tomli-2.2.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6972ca9c9cc9f0acaa56a8ca1ff51e7af152a9f87fb64623e31d5c83700080ee", size = 236030, upload-time = "2024-11-27T22:37:59.344Z" },
    { url = "https://files.pythonhosted.org/packages/1f/47/999514fa49cfaf7a92c805a86c3c43f4215621855d151b61c602abb38091/tomli-2.2.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c954d2250168d28797dd4e3ac5cf812a406cd5a92674ee4c8f123c889786aa8e", size = 240898, upload-time = "2024-11-27T22:38:00.429Z" },
    { url = "https://files.pythonhosted.org/packages/73/41/0a01279a7ae09ee1573b423318e7934674ce06eb33f50936655071d81a24/tomli-2.2.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:8dd28b3e155b80f4d54beb40a441d366adcfe740969820caf156c019fb5c7ec4", size = 229894, upload-time = "2024-11-27T22:38:02.094Z" },
    { url = "https://files.pythonhosted.org/packages/55/18/5d8bc5b0a0362311ce4d18830a5d28943667599a60d20118074ea1b01bb7/tomli-2.2.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:e59e304978767a54663af13c07b3d1af22ddee3bb2fb0618ca1593e4f593a106", size = 245319, upload-time = "2024-11-27T22:38:03.206Z" },
    { url = "https://files.pythonhosted.org/packages/92/a3/7ade0576d17f3cdf5ff44d61390d4b3febb8a9fc2b480c75c47ea048c646/tomli-2.2.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:33580bccab0338d00994d7f16f4c4ec25b776af3ffaac1ed74e0b3fc95e885a8", size = 238273, upload-time = "2024-11-27T22:38:04.217Z" },
    { url = "https://files.pythonhosted.org/packages/72/6f/fa64ef058ac1446a1e51110c375339b3ec6be245af9d14c87c4a6412dd32/tomli-2.2.1-cp311-cp311-win32.whl", hash = "sha256:465af0e0875402f1d226519c9904f37254b3045fc5084697cefb9bdde1ff99ff", size = 98310, upload-time = "2024-11-27T22:38:05.908Z" },
    { url = "https://files.pythonhosted.org/packages/6a/1c/4a2dcde4a51b81be3530565e92eda625d94dafb46dbeb15069df4caffc34/tomli-2.2.1-cp311-cp311-win_amd64.whl", hash = "sha256:2d0f2fdd22b02c6d81637a3c95f8cd77f995846af7414c5c4b8d0545afa1bc4b", size = 108309, upload-time = "2024-11-27T22:38:06.812Z" },
    { url = "https://files.pythonhosted.org/packages/52/e1/f8af4c2fcde17500422858155aeb0d7e93477a0d59a98e56cbfe75070fd0/tomli-2.2.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:4a8f6e44de52d5e6c657c9fe83b562f5f4256d8ebbfe4ff922c495620a7f6cea", size = 132762, upload-time = "2024-11-27T22:38:07.731Z" },
    { url = "https://files.pythonhosted.org/packages/03/b8/152c68bb84fc00396b83e7bbddd5ec0bd3dd409db4195e2a9b3e398ad2e3/tomli-2.2.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:8d57ca8095a641b8237d5b079147646153d22552f1c637fd3ba7f4b0b29167a8", size = 123453, upload-time = "2024-11-27T22:38:09.384Z" },
    { url = "https://files.pythonhosted.org/packages/c8/d6/fc9267af9166f79ac528ff7e8c55c8181ded34eb4b0e93daa767b8841573/tomli-2.2.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4e340144ad7ae1533cb897d406382b4b6fede8890a03738ff1683af800d54192", size = 233486, upload-time = "2024-11-27T22:38:10.329Z" },
    { url = "https://files.pythonhosted.org/packages/5c/51/51c3f2884d7bab89af25f678447ea7d297b53b5a3b5730a7cb2ef6069f07/tomli-2.2.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:db2b95f9de79181805df90bedc5a5ab4c165e6ec3fe99f970d0e302f384ad222", size = 242349, upload-time = "2024-11-27T22:38:11.443Z" },
    { url = "https://files.pythonhosted.org/packages/ab/df/bfa89627d13a5cc22402e441e8a931ef2108403db390ff3345c05253935e/tomli-2.2.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:40741994320b232529c802f8bc86da4e1aa9f413db394617b9a256ae0f9a7f77", size = 252159, upload-time = "2024-11-27T22:38:13.099Z" },
    { url = "https://files.pythonhosted.org/packages/9e/6e/fa2b916dced65763a5168c6ccb91066f7639bdc88b48adda990db10c8c0b/tomli-2.2.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:400e720fe168c0f8521520190686ef8ef033fb19fc493da09779e592861b78c6", size = 237243, upload-time = "2024-11-27T22:38:14.766Z" },
    { url = "https://files.pythonhosted.org/packages/b4/04/885d3b1f650e1153cbb93a6a9782c58a972b94ea4483ae4ac5cedd5e4a09/tomli-2.2.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:02abe224de6ae62c19f090f68da4e27b10af2b93213d36cf44e6e1c5abd19fdd", size = 259645, upload-time = "2024-11-27T22:38:15.843Z" },
    { url = "https://files.pythonhosted.org/packages/9c/de/6b432d66e986e501586da298e28ebeefd3edc2c780f3ad73d22566034239/tomli-2.2.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:b82ebccc8c8a36f2094e969560a1b836758481f3dc360ce9a3277c65f374285e", size = 244584, upload-time = "2024-11-27T22:38:17.645Z" },
    { url = "https://files.pythonhosted.org/packages/1c/9a/47c0449b98e6e7d1be6cbac02f93dd79003234ddc4aaab6ba07a9a7482e2/tomli-2.2.1-cp312-cp312-win32.whl", hash = "sha256:889f80ef92701b9dbb224e49ec87c645ce5df3fa2cc548664eb8a25e03127a98", size = 98875, upload-time = "2024-11-27T22:38:19.159Z" },
    { url = "https://files.pythonhosted.org/packages/ef/60/9b9638f081c6f1261e2688bd487625cd1e660d0a85bd469e91d8db969734/tomli-2.2.1-cp312-cp312-win_amd64.whl", hash = "sha256:7fc04e92e1d624a4a63c76474610238576942d6b8950a2d7f908a340494e67e4", size = 109418, upload-time = "2024-11-27T22:38:20.064Z" },
    { url = "https://files.pythonhosted.org/packages/04/90/2ee5f2e0362cb8a0b6499dc44f4d7d48f8fff06d28ba46e6f1eaa61a1388/tomli-2.2.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:f4039b9cbc3048b2416cc57ab3bda989a6fcf9b36cf8937f01a6e731b64f80d7", size = 132708, upload-time = "2024-11-27T22:38:21.659Z" },
    { url = "https://files.pythonhosted.org/packages/c0/ec/46b4108816de6b385141f082ba99e315501ccd0a2ea23db4a100dd3990ea/tomli-2.2.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:286f0ca2ffeeb5b9bd4fcc8d6c330534323ec51b2f52da063b11c502da16f30c", size = 123582, upload-time = "2024-11-27T22:38:22.693Z" },
    { url = "https://files.pythonhosted.org/packages/a0/bd/b470466d0137b37b68d24556c38a0cc819e8febe392d5b199dcd7f578365/tomli-2.2.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a92ef1a44547e894e2a17d24e7557a5e85a9e1d0048b0b5e7541f76c5032cb13", size = 232543, upload-time = "2024-11-27T22:38:24.367Z" },
    { url = "https://files.pythonhosted.org/packages/d9/e5/82e80ff3b751373f7cead2815bcbe2d51c895b3c990686741a8e56ec42ab/tomli-2.2.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9316dc65bed1684c9a98ee68759ceaed29d229e985297003e494aa825ebb0281", size = 241691, upload-time = "2024-11-27T22:38:26.081Z" },
    { url = "https://files.pythonhosted.org/packages/05/7e/2a110bc2713557d6a1bfb06af23dd01e7dde52b6ee7dadc589868f9abfac/tomli-2.2.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e85e99945e688e32d5a35c1ff38ed0b3f41f43fad8df0bdf79f72b2ba7bc5272", size = 251170, upload-time = "2024-11-27T22:38:27.921Z" },
    { url = "https://files.pythonhosted.org/packages/64/7b/22d713946efe00e0adbcdfd6d1aa119ae03fd0b60ebed51ebb3fa9f5a2e5/tomli-2.2.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:ac065718db92ca818f8d6141b5f66369833d4a80a9d74435a268c52bdfa73140", size = 236530, upload-time = "2024-11-27T22:38:29.591Z" },
    { url = "https://files.pythonhosted.org/packages/38/31/3a76f67da4b0cf37b742ca76beaf819dca0ebef26d78fc794a576e08accf/tomli-2.2.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:d920f33822747519673ee656a4b6ac33e382eca9d331c87770faa3eef562aeb2", size = 258666, upload-time = "2024-11-27T22:38:30.639Z" },
    { url = "https://files.pythonhosted.org/packages/07/10/5af1293da642aded87e8a988753945d0cf7e00a9452d3911dd3bb354c9e2/tomli-2.2.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:a198f10c4d1b1375d7687bc25294306e551bf1abfa4eace6650070a5c1ae2744", size = 243954, upload-time = "2024-11-27T22:38:31.702Z" },
    { url = "https://files.pythonhosted.org/packages/5b/b9/1ed31d167be802da0fc95020d04cd27b7d7065cc6fbefdd2f9186f60d7bd/tomli-2.2.1-cp313-cp313-win32.whl", hash = "sha256:d3f5614314d758649ab2ab3a62d4f2004c825922f9e370b29416484086b264ec", size = 98724, upload-time = "2024-11-27T22:38:32.837Z" },
    { url = "https://files.pythonhosted.org/packages/c7/32/b0963458706accd9afcfeb867c0f9175a741bf7b19cd424230714d722198/tomli-2.2.1-cp313-cp313-win_amd64.whl", hash = "sha256:a38aa0308e754b0e3c67e344754dff64999ff9b513e691d0e786265c93583c69", size = 109383, upload-time = "2024-11-27T22:38:34.455Z" },
    { url = "https://files.pythonhosted.org/packages/6e/c2/61d3e0f47e2b74ef40a68b9e6ad5984f6241a942f7cd3bbfbdbd03861ea9/tomli-2.2.1-py3-none-any.whl", hash = "sha256:cb55c73c5f4408779d0cf3eef9f762b9c9f147a77de7b258bef0a5628adc85cc", size = 14257, upload-time = "2024-11-27T22:38:35.385Z" },
]

[[package]]
name = "traitlets"
version = "5.14.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/eb/79/72064e6a701c2183016abbbfedaba506d81e30e232a68c9f0d6f6fcd1574/traitlets-5.14.3.tar.gz", hash = "sha256:9ed0579d3502c94b4b3732ac120375cda96f923114522847de4b3bb98b96b6b7", size = 161621, upload-time = "2024-04-19T11:11:49.746Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/00/c0/8f5d070730d7836adc9c9b6408dec68c6ced86b304a9b26a14df072a6e8c/traitlets-5.14.3-py3-none-any.whl", hash = "sha256:b74e89e397b1ed28cc831db7aea759ba6640cb3de13090ca145426688ff1ac4f", size = 85359, upload-time = "2024-04-19T11:11:46.763Z" },
]

[[package]]
name = "typer"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "rich" },
    { name = "shellingham" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c5/8c/7d682431efca5fd290017663ea4588bf6f2c6aad085c7f108c5dbc316e70/typer-0.16.0.tar.gz", hash = "sha256:af377ffaee1dbe37ae9440cb4e8f11686ea5ce4e9bae01b84ae7c63b87f1dd3b", size = 102625, upload-time = "2025-05-26T14:30:31.824Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/76/42/3efaf858001d2c2913de7f354563e3a3a2f0decae3efe98427125a8f441e/typer-0.16.0-py3-none-any.whl", hash = "sha256:1f79bed11d4d02d4310e3c1b7ba594183bcedb0ac73b27a9e5f28f6fb5b98855", size = 46317, upload-time = "2025-05-26T14:30:30.523Z" },
]

[[package]]
name = "typing-extensions"
version = "4.14.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d1/bc/51647cd02527e87d05cb083ccc402f93e441606ff1f01739a62c8ad09ba5/typing_extensions-4.14.0.tar.gz", hash = "sha256:8676b788e32f02ab42d9e7c61324048ae4c6d844a399eebace3d4979d75ceef4", size = 107423, upload-time = "2025-06-02T14:52:11.399Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/69/e0/552843e0d356fbb5256d21449fa957fa4eff3bbc135a74a691ee70c7c5da/typing_extensions-4.14.0-py3-none-any.whl", hash = "sha256:a1514509136dd0b477638fc68d6a91497af5076466ad0fa6c338e44e359944af", size = 43839, upload-time = "2025-06-02T14:52:10.026Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/f8/b1/0c11f5058406b3af7609f121aaa6b609744687f1d158b3c3a5bf4cc94238/typing_inspection-0.4.1.tar.gz", hash = "sha256:6ae134cc0203c33377d43188d4064e9b357dba58cff3185f22924610e70a9d28", size = 75726, upload-time = "2025-05-21T18:55:23.885Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/17/69/cd203477f944c353c31bade965f880aa1061fd6bf05ded0726ca845b6ff7/typing_inspection-0.4.1-py3-none-any.whl", hash = "sha256:389055682238f53b04f7badcb49b989835495a96700ced5dab2d8feae4b26f51", size = 14552, upload-time = "2025-05-21T18:55:22.152Z" },
]

[[package]]
name = "urllib3"
version = "2.5.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/15/22/9ee70a2574a4f4599c47dd506532914ce044817c7752a79b6a51286319bc/urllib3-2.5.0.tar.gz", hash = "sha256:3fc47733c7e419d4bc3f6b3dc2b4f890bb743906a30d56ba4a5bfa4bbff92760", size = 393185, upload-time = "2025-06-18T14:07:41.644Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a7/c2/fe1e52489ae3122415c51f387e221dd0773709bad6c6cdaa599e8a2c5185/urllib3-2.5.0-py3-none-any.whl", hash = "sha256:e6b01673c0fa6a13e374b50871808eb3bf7046c4b125b216f6bf1cc604cff0dc", size = 129795, upload-time = "2025-06-18T14:07:40.39Z" },
]

[[package]]
name = "uvicorn"
version = "0.34.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "h11" },
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/de/ad/713be230bcda622eaa35c28f0d328c3675c371238470abdea52417f17a8e/uvicorn-0.34.3.tar.gz", hash = "sha256:35919a9a979d7a59334b6b10e05d77c1d0d574c50e0fc98b8b1a0f165708b55a", size = 76631, upload-time = "2025-06-01T07:48:17.531Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6d/0d/8adfeaa62945f90d19ddc461c55f4a50c258af7662d34b6a3d5d1f8646f6/uvicorn-0.34.3-py3-none-any.whl", hash = "sha256:16246631db62bdfbf069b0645177d6e8a77ba950cfedbfd093acef9444e4d885", size = 62431, upload-time = "2025-06-01T07:48:15.664Z" },
]

[[package]]
name = "virtualenv"
version = "20.31.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "distlib" },
    { name = "filelock" },
    { name = "platformdirs" },
]
sdist = { url = "https://files.pythonhosted.org/packages/56/2c/444f465fb2c65f40c3a104fd0c495184c4f2336d65baf398e3c75d72ea94/virtualenv-20.31.2.tar.gz", hash = "sha256:e10c0a9d02835e592521be48b332b6caee6887f332c111aa79a09b9e79efc2af", size = 6076316, upload-time = "2025-05-08T17:58:23.811Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f3/40/b1c265d4b2b62b58576588510fc4d1fe60a86319c8de99fd8e9fec617d2c/virtualenv-20.31.2-py3-none-any.whl", hash = "sha256:36efd0d9650ee985f0cad72065001e66d49a6f24eb44d98980f630686243cf11", size = 6057982, upload-time = "2025-05-08T17:58:21.15Z" },
]

[[package]]
name = "wcwidth"
version = "0.2.13"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonh