# 07_dataset_class.py
# Level 1 — Topic 7: OOP and dataclasses

from dataclasses import dataclass, field
from typing import List, Any
import statistics


@dataclass
class Sample:
    features: List[float]
    label: Any = None


@dataclass
class Dataset:
    name: str
    samples: List[Sample] = field(default_factory=list)

    def add_sample(self, features: List[float], label=None):
        self.samples.append(Sample(features, label))

    def __len__(self):
        return len(self.samples)

    def mean_feature(self, index: int) -> float:
        values = [s.features[index] for s in self.samples]
        return statistics.mean(values)

    def summary(self):
        print(f"Dataset: {self.name}")
        print(f"Number of samples: {len(self)}")
        if self.samples:
            n_features = len(self.samples[0].features)
            print(f"Features per sample: {n_features}")
            for i in range(n_features):
                print(f"  Feature {i} mean: {self.mean_feature(i):.2f}")


if __name__ == "__main__":
    ds = Dataset(name="Iris-like")
    ds.add_sample([5.1, 3.5, 1.4, 0.2], label="setosa")
    ds.add_sample([7.0, 3.2, 4.7, 1.4], label="versicolor")
    ds.add_sample([6.3, 3.3, 6.0, 2.5], label="virginica")

    ds.summary()
    print(f"Length: {len(ds)}")
