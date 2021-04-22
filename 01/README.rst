0.31b
-----
specs
^^^^^
   - ``PerformanceCalculator.get_amount()`` uses amount_for function.
   - ``amounts.amount_for(aPerf)``  rename to -> ``amounts._amount_for(aPerf)``
   - rename amounts to performances.py
   - instance of ``PerformanceCalucaltor`` substituted setting ``enrich_perf(perf)``
   - ``render_to.{render_html, render_plain_text}``
      - fixed all accessing like ``perf["play"]`` to property access like ``perf.play``
      - removed ``amounts._amounts_for()``
   - renamed file *amounts.py* to *performances.py*.
      - amounts calculating is not main functionality in that module anymore.

0.31a
-----
specs
^^^^^
   - Extract, ``statements.statement``
      1. Extract setting rich data in ``context_data["performances"]`` as ``statements.enrich_perf(perf)``
      #. Marked ``perf["amount"]`` to be modified as Docstring at line 29.
      #. Set up variable play in ``statement.enrich_perf(perf)``.
      #. setup class and class call, for methods parameter.

need improve
^^^^^^^^^^^^
   - finish ``PerformanceCaulator`` class
      To substitute feature for setting up performace's amount and volume_credit

Check point 0.3->0.31
---------------------
need improve
^^^^^^^^^^^^
   - prepare calculations after new genre added.
   - amounts.amount_for function is if condition based, diverse return function.
      - These kind of work makes code trashful when it goes modified for more.

0.3rc
-----
specs
^^^^^
   1. Extracted functions for format strings.
      - *render_to.py*
         - ``itousd(amount)``
         - ``render_plain_text(data)``
      - *statements.py*
         - ``get_volume_credit(perf)``
         - ``get_total_volume_credits(perfs)``
         - ``get_total_amount(perfs)``
         - ``play_for(aPerformance)``
         - ``statement(invoice)``
   #. NEW/render_to/
      *render_html* returns htmls formatted string

0.23b
-----
specs
^^^^^
   1. Refactor/statements/ ``get_total_volume_credits``
      mainly run by ``functools.reduce``
   #. NEW/statements/ ``get_total_amount(perfs)``
      inline ``sum`` function call allocation -> substituted to explicit function. (just as another data.)

need improve
^^^^^^^^^^^^
   - context_data generator stay in *statements.py*
   - extract functions which formats and render to be in another file.
      - add ``render_html(data)`` to above.

0.23a
-----
specs
^^^^^
   1. Extract/statements.statement/get text
      - New/statements.render_plain_text
   #. Refactor/statements.render_plain_text
      - customer data now depends on caller function.
      - performance data depends on caller function.
         - Set performace list data as newly generated one(to protect original).
      - remove parameter invoice in render_plain_text.
      - make not to use external functions directly to parse advanced context_data
   #. Refactor/statements.statement
      - context_data sets ``{play: play_data by playid}`` by this function.
   #. Refactor/statements.render_plain_text
      - ``{'play'}`` data now handled by data argument itself.
      - ``statements.get_volume_credit(perf)`` applied above rule also.
      - ``amounts.amount_for(perf, play)`` arg ``play`` substitued by perf's ``play`` key-value.
   #. Refactor/statements/statement.context_data
      - Set amount by ``amount_for`` to each performance in ``context_data["performances"]``
         - in render_plain_text, use ``perf['amount'])`` when summations to ``have total_amount.``
         - in render_plain_text, remove ``total_amount`` variable.
      - Set total_amount and total_volume_credits from at ``context_data.``
         - in render_plain_text, remove function calls to set total values, ``total_amount, total_volume_credits``

need improve
^^^^^^^^^^^^
   1. convert iterations to pipeline.
      - FIX ``statements.get_total_volume_credit(perfs)``
      - NEW ``statements.get_total_amount(perfs)``

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
   - refered in need_improve in 0.1, 
      - result string should also be parsed to html.

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

