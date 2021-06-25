#!/usr/bin/env python39
import json
from fastai.vision.all import *


def main():
    """This will run, for all three CV networks trained, the 10-fold
    cross-validation training. Adjusts paths as needed."""
    annotation_path = Path("../output/")
    for output_class in ("adhesions", "appearances", "pgs"):
        print(f"Running model for {output_class}")
        for i in range(1, 11):
            print(f"{i} split")
            dls = ImageDataLoaders.from_csv(
                annotation_path,
                f"{output_class}_split_{i}.csv",
                folder="../data/imgs",
                valid_col="is_valid",
                item_tfms=Resize(460),
                batch_tfms=aug_transforms(size=224),
            )
            learn = cnn_learner(dls, resnet50, metrics=error_rate)
            learn.fine_tune(35, 2e-3)
            df = pd.read_csv(annotation_path / f"{output_class}_split_{i}.csv")
            fns = [f for f in df[df.is_valid]["fname"]]
            predictions = {
                f: str(learn.predict("../data/imgs" / f)[0]) for f in fns
            }
            with open(pgs_path / f"../output/{output_class}_split_{i}.json", "w") as jfile:
                json.dump(predictions, jfile)
    print("Done")


if __name__ == "__main__":
    main()
