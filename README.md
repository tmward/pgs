# pgs

This repository holds software used to perform analyses and
generate figures/tables for the 2021
Society of American Gastrointestinal and Endoscopic Surgeons (SAGES)
Annual Meeting "Best Papers" Podium Presentation, number S107,
titled:
"Artificial Intelligence Prediction of Cholecystectomy Operative Course from Automated Identification of Gallbladder Inflammation".
Additionally, it was submitted for publication consideration.

# Overview of repository contents

## `data/`

All `.csv` files are
comma-separated values files that are UTF-8 encoded.
Values delimited by a comma.
Column names are on the first line.
Missing values are represented by the string NA (not surrounding by quotes).
Values are quoted only if they contain a comma, quote, newline, or
an NA that is a literal string NA and not a missing value.

### `adhesions_gt.csv`

Contains the adhesions ground truth for each representative PGS image.
Details on the variable (column) names below:

|variable |class     |description |
|:--------|:-----|:-----------|
|`fname`  |character    | Filename of PGS image |
|`labels`    | character | adhesions ground truth |

### `appearance_gt.csv`

Contains the appearance ground truth for each representative PGS image.
Details on the variable (column) names below:

|variable |class     |description |
|:--------|:-----|:-----------|
|`fname`  |character    | Filename of PGS image |
|`labels`    | character | appearance ground truth |


### `chole_pgs.csv`

Contains the PGS, randomized surgeon ID, and various video metrics
for each video.
Details on the variable (column) names below:


|variable |class     |description |
|:--------|:-----|:-----------|
|`videoid`  |integer    | Randomized sequential video ID |
|`surgid`    |integer | Randomized sequential surgeon ID|
|`pgs`     |integer | Parkland Grading Scale rating |
|`time_until_1st_clip`     |double | Time (minutes) from start of dissection until first clip applied in Calot's Triangle|
|`time_cvs_attained`     |double | Time (minutes) from start of dissection until first seen view of Critical View of Safety|
|`laparascopic_duration`     |double | Duration (minutes) of laparoscopic portion of the case (Intra-operative cholangiogram time removed)|
|`dissection_duration` | double | Duration (minutes) of cystic structures' dissection |
|`gb_removal_duration` | double | Duration (minutes) of removing gallbladder from the liver bed after all cystic structures divided. Does not include prolonged hemostasis of liver bed after or during gallbladder removal|
|`gb_hole` | logical | Whether a hole was created in the gallbladder during removal from the liver bed |
|`gb_holes` | integer | Number of holes created in the gallbladder during removal from the liver bed |

### `cv_results.csv`

Contains the results of the two computer vision models
and the second surgeon's annotations for PGS for representative images.

|variable |class     |description |
|:--------|:-----|:-----------|
|`name`  | character    | Randomized UUID for PGS image |
|`gt`    |integer | Ground Truth PGS |
|`pgs_combo`     |integer | PGS Classifications for the Combined Adhesions/Appearance CV model |
|`pgs_surg2`     |integer | PGS Classifications for the Second Surgeon |
|`pgs_only`     |integer | PGS Classifications for the PGS-only CV Model |
|`fold`     |integer | Cross-validation fold. Does not apply for `pgs_surg2` |

### `pgs_gt.csv`

Contains the PGS ground truth for each representative PGS image.
Details on the variable (column) names below:

|variable |class     |description |
|:--------|:-----|:-----------|
|`fname`  |character    | Filename of PGS image |
|`labels`    | character | PGS ground truth |

## `output/`
Empty directory that will store files generated by the code.

## `src/`

### `cv_model_analyses.Rmd`

Rmarkdown document that contains the code to analyse the CV model performance
and compare to that of a second surgeon annotator.
A knitted pdf that shows the code and results is also provided.

### `cv_model.py`

Code to train and evaluate the performance of the CNN that were trained.
It trains three networks.
The first classifies PGS alone.
The second classifies the degree of gallbladder adhesions.
The third classifies gallbladder appearance.
Requires CSV files generated by `pgs_analyses.Rmd`.

### `pgs_analyses.Rmd`

Rmarkdown document that contains the code
to analyse the effect of PGS on various outcomes.
A knitted pdf that shows the code and results is also provided.

### `prep_folds.Rmd`

Rmarkdown document that contains the code
to generate the 10 folds for 10-fold cross-validation
of the computer vision model.
A knitted pdf that shows the code and results is also provided.

# Questions, comments, concerns, need help?
Please contact me in the communication medium of your preference listed on my
[Contact page](https://thomasward.com/contact/).

# LICENSE

All code is under the ISC license:

Copyright (c) 2021 Thomas Ward <thomas@thomasward.com>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
