0.22
----
specs
^^^^^
   - NEW/statements.{get_volume_credit(perf), get_total_volume_credits(perfs)}
      1. moved total_credit into new for loop below it was at.
      #. Extraction/total_credits from ``get_volume_credit(perf)``
      #. total_credit loop moved to ``get_total_volume_credits(perfs)``
         - ``get_total...`` is caller to func ``get_volume...``
      #. ``statement{volume_credit}`` variable no needs, moved to inline expression.
      #. Test passed

need improve
^^^^^^^^^^^^
   - Tomorrow...lol!

0.22b
-----
specs
^^^^^
   1. NEW/statements.itocurrency(amount)
      returns int to string with comma separated per 3-characters between.
   #. rename itocurrency to itousd

need improve
^^^^^^^^^^^^
   - clean the statements.statement{volumnCredits} variable.

0.21b
-----
specs
^^^^^
   1. NEW/statements.play_for(aPerformance)
      returns object value data in ``plays`` by playID in 1st arg, aPerformance.
   2. REFACTOR/statements.statement
      1. 2nd arg(plays) removed
         now usage in plays can be reffered by ``play_for`` function.
      #. ``plays`` in global only approached by ``play_for()``
         ``plays`` renamed to ``_plays``

need improve
^^^^^^^^^^^^
   - set amount as currency format
      function needed.

0.2b
----
specs
^^^^^
   1. rename: amounts.amount_for/parametername
      ``perf`` to ``aPerformance``
   #. rename: amounts.amount_for/return variable name
      ``this_amount`` to ``result``

need improve
^^^^^^^^^^^^
   - checking invoice's performance playID with plays in not needed.

0.2a
----
specs
^^^^^
   - moved amount calculation function from ``statements.statement()`` to ``amounts.amount_for()``

need improve
^^^^^^^^^^^^
   - After function extracting, 
      1. look in the extracted code carefully,
      #. check for clarity of the variable names.

0.1
---
specs
^^^^^
   - New/resource: json file data
   - New/statements.py: format json program

need improve 
^^^^^^^^^^^^
   - result string should also be parsed to html.
   - Before refactor it, Prepare prper tests first.
      - Test does make self-reflecting for us.

