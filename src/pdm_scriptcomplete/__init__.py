import argparse
import readline
import subprocess

from pdm.cli.commands.base import BaseCommand
from pdm.core import Core
from pdm.project import Project


class ScriptCompleteCommand(BaseCommand):
    """
    pdm_scriptcomplete

    Registers a new script command that lets users choose a pdm script using tab completion
    """

    arguments = []

    @staticmethod
    def setup_tab_completion(scripts: list[str]) -> None:
        def complete(text: str, state: int):
            matches = []
            for item in scripts:
                if item.startswith(text):
                    matches.append(item)

            if state < len(matches):
                return matches[state]
            else:
                return None

        readline.set_completer(complete)
        readline.parse_and_bind("tab: complete")

    def handle(self, project: Project, options: argparse.Namespace) -> None:
        """The command handler function.

        :param project: the pdm project instance
        :param options: the parsed Namespace object
        """

        scripts = [str(script) for script in project.scripts]
        if not scripts:
            return project.core.ui.echo(message="No scripts found!", err=True)

        self.setup_tab_completion(scripts)

        try:
            user_input = input(f"Choose script (<TAB> for list): ")
            subprocess.run(f"pdm {user_input}", shell=True)
        except KeyboardInterrupt:
            project.core.ui.echo(message="Choice aborted by user.", err=True)


def plugin(core: Core) -> None:
    """Register pdm plugin to pdm-core."""
    core.register_command(ScriptCompleteCommand, "script")
