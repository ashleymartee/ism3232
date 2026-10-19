# debug_log.md
# Author: [Ashley Marte]

## Bug 1
Error type: KeyError
File + line: week8_buggy.py, line 12, inside get_total (called from line 21: total = get_total(records))
What the error means: Python tried to look up the key 'amount' in a dictionary (rec['amount']), but at least one record in records has no key with that exact name. It might be missing, misspelled, or differently capitalized (like 'Amount' or 'amt').
What I told the duck: The goal of get_total is to add up the amount from every record in records. It starts with total at 0 and loops through the list. On each pass, rec is one dictionary, and line 12 adds rec['amount'] to total. I expected every record to have an 'amount' key. But the error says one doesn’t, so my expectation doesn’t match the data. The bug is probably in one record’s key, not in the loop itself.
What I tried: I tried to fix the get_total line by reformatting it
How I fixed it: I realized ['amount'] was misspelled in another line and was able to debug it there

## Bug 2
Error type: N/A
File + line: N/A
What the error means: N/A
How I fixed it: I never got a second error. After I fixed my first bug and ran it again I got the correct output.

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records
True
Did pytest pass? Yes 

## AI Literacy Reflection
Did I use AI? Yes
If yes -- exact prompt I used: I am not getting a second error message here but think I am supposed to, what can I do?
What AI explained: To try to run pytest and see what I get
What I changed myself: I ran pytest but I was getting errors from previous files not the one I'm working on currently, so I just moved past it.
Can I explain every fixed line? Yes

## What I learned
I learned that a lot of bugs come from the data and not the code. Printing each record inside the loop showed me exactly where things went wrong, so I didn’t have to guess.
