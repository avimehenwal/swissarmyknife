import click


@click.command()
@click.option("--count", default=1, help="Number of greetings")
@click.option("--name", prompt="Your Name", help="The person to greet")
def app(count, name):
    """Simple program to greet name for total COUNT times"""
    for _ in range(count):
        click.echo(f"Hello, {name}")

