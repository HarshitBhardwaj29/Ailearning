from rich.console import Console
from rich.table import Table

console = Console()


def display_responses(responses):
    table = Table(
        title="LLM Response Comparison",
        show_lines=True
    )

    table.add_column("Model", style="cyan", width=15)
    table.add_column("Response", style="white")

    for model, response in responses.items():
        table.add_row(
            model,
            response if response else "[red]No Response[/red]"
        )

    console.print(table)