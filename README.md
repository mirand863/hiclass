# HiClass

HiClass is an open-source Python library for hierarchical classification compatible with scikit-learn.

[![Deploy PyPI](https://github.com/mirand863/hiclass/actions/workflows/deploy-pypi.yml/badge.svg?event=push)](https://github.com/mirand863/hiclass/actions/workflows/deploy-pypi.yml) [![Documentation Status](https://readthedocs.org/projects/hiclass/badge/?version=latest)](https://hiclass.readthedocs.io/en/latest/?badge=latest) [![codecov](https://codecov.io/gh/mirand863/hiclass/branch/main/graph/badge.svg?token=PR8VLBMMNR)](https://codecov.io/gh/mirand863/hiclass) [![Downloads PyPI](https://static.pepy.tech/personalized-badge/hiclass?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=pypi)](https://pypi.org/project/hiclass/) [![Downloads Conda](https://img.shields.io/conda/dn/conda-forge/hiclass?label=conda)](https://anaconda.org/conda-forge/hiclass) [![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

✨ Here is a **demo** that shows HiClass in action on hierarchical data:

- Classify a consumer complaints dataset from the consumer financial protection bureau: [consumer-complaints](https://colab.research.google.com/drive/1rQTDxWcck-PH4saKzrofQ7Sg9W23lYZv?usp=sharing)

## Quick links

- [Features](#features)
- [Benchmarks](#benchmarks)
- [Roadmap](#roadmap)
- [Who is using HiClass?](#who-is-using-hiclass)
- [Install](#install)
- [Quick start](#quick-start)
- [Step-by-step walk-through](#step-by-step-walk-through)
- [API documentation](#api-documentation)
- [FAQ](#faq)
- [Support](#support)
- [Contributing](#contributing)
- [Getting the latest updates](#getting-the-latest-updates)
- [Citation](#citation)

## Features

- **Python lists and NumPy arrays:** Handles Python lists and NumPy arrays elegantly, out-of-the-box.
- **Pandas Series and DataFrames:** If you prefer to use pandas, that is not an issue as HiClass also works with Pandas.
- **Sparse matrices:** HiClass also supports features (X_train and X_test) built with sparse matrices, both for training and predicting, which can save you heaps of memory.
- **Parallel training:** Training can be performed in parallel on the hierarchical classifiers, which allows parallelization regardless of the implementations available on scikit-learn.
- **Build pipelines:** Since the hierarchical classifiers inherit from the BaseEstimator of scikit-learn, pipelines can be built to automate machine learning workflows.
- **Hierarchical metrics:** HiClass supports the computation of hierarchical precision, recall and f-score, which are more appropriate for hierarchical data than traditional metrics.
- **Compatible with pickle:** Easily store trained models on disk for future use.

**Any feature missing on this list?** Search our [issue tracker](https://github.com/mirand863/hiclass/issues) to see if someone has already requested it and add a comment to it explaining your use-case. Otherwise, please open a new issue describing the requested feature and possible use-case scenario. We prioritize our roadmap based on user feedback, so we would love to hear from you.

## Benchmarks

### Consumer complaints dataset with ~600K training examples

This first benchmark was executed on Google Colab with only 1 core, using Logistic Regression as the base classifier.

|Classifier|Training Time (hh:mm:ss)|Memory Usage (GB)|Disk Usage (MB)|F-score|
|----------|:-----------------------:|:---------------:|:-------------:|:-----:|
|[Local Classifier per Parent Node](https://colab.research.google.com/drive/1yZlQ9UnBEGdkIpnJ3pBwvbZ-U0SXL-UG?usp=sharing)|00:52:58|5.28|121|**0.7689**|
|[Local Classifier per Node](https://colab.research.google.com/drive/1rQTDxWcck-PH4saKzrofQ7Sg9W23lYZv?usp=sharing)|**00:33:02**|**4.87**|123|0.7647|
|[Local Classifier per Level](https://colab.research.google.com/drive/1b_Qb2d6RhSO7ICYTIsxH6ZqCVgeKWmll?usp=sharing)|04:14:45|10.71|123|0.7684|
|[Flat Classifier](https://colab.research.google.com/drive/10jgzA65WaoTc7tFfrlKlhlwPBs3PFy9m?usp=sharing)|03:20:26|9.57|**107**|0.7636|

This second benchmark is similar to the last one, except that it was executed on a cluster node running GNU/Linux with 512 GB physical memory and 128
cores provided by two AMD EPYC™ 7742 processors, and each model had 12 cores available for training.

|Classifier|Training Time (hh:mm:ss)|Memory Usage (GB)|Disk Usage (MB)|F-score|
|----------|:-----------------------:|:---------------:|:-------------:|:-----:|
|Local Classifier per Parent Node|00:19:26|4.08|118|**0.7688**|
|Local Classifier per Node|**00:06:21**|**3.97**|120|0.7648|
|Local Classifier per Level|01:22:51|4.08|120|0.7684|
|Flat Classifier|01:38:19|6.63|**104**|0.7634|

This third benchmark was also executed on the same cluster node as the previous benchmark and 12 cores were provided for each model, however, the base classifier was LightGBM instead.

|Classifier|Training Time (hh:mm:ss)|Memory Usage (GB)|Disk Usage (MB)|F-score|
|----------|:-----------------------:|:---------------:|:-------------:|:-----:|
|Local Classifier per Parent Node|00:31:16|4.06|80|0.7062|
|Local Classifier per Node|**00:24:21**|5.58|318|**0.7603**|
|Local Classifier per Level|01:55:27|**4.02**|40|0.6382|
|Flat Classifier|00:26:16|4.44|**32**|0.4788|

Lastly, this fourth benchmark was also executed on the same cluster node as the previous benchmarks and 12 cores were provided for each model, however, the base classifier was random forest instead.

|Classifier|Training Time (hh:mm:ss)|Memory Usage (GB)|Disk Usage (GB)|F-score|
|----------|:-----------------------:|:---------------:|:-------------:|:-----:|
|Local Classifier per Parent Node|03:23:02|**36.43**|**11**|0.7245|
|Local Classifier per Node|02:19:45|40.98|13|**0.7519**|
|Local Classifier per Level|04:25:45|142.28|45|0.7208|
|Flat Classifier|**00:29:26**|80.47|38|0.6515|

For reproducibility, a Snakemake pipeline was created. Instructions on how to run it and source code are available at [https://github.com/mirand863/hiclass/tree/main/benchmarks/consumer_complaints](https://github.com/mirand863/hiclass/tree/main/benchmarks/consumer_complaints).

We would love to benchmark with larger datasets, if we can find them in the public domain. If you have any suggestions for hierarchical datasets that are public, please let us know by opening an issue. We would also be delighted if you are able to share benchmarks from your own large datasets. Please send us a pull request.

## Roadmap

Here is our public roadmap: https://github.com/mirand863/hiclass/projects/1.

We do Just-In-Time planning, and we tend to reprioritize based on your feedback. Hence, items you see on this roadmap are subject to change. We prioritize features based on the number of people asking for it, features/fixes that are small enough and can be addressed while we work on other related features, features/fixes that help improve stability & relevance and features that address interesting use cases that excite us! If you would like to have a request prioritized, we ask that you add a detailed use-case for it, either as a comment on an existing issue (besides a thumbs-up) or in a new issue. The detailed context helps.


## Who is using HiClass?

HiClass is currently being used in [HiTaC](https://gitlab.com/dacs-hpi/hitac), a hierarchical taxonomic classifier for fungal ITS sequences.

If you use HiClass in one of your projects and would like to have it listed here, please send us a pull request or contact fabio.malchermiranda@hpi.de.

## Install

### Option 1: Pip


HiClass and its dependencies can be easily installed with pip:

```shell
pip install hiclass
```

### Option 2: Conda

Alternatively, HiClass and its dependencies can also be installed with conda:

```shell
conda install -c conda-forge hiclass
```

Further installation instructions are available on our [getting started guide](https://hiclass.readthedocs.io/en/latest/get_started/index.html). This will guide you through the process of setting up an isolated Python virtual environment with conda, venv or pipenv before installing hiclass with conda or pip, and how to verify a successful installation.

## Quick start

Here's a quick example showcasing how you can train and predict using a local classifier per node, with a `RandomForestClassifier` for each node:

```python
from hiclass import LocalClassifierPerNode
from sklearn.ensemble import RandomForestClassifier

# Define data
X_train = [[1], [2], [3], [4]]
X_test = [[4], [3], [2], [1]]
Y_train = [
    ['Animal', 'Mammal', 'Sheep'],
    ['Animal', 'Mammal', 'Cow'],
    ['Animal', 'Reptile', 'Snake'],
    ['Animal', 'Reptile', 'Lizard'],
]

# Use random forest classifiers for every node
rf = RandomForestClassifier()
classifier = LocalClassifierPerNode(local_classifier=rf)

# Train local classifier per node
classifier.fit(X_train, Y_train)

# Predict
predictions = classifier.predict(X_test)
```

HiClass can also be adopted in scikit-learn pipelines, and fully supports sparse matrices as input. In order to demonstrate the use of both of these features, we will use the following example:

```python
from hiclass import LocalClassifierPerParentNode
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Define data
X_train = [
    'Struggling to repay loan',
    'Unable to get annual report',
]
X_test = [
    'Unable to get annual report',
    'Struggling to repay loan',
]
Y_train = [
    ['Loan', 'Student loan'],
    ['Credit reporting', 'Reports']
]
```

Now, let's build a pipeline that will use `CountVectorizer` and `TfidfTransformer` to extract features as sparse matrices:

```python
# Use logistic regression classifiers for every parent node
lr = LogisticRegression()
pipeline = Pipeline([
    ('count', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('lcppn', LocalClassifierPerParentNode(local_classifier=lr)),
])
```

Finally, let's train and predict with the pipeline we just created:

```python
# Train local classifier per parent node
pipeline.fit(X_train, Y_train)

# Predict
predictions = pipeline.predict(X_test)
```

## Step-by-step walk-through

A step-by-step walk-through is available on our documentation hosted on [Read the Docs](https://hiclass.readthedocs.io/en/latest/index.html).

This will guide you through the process of installing hiclass within a virtual environment, training, predicting, persisting models and much more.

## API documentation

Here's our official API documentation, available on [Read the Docs](https://hiclass.readthedocs.io/en/latest/api/index.html).

If you notice any issues with the documentation or walk-through, please let us know by opening an issue here: [https://github.com/mirand863/hiclass/issues](https://github.com/mirand863/hiclass/issues).

## FAQ

### How do the hierarchical classifiers work?

A detailed description on how the classifiers work is available at the [Algorithms Overview](https://hiclass.readthedocs.io/en/latest/algorithms/index.html) section on Read the Docs.

## Support

If you run into any problems or issues, please create a [Github issue](https://github.com/mirand863/hiclass/issues) and we'll try our best to help.

We strive to provide good support through our issue tracker on Github. However, if you'd like to receive private support with:

- Phone / video calls to discuss your specific use case and get recommendations
- Private discussions over Slack or Mattermost

Please reach out to fabio.malchermiranda@hpi.de.

## Contributing

We are a small team on a mission to democratize hierarchical classification, and we will take all the help we can get! If you would like to get involved, here is information on [contribution guidelines and how to test the code locally](https://github.com/mirand863/hiclass/blob/main/CONTRIBUTING.md).

You can contribute in multiple ways, e.g., reporting bugs, writing or translating documentation, reviewing or refactoring code, requesting or implementing new features, etc.

## Getting the latest updates

If you'd like to get updates when we release new versions, please click on the "Watch" button on the top and select "Releases only". Github will then send you notifications along with a changelog with each new release.

## Citation

If you use HiClass, please cite:

> Miranda, Fábio M., Niklas Köehnecke, and Bernhard Y. Renard. "HiClass: a Python library for local hierarchical classification compatible with scikit-learn." arXiv preprint arXiv:2112.06560 (2021).

```latex
@article{miranda2021hiclass,
  title={HiClass: a Python library for local hierarchical classification compatible with scikit-learn},
  author={Miranda, F{\'a}bio M and K{\"o}ehnecke, Niklas and Renard, Bernhard Y},
  journal={arXiv preprint arXiv:2112.06560},
  year={2021}
}
```

**Note**: If you use HiClass in your GitHub projects, please add `hiclass` in the `requirements.txt`.

In addition, we would like to list publications that use HiClass to solve hierarchical problems. If you would like your manuscript to be added to this list, please email the reference, the name of your lab, department and institution to fabio.malchermiranda@hpi.de
