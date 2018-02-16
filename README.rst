Datasets for Training Defensive Neural Networks
===============================================

.. image:: https://imgur.com/uXO9dCE.png

These are the Anti-Nex datasets for training deep neural networks to defend against network exploits (only web applications added so far). Under the hood these models are trained and tuned using Keras and Tensorflow.

These datasets were created by merging datasets recorded from `OWASP ZAP attack simulations`_ and `multi-user non-attack simulations with Django`_.

.. _OWASP ZAP attack simulations: https://github.com/jay-johnson/network-pipeline/tree/master/simulations#network-traffic-simulations
.. _multi-user non-attack simulations with Django: https://github.com/jay-johnson/train-ai-with-django-swagger-jwt#multi-tenant-simulations

Each model has an associated guide for preparing datasets and training models:

- `Protecting Flask RESTplus`_ with **89%** accuracy
- `Protecting React and Redux`_ with **87%** accuracy
- `Protecting Vue`_ with **83%** accuracy
- `Protecting Django`_ with **70%** accuracy
- `Protecting Spring`_ with **66%** accuracy

This is a 75 MB gif I recorded while capturing the ``non-attack`` training data by running the multi-user simulation with the capture tools all active inside a single vm (note: from inside imgur, right click on the gif and select ``Open in video in new tab`` to make it larger to read the text):

.. raw:: html

    <a href="https://i.imgur.com/fHReLOW.gifv" target="_blank"><img src="https://imgur.com/4hirZBO.png"/></a>

.. _Protecting Django: https://github.com/jay-johnson/antinex-datasets/tree/master/v1/webapps/django
.. _Protecting Flask RESTplus: https://github.com/jay-johnson/antinex-datasets/tree/master/v1/webapps/flask-restplus
.. _Protecting React and Redux: https://github.com/jay-johnson/antinex-datasets/tree/master/v1/webapps/react-redux
.. _Protecting Vue: https://github.com/jay-johnson/antinex-datasets/tree/master/v1/webapps/vue
.. _Protecting Spring: https://github.com/jay-johnson/antinex-datasets/tree/master/v1/webapps/spring
