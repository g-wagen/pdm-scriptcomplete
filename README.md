# PDM Script Complete

This [PDM](https://github.com/pdm-project/pdm) plugin enables tab completion for pdm scripts.

## Installation
### PDM
PDM needs to be installed prior to installing the plugin. Please follow the instructions from the official [PDM README](https://github.com/pdm-project/pdm/README.md).

### The plugin
You can install the plugin with [PDM](https://github.com/pdm-project/pdm):
```commandline
pdm self add pdm-scriptcomplete
```

As a local-only plugin:

```toml
# pyproject.toml
[tool.pdm]
plugins = ["pdm-scriptcomplete"]
```

```commandline
pdm install --plugins
```

## Usage

```commandline
pdm script <ENTER>
```