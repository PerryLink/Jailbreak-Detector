import click
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from .core import JailbreakDetector
from .patterns import PatternManager

console = Console()

@click.group()
def main():
    pass

@main.command()
@click.argument('text', required=False)
@click.option('--file', type=click.Path(exists=True), help='Read text from file')
@click.option('--json', 'output_json', is_flag=True, help='Output in JSON format')
@click.option('--quiet', is_flag=True, help='Only output detection result')
def detect(text, file, output_json, quiet):
    if file:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
    elif not text:
        click.echo("Error: Provide text or use --file option")
        return

    detector = JailbreakDetector()
    result = detector.detect(text)

    if output_json:
        import json
        click.echo(json.dumps({
            "is_jailbreak": result.is_jailbreak,
            "confidence": result.confidence,
            "categories": result.categories,
            "matched_patterns": [{"pattern": m["pattern"], "position": [m["start"], m["end"]]}
                                for m in result.matched_patterns]
        }))
        return

    if quiet:
        click.echo(str(result.is_jailbreak).lower())
        return

    if result.is_jailbreak:
        console.print(Panel.fit(
            "[bold red]🛡️  BLOCKED  🛡️[/bold red]\n\n"
            "[yellow]Jailbreak attempt detected![/yellow]",
            border_style="red"
        ))

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Pattern")
        table.add_column("Position")
        table.add_column("Category")

        for match in result.matched_patterns:
            table.add_row(
                match["pattern"],
                f"{match['start']}-{match['end']}",
                match["metadata"]["category"]
            )

        console.print(table)
        console.print(f"\n[bold]Confidence:[/bold] {result.confidence}")
    else:
        console.print("[bold green]✅ SAFE[/bold green] - No jailbreak patterns detected")

@main.group()
def patterns():
    pass

@patterns.command('list')
def list_patterns():
    pattern_file = Path(__file__).parent.parent.parent / "data" / "patterns.json"
    pm = PatternManager().load_from_json(pattern_file)

    for category, pattern_list in pm.get_patterns_by_category().items():
        console.print(f"\n[bold cyan]{category}[/bold cyan]")
        for pattern in pattern_list:
            console.print(f"  • {pattern}")

@patterns.command('add')
@click.argument('pattern')
@click.option('--category', required=True, help='Pattern category')
def add_pattern(pattern, category):
    pattern_file = Path(__file__).parent.parent.parent / "data" / "patterns.json"
    pm = PatternManager().load_from_json(pattern_file)
    pm.add_pattern(category, pattern)
    pm.save_to_json(pattern_file)
    console.print(f"[green]✓[/green] Added pattern '{pattern}' to category '{category}'")

@patterns.command('stats')
def pattern_stats():
    pattern_file = Path(__file__).parent.parent.parent / "data" / "patterns.json"
    pm = PatternManager().load_from_json(pattern_file)

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Category")
    table.add_column("Count", justify="right")

    total = 0
    for category, pattern_list in pm.get_patterns_by_category().items():
        count = len(pattern_list)
        table.add_row(category, str(count))
        total += count

    console.print(table)
    console.print(f"\n[bold]Total patterns:[/bold] {total}")

if __name__ == '__main__':
    main()
