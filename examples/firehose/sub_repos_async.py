import asyncio

from atproto.firehose import (
    AsyncFirehoseSubscribeReposClient,
    parse_subscribe_repos_message,
)


async def main():
    client = AsyncFirehoseSubscribeReposClient()

    async def on_message_handler(message):
        print(message.header, parse_subscribe_repos_message(message))

    await client.start(on_message_handler)


if __name__ == '__main__':
    # use run() for higher Python version
    asyncio.get_event_loop().run_until_complete(main())
