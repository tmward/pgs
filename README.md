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

### `chole_pgs.csv`

A comma-separated values file that is UTF-8 encoded.
Values delimited by a comma.
Column names are on the first line.
Missing values are represented by the string NA (not surrounding by quotes).
Values are quoted only if they contain a comma, quote, newline, or
an NA that is a literal string NA and not a missing value.
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

A comma-separated values file that is UTF-8 encoded.
Values delimited by a comma.
Column names are on the first line.
Missing values are represented by the string NA (not surrounding by quotes).
Values are quoted only if they contain a comma, quote, newline, or
an NA that is a literal string NA and not a missing value.
Details on the variable (column) names below:


|variable |class     |description |
|:--------|:-----|:-----------|
|`name`  | character    | Randomized UUID for PGS image |
|`gt`    |integer | Ground Truth PGS |
|`pgs_combo`     |integer | PGS Classifications for the Combined Adhesions/Appearance CV model |
|`pgs_surg2`     |integer | PGS Classifications for the Second Surgeon |
|`pgs_only`     |integer | PGS Classifications for the PGS-only CV Model |
|`fold`     |integer | Cross-validation fold. Does not apply for `pgs_surg2` |
