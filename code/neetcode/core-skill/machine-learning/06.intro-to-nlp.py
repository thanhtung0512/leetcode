import torch
import torch.nn as nn
from torchtyping import TensorType

# https://neetcode.io/problems/nlp-intro
# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(
        self, positive: List[str], negative: List[str]
    ) -> TensorType[float]:
        word_set = set()
        combined = positive + negative

        for sentence in combined:
            for word in sentence.split():
                word_set.add(word)

        word_list = sorted(list(word_set))
        integer_of_word = {}
        for i, c in enumerate(word_list):
            integer_of_word[c] = i + 1

        def encode(sentence):
            integers = []
            for word in sentence.split():
                integers.append(integer_of_word[word])
            return integers

        combined_tensor = []
        for sentence in combined:
            print(sentence)
            combined_tensor.append(torch.tensor(encode(sentence)))

        return nn.utils.rnn.pad_sequence(combined_tensor, batch_first=True)
