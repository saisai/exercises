import asyncio
import json

async def fake_request(_url: str, **_kwargs: object) -> str:
    await asyncio.sleep(2)
    return "foo"

async def get_words(sql_line: str) -> str:
    print("2. INSIDE get_words:")
    baseurl = "http://localhost:4000/wordscape"
    body = json.dumps({"sqlline": sql_line})
    headers = {"Content-type": "application/json"}
    my_words = await fake_request(
        f"{baseurl}/read", body=body, method="POST", headers=headers
    )
    print("3. my_words INSIDE get_words:", my_words)
    return my_words

async def main() -> None:
    sql = """
    select upper(word) as word from dictionary.dictionary_words_20230103
    where word = 'help'\n """
    print("1. BUILD SQL:", sql)
    words = await get_words(sql)
    print("4. #### WORDS RETURNED FROM get_words:", words)

if __name__ == "__main__":
    asyncio.run(main())
