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
> French (Level 1) - [Score: 50]


MIT License
===
Copyright (c) 2015 David Gunter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
