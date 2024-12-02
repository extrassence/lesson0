import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")

    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял шар номер {i}")

    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman("Иван", 2)),
        asyncio.create_task(start_strongman("Петр", 3)),
        asyncio.create_task(start_strongman("Алексей", 1))
    ]

    await asyncio.gather(*tasks)



asyncio.run(start_tournament())