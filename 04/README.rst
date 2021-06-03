FIX/0.101a
----------
specs
^^^^^
   1. Test/test_total_production
   #. Test/test_shortfall
   #. Test/test_profit to be failed

fixes
^^^^^
   1. province/Province.init/Map object did not executed **, SOLVED**
      - Changed to list comprehension.(lazy eval not needed)

need improve
^^^^^^^^^^^^

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
