FIX/0.102a
----------
specs
^^^^^
   1. Test/NEW/Negative test
      - ``test_no_prods_demand_unchanged:`` no producers for province
      - ``test_no_demand_minus_shortfall:`` demand zero for province
	  - ``test_dept_demand_minus_profit:`` demand negative on province
	  - ``test_string_producers:`` check when invalid type as input *(NOT TYPEERROR)*
         - TypeError not occur/WHY?/Python string also iterable.
            - then, Need Type Assertion? (Guess not..)
   #. ``province.gen_province_doc:`` Changed to provide producer_doc also internally
   #. Test/NEW/Negative test
	  - ``test_string_producer:`` check when invalid producer data input *(TYPEERROR!)*


need improve
^^^^^^^^^^^^
   1. ``test_string_producers`` did not raised appropriate error **, UNSOLVED**
   #. substitute some tests with assertions **, UNSOLVED**

FIX/0.101rc
----------
specs
^^^^^
   1. Test/test_total_production
   #. Test/test_shortfall
   #. Test/test_profit
   #. Test/test_change_production **RENAMED**
      - Test/RENAME/test_change_production to test_diff_prod_to_shortfall
   #. Test/test_change_production/added additional check **MOVED**
      - Test/MOVE/test_change_production added to test_diff_prod_to_profit

fixes
^^^^^
   1. province/Province.init/Map object did not executed **, SOLVED**
      - Changed to list comprehension.(lazy eval not needed)
   #. AT/SPECS.5/Continous testing with single fixture better to avoid **, SOLVED**

need improve
^^^^^^^^^^^^
   1. Boundary Condition test Needed (ie, zero value input, Type errror input)

INIT(0.1)
---------
specs
^^^^^
   - New/province.py: Production Required based on different Province.
      - ``class Province``
         Province have Producers.
            Delegates the producer instances in tuple to ``self.producers`` by ``self.add_producers();``
      - ``get_samplea_province()``
         A function that return for dict-like sample Province data.(producers also)
   - New/producer.py: Actual producer who produces for now.
      - ``class Producer``
         Producer have single province to figout requied quantity.
            Delegate to data of province on ``self._province`` 
            (not sure that would be instance or not)

need improve 
^^^^^^^^^^^^
   1. ``<class Producer>._province`` **, UNSOLVED**
      - Delegation on Producer._province is too much.
      - Test does make self-reflecting for us.
   #. ``get_sample_province`` **, SOLVED**
      - Creates sample province but also producers included.
