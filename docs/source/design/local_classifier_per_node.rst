.. _local-classifier-per-node-overview:

Local Classifier Per Node
=========================

One of the most popular approaches in the literature, the local classifier per node consists of training one binary classifier for each node of the class taxonomy, except for the root node.

.. figure:: local_classifier_per_node.svg
   :align: center

   Visual representation of the local classifier per node approach, adapted from [1]_.

There are multiple ways to define the set of positive and negative examples for training the binary classifiers. In HiClass we implemented 6 policies described at [1]_, which were based on previous work from [2]_ and [3]_. In the table below the notation used to define the sets of positive and negative examples is presented, as described by [1]_.

=============================  ===============================================================
Symbol                         Meaning
-----------------------------  ---------------------------------------------------------------
:math:`Tr`                     The set of all training examples
:math:`Tr^+(c_i)`              The set of positive training examples of :math:`c_i`
:math:`Tr^-(c_i)`              The set of negative training examples of :math:`c_i`
:math:`\uparrow (c_i)`         The parent category of :math:`c_i`
:math:`\downarrow (c_i)`       The set of children categories of :math:`c_i`
:math:`\Uparrow (c_i)`         The set of ancestor categories of :math:`c_i`
:math:`\Downarrow (c_i)`       The set of descendant categories of :math:`c_i`
:math:`\leftrightarrow (c_i)`  The set of sibling categories of :math:`c_i`
:math:`*(c_i)`                 Denotes examples whose most specific known class is :math:`c_i`
=============================  ===============================================================

.. [1] Silla, C. N., & Freitas, A. A. (2011). A survey of hierarchical classification across different application domains. Data Mining and Knowledge Discovery, 22(1), 31-72.

.. [2] Eisner, R., Poulin, B., Szafron, D., Lu, P., & Greiner, R. (2005, November). Improving protein function prediction using the hierarchical structure of the gene ontology. In 2005 IEEE symposium on computational intelligence in bioinformatics and computational biology (pp. 1-10). IEEE.

.. [3] Fagni, T., & Sebastiani, F. (2007, October). On the selection of negative examples for hierarchical text categorization. In Proceedings of the 3rd language technology conference (pp. 24-28).
