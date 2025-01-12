import spacy
from spacy.training.example import Example
from spacy.util import minibatch, compounding

# Define the global variable for the model path
model_path = "intent_model"


def train_intent_model(training_data):
    print("Training the intent model...")
    # Hyperparameters
    BATCH_START = 4.0
    BATCH_END = 32.0
    BATCH_COMPOUND = 1.001
    N_ITERATIONS = 20  # Increased number of iterations
    DROPOUT_RATE = 0.2  # Reduced dropout rate

    # Load a pre-trained model
    nlp = spacy.load("en_core_web_md")

    # Add the text classifier to the pipeline
    if "textcat" not in nlp.pipe_names:
        textcat = nlp.add_pipe("textcat", last=True)
    else:
        textcat = nlp.get_pipe("textcat")

    # Add labels to the text classifier based on the training data
    for _, annotations in training_data:
        for label in annotations["cats"]:
            textcat.add_label(label)

    # Train the model
    optimizer = nlp.begin_training()
    for i in range(N_ITERATIONS):
        losses = {}
        batches = minibatch(training_data, size=compounding(BATCH_START, BATCH_END, BATCH_COMPOUND))
        for batch in batches:
            texts, annotations = zip(*batch)
            examples = [Example.from_dict(nlp.make_doc(text), annotation) for text, annotation in
                        zip(texts, annotations)]
            nlp.update(examples, drop=DROPOUT_RATE, losses=losses)
        print(f"Losses at iteration {i}: {losses}")

    # Save the model
    nlp.to_disk(model_path)
    print(f"Model trained and saved to '{model_path}'")
