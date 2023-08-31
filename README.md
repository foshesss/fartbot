# fartbot
[https://fartclub.aspear.net](https://fartclub.aspear.net)

## Guide to use codebase
1. Create a virtual environment: `python -m venv venv`
2. Activate virtual environment: `. venv/bin/activate`
3. Install/update dependencies: `poetry install`
4. Start the app locally: `flask --app main --debug run`

## How to add new libraries
`poetry add library@version`

```python
(
    userid, # 0 
    longeststreak_start_date, # 1
    longeststreak_end_date, # 2
    currentstreak_start_date, # 3
    currentstreak_end_date, # 4
    longeststreak_length, # 5
    currentstreak_length, # 6
    pfp,
    name,
    total
) 
```
## Expected DB JSON Format
```json
[
    [
        "", // userid
        "2023-01-04", // longeststreak_start_date
        "2023-01-04", // longeststreak_end_date
        "2023-01-04", // currentstreak_start_date
        "2023-01-04", // currentstreak_end_date
        0, // longesstreakt_length
        0, // currentstreak_length
        "", // pfp
        "derpmonster83", // username
        500 // total
    ]
]
```
