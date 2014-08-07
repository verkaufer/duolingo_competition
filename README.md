duolingo_competition
====================

This package helps get a Duolingo competition running in seconds. A Duolingo competition simply involves tracking each language a player is learning and tracking his/her score for each language. Highest score for each language wins!

Usage
============
Install duolingo-api: `pip install duolingo-api`

Clone or download a ZIP of this repository:
 `https://github.com/verkaufer/duolingo_competition.git`

In the **duolingo_competition** folder, you will see two files: **usernames.txt** and **scores.txt**. Open **usernames.txt** and enter the Duolingo usernames of everyone in your competition. 

*Note: Each username must be on its own line*

Run `duolingo_competition.py` 

If everything worked, you should see a list of users, languages, and scores in scores.txt. Each time you run the script, the results will be appended to scores.txt.

*Example Output*:
> testuser

> German (Level 5) - [Score: 503]


License
===
Copyright 2014 David Gunter

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.