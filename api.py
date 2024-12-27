import csv
import logging
logger = logging.getLogger(__name__)



def main():
    logging.basicConfig(filename='training_and_testing.log', level=logging.INFO)
    # train the labeled data to get a model
    computed_model = training_data() # para needed

    # read the testing data and classify them
    string_list = testing_data_reader() # para needed
    embedding_matrix = convert_string_list_to_embedding_matrix(string_list)
    if not embedding_matrix:
        logger.info('no testing data provided')
    else:    
        result = classify(embedding_matrix, computed_model)
        with open('result.csv', 'w', newline='') as csvfile:
            result_writer = csv.writer(csvfile)
            result_writer.writerows(zip(string_list, result))

        
def convert_string_list_to_embedding_matrix(list_of_strings: list[str]) -> Optional[list[list[float]]]:
    embedding_matrix = []

    for string in list_of_strings:
        embedding = embed(string) # feature vector
        logger.info(f'adding {embedding} into embedding_matrix')
        embedding_matrix.append(testing_embedding)

    if len(embedding_matrix) == 0:
        return None

    return embedding_matrix


def testing_data_reader(test_file_location: str) -> Optional[list[str]]:
    string_list = []
    
    with open(test_file_location, newline='') as testing_csvfile:
        logger.info(f'testing {testing_csvfile}...')
        test_file_reader = csv.reader(testing_csvfile)
        for testing_data in test_file_reader:
            string_list.append(testing_embedding)

    return string_list

            
def training_data(labeled_data_file_location: str) -> Model:
    embedding_labeled_data_matrix = []
    embedding_labels = []
    with open(labeled_data_file_location, newline='') as labeled_csvfile:
        logger.info('loading training dataset')
        for row in labeled_data_file_location:
            sentence, label = row
            labeled_data_embedding = embed(sentence)
            logger.info(f'[training]adding {labeled_data_embedding} into embedding_labeled_data_matrix')
            embedding_labeled_data_matrix.append(labeled_data_embedding)
            logger.info(f'[training]adding {label} into embedding_labels')
            embedding_labels.append(label)

    computed_model = train(embedding_labeled_data_matrix, embedding_labels)
    logger.info(computed_model) # assuming this has __str__
    return computed_model        


def embed(text : str) -> List[float]:
    pass


def train(X : List[List[float]], y : List[int]) -> Model:
    pass


def classify(model : Model, text : str) -> int:
    pass

