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

