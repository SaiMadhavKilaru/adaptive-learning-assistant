
QUESTIONS = [
    # BEGINNER - 10 QUESTIONS
    ("Beginner", "What does CPU stand for?",
     ["Central Processing Unit", "Computer Processing Utility", "Central Program Unit"], 0,
     "CPU stands for Central Processing Unit."),

    ("Beginner", "Which programming language is widely used in AI?",
     ["HTML", "Python", "CSS"], 1,
     "Python is widely used in AI and machine learning."),

    ("Beginner", "What is RAM used for?",
     ["Permanent storage", "Temporary working memory", "Internet access"], 1,
     "RAM temporarily stores data used by running programs."),

    ("Beginner", "What does HTML stand for?",
     ["HyperText Markup Language", "High Tech Machine Language", "Home Tool Markup Language"], 0,
     "HTML is used to structure web pages."),

    ("Beginner", "What does an operating system do?",
     ["Only plays videos", "Manages computer resources", "Only stores passwords"], 1,
     "An operating system manages hardware and software resources."),

    ("Beginner", "Which is a programming language?",
     ["Python", "Google", "Windows"], 0,
     "Python is a programming language."),

    ("Beginner", "What does AI stand for?",
     ["Automatic Internet", "Artificial Intelligence", "Advanced Interface"], 1,
     "AI stands for Artificial Intelligence."),

    ("Beginner", "What is a web browser?",
     ["An application for accessing websites", "A computer processor", "A programming language"], 0,
     "Browsers allow users to access and interact with websites."),

    ("Beginner", "Which symbol begins a Python comment?",
     ["//", "#", "@"], 1,
     "Python uses # for single-line comments."),

    ("Beginner", "What is the result of 2 + 3 in Python?",
     ["23", "5", "6"], 1,
     "The + operator adds the two integers."),

    # INTERMEDIATE - 10 QUESTIONS
    ("Intermediate", "What is a Python list?",
     ["An ordered collection", "A database server", "An operating system"], 0,
     "A list stores an ordered collection of items."),

    ("Intermediate", "Which Python library is commonly used for machine learning?",
     ["Flask", "scikit-learn", "Pygame"], 1,
     "scikit-learn provides tools for machine learning."),

    ("Intermediate", "What does a for loop do?",
     ["Deletes variables", "Repeats operations", "Installs libraries"], 1,
     "A for loop iterates over items."),

    ("Intermediate", "What is supervised learning?",
     ["Learning from labeled data", "Learning without data", "Manual interface design"], 0,
     "Supervised learning uses labeled training examples."),

    ("Intermediate", "Which Python function displays output?",
     ["show()", "print()", "output()"], 1,
     "Python uses print() to display text output."),

    ("Intermediate", "What is a Python dictionary?",
     ["A collection of key-value pairs", "A list of only numbers", "A text editor"], 0,
     "Dictionaries associate keys with values."),

    ("Intermediate", "What is the purpose of a function?",
     ["Organize reusable code", "Delete an application", "Restart a computer"], 0,
     "Functions organize reusable blocks of logic."),

    ("Intermediate", "Which keyword defines a function in Python?",
     ["function", "def", "method"], 1,
     "Python uses def to define functions."),

    ("Intermediate", "What does an API help applications do?",
     ["Communicate with other systems", "Increase screen brightness", "Replace RAM"], 0,
     "APIs allow software components to communicate."),

    ("Intermediate", "What is a training dataset used for?",
     ["Learning patterns for a model", "Designing computer hardware", "Changing display settings"], 0,
     "Machine-learning algorithms learn patterns from training data."),

    # ADVANCED - 10 QUESTIONS
    ("Advanced", "What is overfitting in machine learning?",
     ["Learning training-specific patterns too closely", "Using no data", "Running too quickly"], 0,
     "Overfitting means a model may not generalize well to new data."),

    ("Advanced", "Which algorithm is used for classification?",
     ["K-Means", "Logistic Regression", "PCA"], 1,
     "Logistic regression is commonly used for classification."),

    ("Advanced", "What is cross-validation used for?",
     ["Evaluating performance across data splits", "Deleting duplicates", "Increasing processor speed"], 0,
     "Cross-validation helps evaluate model generalization."),

    ("Advanced", "What does a confusion matrix summarize?",
     ["File sizes", "Classification results", "Network traffic"], 1,
     "A confusion matrix compares actual and predicted classes."),

    ("Advanced", "What is regularization used for?",
     ["Reducing overfitting", "Increasing file size", "Deleting all features"], 0,
     "Regularization constrains model complexity."),

    ("Advanced", "What is data leakage?",
     ["Using information unavailable at prediction time", "Losing a CSV file", "Compressing data"], 0,
     "Data leakage can produce misleading model evaluation results."),

    ("Advanced", "Which metric measures how many positive predictions are correct?",
     ["Recall", "Precision", "Mean Squared Error"], 1,
     "Precision is true positives divided by all predicted positives."),

    ("Advanced", "What is gradient descent?",
     ["An optimization algorithm", "A database language", "A sorting algorithm"], 0,
     "Gradient descent adjusts parameters to reduce an objective function."),

    ("Advanced", "What is the bias-variance tradeoff?",
     ["Balancing underfitting and overfitting", "Balancing RAM and storage", "Choosing interface colors"], 0,
     "The bias-variance tradeoff concerns competing sources of prediction error."),

    ("Advanced", "What is the purpose of a held-out test dataset?",
     ["Evaluate performance on unseen data", "Train on every example", "Store passwords"], 0,
     "A held-out test set helps estimate performance on unseen examples.")
]

assert len(QUESTIONS) == 30
print("All 30 questions are ready!")
