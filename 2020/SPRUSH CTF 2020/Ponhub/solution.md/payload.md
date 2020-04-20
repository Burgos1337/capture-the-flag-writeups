```
{ "$lookup":
     {
       "from": "flag",
       "let": { "f": "$flag"},
       "pipeline": [
            { "$match":
                { "$expr":
                    { "$and":
                        [
                           { "$eq": ["$title", "$$f" ] }
                        ]
                    }
                }
            }
        ],
        "as": "myflag"
      }
 }
```