# Pizzas API 

Simple Django Rest Framework Application that enables to make pollings  
related to pizz'ish things. 

* Create new pollings by posting its name at `/api/polls/`  
  (of course, detailed url is also possible). I've done that, because  
  pizzas can be rated from different point of views i.e best pizza below 10$  
  or best vege pizza.

* Pizzas are available at `/api/pizzas/` (foreign key to polling)

* To vote at particular pizza just patch at, for instance `/api/pizzas/1/vote`

This is all for now :) Additional behaviour added to DRF was tested.
