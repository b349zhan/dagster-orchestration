from dagster import asset, Definitions

@asset
def hello_world(context): 
    context.log.info("Hello world!")
    return "Hello world!"

defs = Definitions(
    assets=[hello_world]
)