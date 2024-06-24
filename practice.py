import asyncio

async def cook_appetizer():
    print("Start cooking appetizer...")
    await asyncio.sleep(2)  # Simulate time taken to cook
    print("Appetizer is ready!")

async def cook_main_course():
    print("Start cooking main course...")
    await asyncio.sleep(5)
    print("Main course is ready!")

async def cook_dessert():
    print("Start cooking dessert...")
    await asyncio.sleep(3)
    print("Dessert is ready!")

async def cook_meal():
    await asyncio.gather(
        cook_appetizer(),
        cook_main_course(),
        cook_dessert()
    )

# Run the asynchronous cook_meal function
asyncio.run(cook_meal())
